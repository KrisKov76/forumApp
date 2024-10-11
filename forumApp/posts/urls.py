from django.urls import path, include
from forumApp.posts.views import details_page, Index, IndexView, \
    RedirectHomeView, DashboardView, AddPostView, EditPostView, DeletePostView

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('add-post/', AddPostView.as_view(), name='add-post'),
    path('<int:pk>/', include([
        path('delete-post/', DeletePostView.as_view(), name='delete-post'),
        path('details-post/', details_page, name='details-post'),
        path('edit-post/', EditPostView.as_view(), name='edit-post'),
    ])),
    path('redirect-home/', RedirectHomeView.as_view(), name='redirect-home')
]