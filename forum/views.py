from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.template.defaultfilters import register
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import TemplateView, DetailView, FormView, DeleteView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from forum.forms import SystemPostForm, GamePostForm
from forum.models import Theme, Section, Post, SectionSerializer, Like, Dislike
from rest_framework.views import APIView


class ForumListView(TemplateView):
    template_name = 'forum/forum_list.html'

    def get_context_data(self, **kwargs):
        context = super(ForumListView, self).get_context_data(**kwargs)
        context['themes'] = Theme.objects.filter(is_game=False)
        context['game_themes'] = Theme.objects.filter(is_game=True)
        context['sections'] = Section.objects.all()
        return context


class ForumPageView(DetailView):
    model = Theme
    template_name = 'forum/forum_page.html'
    context_object_name = 'theme'

    def get_context_data(self, **kwargs):
        context = super(ForumPageView, self).get_context_data(**kwargs)
        posts = Post.objects.filter(theme=self.object).order_by('when')
        context['posts'] = posts
        context['first_likes'] = Like.objects.filter(post=self.object.first_post).count()
        context['first_dislikes'] = Dislike.objects.filter(post=self.object.first_post).count()
        likes = {}
        dislikes = {}
        for p in posts:
            likes[p.pk] = Like.objects.filter(post=p).count()
            dislikes[p.pk] = Dislike.objects.filter(post=p).count()
        context['likes'] = likes
        context['dislikes'] = dislikes
        return context


class SystemPostFormView(FormView):
    form_class = SystemPostForm
    template_name = 'forum/new_system_post.html'

    def get_success_url(self):
        return reverse_lazy(self.request.POST.get('next', 'Forum:list'))

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.when = timezone.now()
        form.save()
        return super(SystemPostFormView, self).form_valid(form)


class GamePostFormView(FormView):
    form_class = GamePostForm
    template_name = 'forum/new_game_post.html'

    def get_form_kwargs(self):
        kwargs = super(GamePostFormView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_success_url(self):
        return reverse_lazy('Forum:list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.when = timezone.now()
        form.save()
        return super(GamePostFormView, self).form_valid(form)


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('Forum:list')


@login_required
def like(request, pk):
    if Like.objects.filter(post_id=pk, user=request.user).exists():
        Like.objects.get(post_id=pk, user=request.user).delete()
    else:
        if Dislike.objects.filter(post_id=pk, user=request.user).exists():
            Dislike.objects.get(post_id=pk, user=request.user).delete()
        Like.objects.create(post_id=pk, user=request.user)
    next_page = request.POST.get('next', 'main_page')
    return HttpResponseRedirect(next_page)


@login_required()
def dislike(request, pk):
    if Dislike.objects.filter(post_id=pk, user=request.user).exists():
        Dislike.objects.get(post_id=pk, user=request.user).delete()
    else:
        if Like.objects.filter(post_id=pk, user=request.user).exists():
            Like.objects.get(post_id=pk, user=request.user).delete()
        Dislike.objects.create(post_id=pk, user=request.user)
    next_page = request.POST.get('next', 'main_page')
    return HttpResponseRedirect(next_page)


# filter for getting an item from dictionary by it's key in templates
@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


# old version of api for Section objects
# class AllSectionView(APIView):
#
#     def get(self):
#         sections = SectionSerializer(Section.objects.all(), many=True)
#         return Response({'sections': sections.data})
#
#     def post(self, request):
#         section = request.data.get('section')
#         serializer = SectionSerializer(data=section)
#         if serializer.is_valid(raise_exception=True):
#             section_saved = serializer.save()
#         return Response({"success": "Section '{}' created successfully".format(section_saved.name)})
#
#     def put(self, request, pk):
#         saved_section = get_object_or_404(Section.objects.all(), pk=pk)
#         data = request.data.get('article')
#         serializer = SectionSerializer(instance=saved_section, data=data, partial=True)
#         if serializer.is_valid(raise_exception=True):
#             section_saved = serializer.save()
#         return Response({
#             "success": "Section '{}' updated successfully".format(section_saved.name)
#         })
#
#     def delete(self, pk):
#         section = get_object_or_404(Section.objects.all(), pk=pk)
#         section.delete()
#         return Response({
#             "message": "Section with id `{}` has been deleted.".format(pk)
#         }, status=204)


class AllSectionsView(ListCreateAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

    def perform_create(self, serializer):
        return serializer.save()


class SingleSectionView(RetrieveUpdateDestroyAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
