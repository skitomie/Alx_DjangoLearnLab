from django.urls import path
from ..notificationsss.views import NotificationListView

urlpatterns = [
    path('notifications/', NotificationListView.as_view(), name='notifications'),
]
