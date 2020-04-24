from django.views.generic import TemplateView

from forum.models import Theme, Section


class ForumListView(TemplateView):
    template_name = 'forum/forum_list.html'

    def get_context_data(self, **kwargs):
        context = super(ForumListView, self).get_context_data(**kwargs)
        context['themes'] = Theme.objects.filter(is_game=False)
        context['game_themes'] = Theme.objects.filter(is_game=True)
        context['sections'] = Section.objects.all()
        return context
