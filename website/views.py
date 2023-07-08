# an connector that connect url to user requests
from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseRedirect
from django.http import JsonResponse
from website.models import Contact
from website.forms import NameForm,ContactForm
from django.contrib import messages
def index_view(request):
    return  render (request ,'website/index.html')
def about_view(request):
    return  render (request ,'website/about.html')

# Contact.objects.update(name='unknown')
def contact_view(request):
    form = ContactForm(request.POST)
    if request.method == 'POST' : 
        form = ContactForm(request.POST)
        if form.is_valid():
           form.save()
           messages.add_message(request,messages.SUCCESS,'*****************************         Your ticket submitted successfully     *****************************')
        else:
            messages.add_message(request,messages.ERROR,'******************************        Your ticket did not submitted     *************************')
    form = ContactForm()
    return render(request,'website/contact.html',{'form': form})
        

def test(request):   
    if request.method == 'POST' :
        form = ContactForm(request.POST)
        if form.is_valid():
           form.save()
           return HttpResponse('Done')
        else:
            return HttpResponse('Not valid')
    form = ContactForm()
    return render(request,'shop.html',{'form': form})
# Create your views here.
