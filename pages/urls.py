from django.urls import path

from .views import PagesListView,BlogDetaView

urlpatterns = [
path('', PagesListView.as_view(), name='home'),
path('post/<int:pk>/',BlogDetaView.as_view(), name='post_detail'),
]