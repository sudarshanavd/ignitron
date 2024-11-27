from django.urls import path
from .views import EventSelectionView, EventDetailView

app_name='e_admin'

urlpatterns = [
    path('event-selection/<str:username>/', EventSelectionView.as_view(), name='event_selection'),
    path('event-detail/<str:username>/<str:event_name>/', EventDetailView.as_view(), name='event_detail'),
]

