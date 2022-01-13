from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Messages


# Create your views here.

def index(request):
    context = {}
    if request.method =='POST' :
        try:
            Messages.objects.create(
                name = request.POST['name'],
                email = request.POST['email'],
                subject = request.POST['subject'],
                message = request.POST['message']
            )
            messages.success(request, "thanks " + request.POST['name'] + "  , message sent successfully")
        except:
            messages.error(request, f"sorry {request.POST['name']}, internal server error please try again")
        print(messages)
        return redirect('/#contact')
    return render(request, 'blog/index.html', context)
