from django.shortcuts import render
from django.core.mail import send_mail
from .models import Messages


# Create your views here.

def index(request):
    message = "send message"
    context = {
        'message': message
    }
    if request.method =='POST' :
        message = "thanks "+ request.POST['name'] + "  , message sent successfully"
        Messages.objects.create(
            name = request.POST['name'],
            email = request.POST['email'],
            subject = request.POST['subject'],
            message = request.POST['message']
        )
        context['message'] = message
        print(message)
        return render(request, 'blog/blog.html', context)

    print(context['message'])

    return render(request, 'blog/blog.html', context)
