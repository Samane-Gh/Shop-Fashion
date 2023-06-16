# an connector that connect url to user requests
from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseRedirect
from django.http import JsonResponse
from website.models import Contact
from website.forms import NameForm,ContactForm,NewsletterForm
from django.contrib import messages
def index_view(request):
    return  render (request ,'website/index.html')
def about_view(request):
    return  render (request ,'website/about.html')

Contact.objects.update(name='unknown')
def contact_view(request):
    
    
    form = ContactForm(request.POST)
    if request.method == 'POST' :
        
        form = ContactForm(request.POST)
        form.save()
        if form.is_valid():
           
           messages.add_message(request,messages.SUCCESS,'*********    Your ticket submitted successfully   ***********')
        else:
            messages.add_message(request,messages.ERROR,'***********  Your ticket didnt submited     ***********')
     
        
    form = ContactForm()
    return render(request,'website/contact.html',{'form': form})
    
    
def newsletter_view(request):
    if request.method == 'POST':
        form =NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
    

def test(request):   
    if request.method == 'POST' :
        form = ContactForm(request.POST)
        if form.is_valid():
           form.save()
           return HttpResponse('Done')
        else:
            return HttpResponse('Not valid')
    form = ContactForm()
    return render(request,'test.html',{'form': form})
# Create your views here.
