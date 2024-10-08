from django.urls import path
from quotes.views import AddTagView, AddAuthorView, AddQuoteView
from quotes.views import AuthorDetailView

urlpatterns = [
    path('add_tag/', AddTagView.as_view(), name='add_tag'),
    path('add_author/', AddAuthorView.as_view(), name='add_author'),
    path('add_quote/', AddQuoteView.as_view(), name='add_quote'),
    path('author/<int:id>/', AuthorDetailView.as_view(), name='author_detail'),
]
