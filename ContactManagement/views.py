from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from .models import Contact


def home(request):
    context = {
        'contacts': Contact.objects.all()
    }
    return render(request, 'ContactManagement/home.html', context)


class ContactListView(ListView):
    model = Contact
    template_name = 'ContactManagement/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'contacts'
    ordering = ['name']
    paginate_by = 25


class UserContactListView(ListView):
    model = Contact
    template_name = 'ContactManagement/user_list.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'contacts'
    ordering = ['name']
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Contact.objects.filter(author=user).order_by('name')


class ContactDetailView(DetailView):
    model = Contact


class ContactCreateView(LoginRequiredMixin, CreateView):
    model = Contact
    fields = ['name', 'number', 'occupation']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ContactUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Contact
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class ContactDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Contact
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
