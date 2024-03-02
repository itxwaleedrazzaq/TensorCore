from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView,CreateView,DeleteView,UpdateView,View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from . import models
from django.urls import reverse_lazy
from . import forms
from django.db.models import Prefetch

class ContactUsView(TemplateView):
    template_name = 'portfolio/contact.html'
    
class FrontPageView(TemplateView):
    template_name = 'portfolio/frontpage.html'

class UserSignupView(View):
    def get(self,request):
        form = forms.UserForm()
        form_dict = {'userform':form,'reg':False}
        return render(request,'registration/signup.html',context=form_dict)
    
    def post(self,request):
        reg = False
        if request.method == 'POST':
            form = forms.UserForm(data=request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.set_password(user.password)
                user.save()
                reg = True
            else:
                print('INVALID FORM')
        form_dict = {'userform':form,'reg':reg}
        return render(request,'registration/signup.html',context=form_dict)
    

class CategoryListView(ListView):
    model = models.Category
    context_object_name = 'categories'
    template_name = 'portfolio/category_list.html'

    def get_queryset(self):
        # Assuming you have a 'projects' related name in your Category model
        return models.Category.objects.prefetch_related(
            Prefetch('projects', queryset=models.Project.objects.filter(publish_date__lte=timezone.now()).order_by('-publish_date'))
        )

class CategoryDetailView(DetailView):
    model = models.Category
    fields = ('title','abstract')
    context_object_name = 'categories_detail'
    template_name = 'portfolio/category_detail.html'

class CreateProjectView(CreateView):
    #login_url = '/login/'
    #redirect_field_name = 'portfolio/project_detail.html'
    form_class = forms.ProjectForm
    model = models.Project
    
class UpdateProjectView(UpdateView):
    #login_url = '/login/'
    #redirect_field_name = 'portfolio/project_detail.html'
    form_class = forms.ProjectForm
    model = models.Project

    

class DeleteProjectView(DeleteView):
    model = models.Project
    success_url = reverse_lazy('portfolio:list_view')
    
