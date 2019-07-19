from django.shortcuts import render,get_object_or_404,redirect
from .models import Contact
from django.views.generic import ListView,DetailView,DeleteView,CreateView,UpdateView
from django.db.models import Q  #for seaching complex search
# from django.views.generic.edit import CreateView
from django.urls import reverse_lazy #for redirection 
from django.contrib.auth.forms import UserCreationForm #user creation form..
from django.contrib.auth.mixins import LoginRequiredMixin #login required..
from django.contrib.auth.decorators import login_required #login required..
# Create your views here.
# def home(request):
#     data=Contact.objects.all()
#     context={}
#     context['data']=data
#     context['home']=home
#     return render(request,'index.html',context)

class homepageview(LoginRequiredMixin,ListView):
    template_name='index.html'
    model=Contact
    context_object_name = 'data'

    def get_queryset(self):
        contacts = super().get_queryset()
        return contacts.filter(manager=self.request.user)

@login_required
def details(request,task_id):
    # val=Contact.objects.get(pk=task_id)
    val=get_object_or_404(Contact,pk=task_id)
    context={}
    context['val']=val
    return render(request,'detail.html',context)

class detailpageview(LoginRequiredMixin, DetailView):
    template_name='detail.html'
    model=Contact
    context_object_name = 'val'   

@login_required
def delete(request,task_id):
    v1=Contact.objects.get(pk=task_id)
    v1.delete()
    return redirect('home')

@login_required
def search(request):
    if request.GET:
        search_name=request.GET['search_name']
        search_term=Contact.objects.filter(
            Q(name__icontains=search_name) |
            Q(email__icontains=search_name) |
            Q(gender__icontains=search_name) |
            Q(phone__icontains=search_name) |
            Q(info__iexact=search_name)
        )
        if search_term:
             context={}
             context['search_name']=search_name
             search_term_filter=search_term.filter(manager=request.user)
             context['search_term']=search_term_filter
        else:
            context={}
            context['msg']="No Data"
            return render(request,'search.html',context)
        return render(request,'search.html',context)
    else:
        return redirect('home')


class CreateBaseView(CreateView):
    model=Contact
    template_name='create.html'
    fields=['name','email','phone','info','gender','image']
    # success_url=reverse_lazy('home')

    def form_valid(self,form):
        instance=form.save(commit=False)
        instance.manager=self.request.user
        instance.save()
        return redirect('home')


class UpdateBaseView(LoginRequiredMixin,UpdateView):
    model=Contact
    template_name='update.html'
    fields=['name','email','phone','info','gender','image']
    success_url=reverse_lazy('home')


class ContactDeleteView(LoginRequiredMixin,DeleteView):
    model=Contact
    template_name='delete.html'
    success_url=reverse_lazy('home')

class SignupForm(CreateView):
    form_class=UserCreationForm
    template_name='registration/signup.html'
    success_url=reverse_lazy('login')



