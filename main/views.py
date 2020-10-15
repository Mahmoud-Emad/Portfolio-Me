from django.views.generic import ListView
from .models import TestMe,ProjectsModel,Comments
from main.forms import TestmeForm,CommentsForm,ContactForm
from django.shortcuts import render, redirect



# Create your views here.

def Project(request):
    allin = ProjectsModel.objects.all()
    form_contact = ContactForm
    if request.method =='POST':
        form_contact = form_contact(request.POST)
        if form_contact.is_valid():
            form_contact.save()
            return redirect ('home')
        else:
            form_contact.errors
    else:
        form_contact = ContactForm
    context = {'allin':allin,'form_contact':form_contact}
    return render (request,"projects.html",context)


def Project_Ditail(request,slug):
    allin = ProjectsModel.objects.get(slug=slug)
    context = {'allin':allin}
    return render (request,"Project_Cetail.html",context)

def main(request):
    commentat = Comments.objects.all()
    allin = ProjectsModel.objects.all()
    form = TestmeForm
    if request.method =='POST':
        form = TestmeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('thanks')
        else:
            form.errors
    else:
        form = TestmeForm
    form_comment = CommentsForm
    if request.method =='POST':
        form_comment = CommentsForm(request.POST)
        if form_comment.is_valid():
            form_comment.save()
            return redirect ('home')
        else:
            form_comment.errors
    else:
        form_comment = CommentsForm
    form_contact = ContactForm
    if request.method =='POST':
        form_contact = form_contact(request.POST)
        if form_contact.is_valid():
            form_contact.save()
            return redirect ('home')
        else:
            form_contact.errors
    else:
        form_contact = ContactForm
    context = {
        'commentat':commentat,
        'form_comment':form_comment,
        'form':form,
        'form_contact':form_contact,
        'allin':allin

    }
    return render(request,"main.html",context)


def Aboutme(request):
    form_contact = ContactForm
    if request.method =='POST':
        form_contact = form_contact(request.POST)
        if form_contact.is_valid():
            form_contact.save()
            return redirect ('home')
        else:
            form_contact.errors
    else:
        form_contact = ContactForm
    context = {'form_contact':form_contact,}
    return render (request,"about-me.html",context)


def Service(request):
    form_contact = ContactForm
    if request.method =='POST':
        form_contact = form_contact(request.POST)
        if form_contact.is_valid():
            form_contact.save()
            return redirect ('home')
        else:
            form_contact.errors
    else:
        form_contact = ContactForm
    context = {'form_contact':form_contact,}
    return render (request,"Service.html",context)



def Thanks(request):
    form = TestmeForm
    if request.method =='POST':
        form = TestmeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('thanks')
        else:
            form.errors
    else:
        form = TestmeForm
    form_contact = ContactForm
    if request.method =='POST':
        form_contact = form_contact(request.POST)
        if form_contact.is_valid():
            form_contact.save()
            return redirect ('home')
        else:
            form_contact.errors
    else:
        form_contact = ContactForm
    context = {'form':form,'form_contact':form_contact,}
    return render (request,"thanks.html",context)






    
def TestMeViwe(request):
    form = TestmeForm
    if request.method =='POST':
        form = TestmeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('thanks')
        else:
            form.errors
    else:
        form = TestmeForm
    form_contact = ContactForm
    if request.method =='POST':
        form_contact = form_contact(request.POST)
        if form_contact.is_valid():
            form_contact.save()
            return redirect ('home')
        else:
            form_contact.errors
    else:
        form_contact = ContactForm
    context = {
        'form_contact':form_contact,
        'form':form
    }
    return render(request,"testme.html",context)

    