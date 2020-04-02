from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('note/<int:pk>/', views.post_detail, name='post_detail'),
    path('note/new/', views.post_new, name='post_new'),
    path('note/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('note/<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('signup/', views.signup, name='signup'),
    path('', include("django.contrib.auth.urls")),
    path('upload/', views.upload, name='upload'),
    path('showfiles/', views.files_list, name='file_list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
