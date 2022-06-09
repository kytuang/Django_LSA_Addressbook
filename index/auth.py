from audioop import reverse
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import FormView
from .models import Address
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
#this page is to handle all the users' auth

#class to create login page
class CreateLoginView(LoginView):
    template_name = 'index/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('addressbooks')
    
#class to register user
class RegisterUser(FormView):
    template_name = 'index/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('addressbooks')
    
    #if form is good, save
    def form_valid(self, form):
        user = form.save() #save user form
        
        #if user is logged in
        if user is not None:
            login(self.request, user)
        return super(RegisterUser, self).form_valid(form)
    
    
    
    