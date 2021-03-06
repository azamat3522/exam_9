from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import PhotoForm
from webapp.models import Photo


class PhotoListView(ListView):
    model = Photo
    template_name = 'index.html'
    ordering = ['-created_at']


class PhotoDetailView(DetailView):
    model = Photo
    template_name = 'detail.html'


class PhotoCreateView(LoginRequiredMixin, CreateView):
    model = Photo
    template_name = 'create.html'
    form_class = PhotoForm


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('webapp:index')


class PhotoUpdateView(PermissionRequiredMixin, UpdateView):
    model = Photo
    template_name = 'update.html'
    context_object_name = 'photo'
    form_class = PhotoForm
    permission_required = 'webapp.change_photo'
    permission_denied_message = "Доступ запрещён"

    def get_success_url(self):
        return reverse('webapp:photo_detail', kwargs={'pk': self.object.pk})


class PhotoDeleteView(PermissionRequiredMixin, DeleteView):
    model = Photo
    template_name = 'delete.html'
    context_object_name = 'photo'
    success_url = reverse_lazy('webapp:index')
    permission_required = 'webapp.delete_photo'
    permission_denied_message = "Доступ запрещён"
