from django.urls import path
from . import views
from . import auth
from .views import BookDelete, BookList, BookDetail, BookCreate, BookUpdate, DeleteView

#Users Authentications
from .auth import CreateLoginView, LogoutView, RegisterUser

# from django.views import views

urlpatterns = [
    #auth views
    path('login/', CreateLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),

    
    #views
    path('', BookList.as_view(), name='addressbooks'),
    # path('search/', BookList.as_view(), name='search'),
    path('addressbook/<int:pk>/', BookDetail.as_view(), name='addressbook'),
    path('book-create', BookCreate.as_view(), name='book-create'),
    path('book-edit<int:pk>', BookUpdate.as_view(), name='book-edit'),
    path('book-delete<int:pk>', BookDelete.as_view(), name='book-delete'),
   
]

