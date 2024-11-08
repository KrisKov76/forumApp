from django.conf.urls.static import static
from django.urls import path, include

from django.conf import settings
from forumApp.posts.views import IndexView, \
    RedirectHomeView, DashboardView, AddPostView, EditPostView, DeletePostView, PostDetailView, approve_post

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('add-post/', AddPostView.as_view(), name='add-post'),
    path('<int:pk>/', include([
        path('approve/', approve_post, name='approve'),
        path('delete-post/', DeletePostView.as_view(), name='delete-post'),
        path('details-post/', PostDetailView.as_view(), name='details-post'),
        path('edit-post/', EditPostView.as_view(), name='edit-post'),
    ])),
    path('redirect-home/', RedirectHomeView.as_view(), name='redirect-home')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)