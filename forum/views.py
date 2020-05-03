from django.utils import timezone
from django.views.generic import TemplateView, DetailView, CreateView

from forum.forms import GamePostForm, SystemPostForm
from forum.models import Theme, Section, Post


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
        # context['game_form'] = GamePostForm
        # context['system_form'] = SystemPostForm
        return context
