from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *


@login_required(login_url='home')
def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            text = form.cleaned_data['text']
            tags = form.cleaned_data['tags']
            user = request.user.id
            note = Note.objects.filter(name=name, user_id=user).first()
            if note is None:
                if tags == '':
                    note = Note.objects.create(
                        name=name,
                        text=text,
                        user_id=user
                    )
                else:
                    note = Note.objects.create(
                        name=name,
                        text=text,
                        user_id=user
                    )
                    note.tags.set(tags)
                note.save()
                messages.success(request, 'Success create')
                return redirect('create_note')
            else:
                messages.error(request, 'Note name already exist!')
        else:
            messages.error(request, 'Error valid from')
    else:
        form = NoteForm()

    tags = Tag.objects.all()
    return render(request, 'notes/create_note.html', {'form': form, 'tags': tags})


@login_required(login_url='home')
def create_tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            tag = form.cleaned_data['tag']
            user = request.user.id
            tags = Tag.objects.filter(tag=tag, user_id=user).first()
            if tags is None:
                tags = Tag.objects.create(tag=tag, user_id=user)
                tags.save()
                messages.success(request, 'Success create')
                return redirect('create_tag')
            else:
                messages.error(request, 'Tag already exist!')
        else:
            messages.error(request, 'Error valid from')
    else:
        form = TagForm()
    return render(request, 'notes/create_tag.html', {'form': form})


class TagsByUser(ListView):
    model = Tag
    initial = {'key': 'value'}
    template_name = 'notes/tags.html'
    context_object_name = 'tags_data'

    def get_queryset(self):
        return Tag.objects.filter(user_id=self.request.user.id)

    def get_context_data(self, *, object_list=None, **kwargs):
        object_list = self.get_queryset()
        context = super().get_context_data(**kwargs, object_list=object_list)
        return context


@login_required(login_url='home')
def delete_tag(request, tag_id):
    tag = get_object_or_404(Tag, pk=tag_id)
    tag.delete()
    return redirect('tags')


@login_required(login_url='home')
def user_note(request, pk):
    user = request.user.id
    instance = Note.objects.filter(pk=pk, user_id=user).first()
    if request.method == 'GET':
        if instance is None:
            return redirect('notes_list')
        form = NoteForm(instance=instance)
        return render(request, 'notes/edit_note.html', {'form': form})
    if request.method == 'POST':
        if request.POST.get('b-delete') == 'delete':
            instance.delete()
            return redirect('notes_list')
        form = NoteForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('notes_list')
        return render(request, 'notes/edit_note.html', {'form': form})


class NoteByUser(ListView):
    model = Note
    initial = {'key': 'value'}
    template_name = 'notes/notes_view.html'
    context_object_name = 'notes_data'

    def get_queryset(self):
        return Note.objects.filter(user_id=self.request.user.id)

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        notes_list = self.request.POST.getlist('note')
        Note.objects.filter(pk__in=notes_list).delete()
        return render(request, self.template_name, context)

    def get_context_data(self, *, object_list=None, **kwargs):
        object_list = self.get_queryset()
        context = super().get_context_data(**kwargs, object_list=object_list)
        return context


@login_required(login_url='home')
def notes_by_tag(request, tag_id):
    notes_data = Note.objects.filter(tags__pk=tag_id, user_id=request.user.id).all()
    return render(request, 'notes/notes_view.html', {'notes_data': notes_data})


#
# class NotesByTag(DetailView):
#     model = Note
#     template_name = 'notes/notes_by_tag_view.html'
#     context_object_name = 'notes_by_tag_data'
#     pk_tag_kwarg = 'tag_id'
#
#     def get_queryset(self):
#         return Note.objects.filter(category_id=self.kwargs['category_id'], is_published=True)


class SearchTag(ListView):
    template_name = 'notes/tags.html'
    context_object_name = 'tags_data'

    def get_queryset(self):
        if self.request.GET.get('q') is None:
            return None
        return Tag.objects.filter(tag__icontains=self.request.GET.get('q'), user_id=self.request.user.id)


class Search(ListView):
    template_name = 'notes/notes_view.html'
    context_object_name = 'notes_data'

    def get_queryset(self):
        if self.request.GET.get('a') is None:
            return None
        return Note.objects.filter(
            Q(name__icontains=self.request.GET.get('a'), user_id=self.request.user.id) |
            Q(text__icontains=self.request.GET.get('a'), user_id=self.request.user.id) |
            Q(tags__tag__icontains=self.request.GET.get('a'), user_id=self.request.user.id))
