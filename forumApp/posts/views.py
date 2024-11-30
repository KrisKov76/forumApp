from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import modelform_factory
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, RedirectView, ListView, FormView, CreateView, UpdateView, DeleteView, \
    DetailView
from forumApp.posts.forms import PostCreateForm, PostDeleteForm, SearchForm, PostEditForm, CommentFormSet
from forumApp.posts.models import Post


class IndexView(TemplateView):
    template_name = 'common/index.html'  # static way
    extra_context = {
        'static_time': datetime.now(),
    }  # static way

    def get_context_data(self, **kwargs):  # dynamic way
        context = super().get_context_data(**kwargs)
        context['dynamic_time'] = datetime.now()
        return context

    def get_template_names(self):  # dynamic way
        if self.request.user.is_authenticated:
            return ['common/index_logged_in.html']
        else:
            return ['common/index.html']


class DashboardView(ListView, FormView):
    template_name = 'posts/dashboard.html'
    context_object_name = 'posts'
    form_class = SearchForm
    success_url = reverse_lazy('dashboard')
    model = Post


def get_queryset(self):
    queryset = self.model.objects.all()

    # Проверяваме всички разрешения на потребителя (индивидуални и групови)
    if 'posts.can_approve_post' not in self.request.user.has_permissions():
        queryset = queryset.filter(approved=True)

    # Проверяваме дали има заявка за търсене и я прилагаме
    if 'query' in self.request.GET:
        query = self.request.GET.get('query')
        queryset = queryset.filter(title__icontains=query)

    return queryset


def approve_post(request, pk):
    post = Post.objects.get(pk=pk)
    post.approved = True
    post.save()
    return redirect(request.META.get('HTTP_REFERER'))

class AddPostView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'posts/add-post.html'
    success_url = reverse_lazy('dashboard')


class EditPostView(UpdateView):
    model = Post
    template_name = 'posts/edit-post.html'
    success_url = reverse_lazy('dashboard')

    def get_form_class(self):
        if self.request.user.is_superuser:
            return modelform_factory(Post, fields=('title', 'content', 'author', 'languages', 'image'))
        else:
            return modelform_factory(Post, fields=('content',))


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/details-post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['formset'] = CommentFormSet()
        return context

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        formset = CommentFormSet(request.POST or None)

        if formset.is_valid():
            for form in formset:
                if form.cleaned_data:
                    comment = form.save(commit=False)
                    comment.post = post
                    comment.save()

            return redirect('details-post', pk=post.id)

        context = self.get_context_data()
        context['formset'] = formset

        return self.render_to_response(context)


# def details_page(request, pk: int):
#     post = Post.objects.get(pk=pk)
#     formset = CommentFormSet(request.POST or None)
#
#     if request.method == "POST":
#         if formset.is_valid():
#             for form in formset:
#                 if form.cleaned_data:
#                     comment = form.save(commit=False)
#                     comment.post = post
#                     comment.save()
#
#             return redirect('details-post', pk=post.id)
#
#     context = {
#         "post": post,
#         "formset": formset,
#     }

# return render(request, 'posts/details-post.html', context)


class DeletePostView(DeleteView, FormView):
    model = Post
    template_name = 'posts/delete-post.html'
    success_url = reverse_lazy('dashboard')

    def get_initial(self):
        pk = self.kwargs.get(self.pk_url_kwarg)
        post = Post.objects.get(pk=pk)
        return post.__dict__


class RedirectHomeView(RedirectView):
    url = reverse_lazy('index')  # static way

    def get_redirect_url(self, *args, **kwargs):  # dynamic_way
        pass
