from django.shortcuts import render
from.models import Contact
import requests, json
# Create your views here.

def index(request):
    if request.method == 'POST':
        first_name_= request.POST.get('first_name')
        last_name_ = request.POST.get('last_name')


        r=requests.get('http://api.icndb.com/jokes/random?firstName=' + first_name_ +' &lastName= '+ last_name_)
        json_data = json.loads(r.text)
        joke = json_data.get('value').get('joke')
        context={'joke': joke, 'name': first_name_ + " " + last_name_}
        return render(request, 'mysite/index.html',context)
    else:
        first_name_ = 'Tawanda'
        last_name_ = 'Nyahuye'

        r = requests.get('http://api.icndb.com/jokes/random?firstName=' + first_name_ + ' &lastName= ' + last_name_)
        json_data = json.loads(r.text)
        joke = json_data.get('value').get('joke')
        context={'joke': joke, 'name': first_name_ + " " + last_name_}
        return render(request, 'mysite/index.html', context)

def contact(request):
    if request.method == 'POST':
        email_ = request.POST.get('email')
        subject_ = request.POST.get('subject')
        message_ = request.POST.get('message')

        c = Contact(email=email_, subject=subject_, message=message_)
        c.save()

        context={'feedback':"Cheers buddie i will get back to you!"}
        return render(request, 'mysite/contact.html',context)
    else:
        return render(request, 'mysite/contact.html')

def portfolio(request):
    return render(request, 'mysite/portfolio.html')
