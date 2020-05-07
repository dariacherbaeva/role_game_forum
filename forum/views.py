from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import TemplateView, DetailView, FormView
from rest_framework.response import Response

from forum.forms import SystemPostForm
from forum.models import Theme, Section, Post, SectionSerializer, Like
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
        context['posts'] = Post.objects.filter(theme=self.object).order_by('when')
        return context


class SystemPostFormView(FormView):
    form_class = SystemPostForm
    template_name = 'forum/new_system_post.html'

    def get_success_url(self):
        return reverse_lazy(self.request.POST.get('next', 'main_page'))

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.when = timezone.now()
        form.instance.theme = self.request.POST.get('theme')
        form.save()
        return super(SystemPostFormView, self).form_valid(form)


class AllSectionView(APIView):
    def get(self, request):
        sections = SectionSerializer(Section.objects.all(), many=True)
        return Response({'sections': sections.data})


@login_required
def like(request, pk):
    if Like.objects.filter(post_id=pk, user=request.user).exists():
        Like.objects.delete(post_id=pk, user=request.user)
    else:
        Like.objects.create(post_id=pk, user=request.user)
    next_page = request.POST.get('next', '/')
    return HttpResponseRedirect(next_page)
