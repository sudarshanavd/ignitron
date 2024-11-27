from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from coordinator.models import StudentDetail  # Assuming the model for participant details
from django.contrib.auth.models import User
from django.db.models import Q
from django.core.paginator import Paginator

class EventSelectionView(TemplateView):
    template_name = "event_selection.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add the username from URL kwargs
        context['username'] = self.kwargs['username']
        
        # List of event names (You can dynamically fetch this if needed)
        context['event_names'] = [
            "Hackathon", "Idea-thon", "Data Hunt", "Poster Presentation",
            "Psy(c)ury", "Robo Quest", "Tech Expo", "Tech Debate", "Blind Code"
        ]
        return context


class EventDetailView(LoginRequiredMixin, TemplateView):
    template_name = 'event_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        event_name = self.kwargs['event_name']
        username = self.kwargs['username']

        # Filter the students by event name
        students = StudentDetail.objects.filter(event_name=event_name)
        query = self.request.GET.get('q', '')

        # Apply search filter if query exists
        if query:
            students = students.filter(
                Q(team_name__icontains=query) |
                Q(team_lead_name__icontains=query) |
                Q(contact_number__icontains=query) |
                Q(institute_name__icontains=query) |
                Q(district__icontains=query) |
                Q(participant_2__icontains=query) |
                Q(participant_3__icontains=query) |
                Q(participant_4__icontains=query)
            )

        # Pagination setup
        from django.core.paginator import Paginator
        paginator = Paginator(students, 10)  # 10 students per page
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        # Add necessary context to the template
        context.update({
            'username': username,
            'event_name': event_name,
            'page_obj': page_obj,
            'query': query,
        })
        return context