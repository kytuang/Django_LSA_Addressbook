from ast import Add
from email.headerregistry import Address
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from .models import Address
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q

from django.contrib.auth.mixins import LoginRequiredMixin #restricting users

# Class based views within Django

#List all of the addressbooks in "home" or booklist.html
class BookList(LoginRequiredMixin, ListView):
    model = Address
    template_name = 'index/book_list.html'
    context_object_name = 'books'
     
    #only show data for logged in user
    def get_queryset(self):
        if 'q' in self.request.GET:
            q = self.request.GET['q']
            
            #creating search queries through all fields
            search_queries = Q(Q(first_name__icontains=q) | Q(last_name__icontains=q) | 
                               Q(mobile_number__icontains=q) | Q(home_number__icontains=q) | Q(work_number__icontains=q) |
                               Q(email__icontains=q) | Q(address__icontains=q))
            
            #return the search queries based on logged-in user's directory
            return Address.objects.filter(search_queries, user=self.request.user)
   
        #if empty string search returns all user's addressbook
        else:
            return Address.objects.filter(user=self.request.user) #filter authenticated user
      
        
#Show Individual Object
class BookDetail(LoginRequiredMixin, DetailView):
    model = Address
    template_name = 'index/addressbook.html'
    context_object_name = 'book'
    
# Create New AddressBook with CreateView
class BookCreate(LoginRequiredMixin, CreateView):
    model = Address
    fields = ['first_name', 'last_name', 'mobile_number', 'home_number', 'work_number', 'email', 'address'] #delete the users selection options
    success_url = reverse_lazy('addressbooks') #if successful, return to home
    template_name = 'index/book_form.html'
 
    #store the users' form
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(BookCreate, self).form_valid(form)

#Edit current AddressBook with UpdateView
class BookUpdate(LoginRequiredMixin, UpdateView):
    model = Address
    fields = ['first_name', 'last_name', 'mobile_number', 'home_number', 'work_number', 'email', 'address'] #delete the users selection options
    success_url = reverse_lazy('addressbooks')
    template_name = 'index/book_form.html'
    
#Delete page with DeleteView
class BookDelete(LoginRequiredMixin, DeleteView):
    model = Address
    success_url = reverse_lazy('addressbooks')
    template_name = 'index/book_delete_confirm.html'
    

    

    

    
    
    
    
    
    
    
    
    



