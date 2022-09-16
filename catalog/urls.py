from django.urls import path
from . import views


urlpatterns = [
    # path(url pattern, call view.index if pattern detected, unique identifier name of this url mapping
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    # use '<int:pk>' to capture the book id (short for primary key)
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path(r'borrowed/', views.LoanedBooksAllListView.as_view(), name='all-borrowed'),
    # redirect URLs with the format /catalog/book/<bookinstance_id>/renew/ to the function in views
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
    path('author/create/', views.AuthorCreate.as_view(), name='author-create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author-update'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author-delete'),
    path('book/create/', views.BookCreate.as_view(), name='book-create'),
    path('book/<int:pk>/update/', views.BookUpdate.as_view(), name='book-update'),
    path('book/<int:pk>/delete/', views.BookDelete.as_view(), name='book-delete'),
]

"""
We can use the name to "reverse" the mapper. For example, we can use the name parameter to link to 
our home page from any other page by adding the following link in a template:
<a href="{% url 'index' %}">Home</a>.
"""

"""
re_path(): 
path() is simple and useful for the (very common) cases where we just want to capture any string or 
integer. If you need more refined filtering then you can use the re_path() method, which uses 
"regular expression" that is not that intuitive. 
eg: re_path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
"""