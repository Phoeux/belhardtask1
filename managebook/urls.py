from django.urls import path
from django.views.decorators.cache import cache_page

from managebook import views


urlpatterns = [
    # path('hello/', cache_page(2)(views.BookView.as_view()), name='hello'),
    path('hello/', views.BookView.as_view(), name='hello'),
    path('add_rate/<int:rate>/<int:book_id>', views.AddRateBook.as_view(), name='add_rate'),
    path('add_like2comment/<int:comment_id>', views.AddLike.as_view(), name='add_like2comment'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('add_book/', views.AddNewBook.as_view(), name='add_book'),
    path('add_comment/<int:book_id>', views.AddComment.as_view(), name='add_comment'),
    path('delete_book/<int:book_id>', views.DeleteBook.as_view(), name='delete_book'),
    path('update_book/<str:book_slug>', views.UpdateBook.as_view(), name='update_book'),
    path('delete_comment/<int:comment_id>', views.DeleteComment.as_view(), name='delete_comment'),
    path('update_comment/<int:comment_id>', views.UpdateComment.as_view(), name='update_comment'),
]
