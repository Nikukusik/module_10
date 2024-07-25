from django.forms import ModelForm, CheckboxSelectMultiple

from quotes.models import Tag, Author, Quote


class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = ['name']

class AuthorForm(ModelForm):

    class Meta:
        model = Author
        fields = ['name', 'description']

class QuoteForm(ModelForm):
    class Meta:
        model = Quote
        fields = ['text', 'author', 'tags']
        widgets = {
            'tag': CheckboxSelectMultiple()
        }