from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from quotes.forms import TagForm, AuthorForm, QuoteForm
from quotes.models import Quote, Author, Tag
from django.contrib.auth.mixins import LoginRequiredMixin


class MainView(ListView):
    model = Quote
    template_name = 'quotes/main.html'
    context_object_name = 'quotes'

class AuthorListView(ListView):
    model = Author
    template_name = 'quotes/authors.html'
    context_object_name = 'author'


class AddTagView(LoginRequiredMixin, CreateView):
    login_url = '/login'
    model = Tag
    template_name = 'quotes/add_tag.html'
    success_url = reverse_lazy('main')
    form_class = TagForm

class AddAuthorView(LoginRequiredMixin, CreateView):
    login_url = '/login'
    model = Author
    template_name = 'quotes/add_author.html'
    success_url = reverse_lazy('main')
    form_class = AuthorForm

class AddQuoteView(LoginRequiredMixin, CreateView):
    login_url = '/login'
    model = Quote
    template_name = 'quotes/add_quote.html'
    success_url = reverse_lazy('main')
    form_class = QuoteForm


