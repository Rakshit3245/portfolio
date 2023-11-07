from django.shortcuts import render
from .models import Profile
from django.http import HttpResponse



# Create your views here.

def resume(request):
    if request.method=="POST":
        name=request.POST.get("name","")
        phone=request.POST.get("phone","")
        email=request.POST.get("email","")
        degree=request.POST.get("degree","")
        school=request.POST.get("school","")
        university=request.POST.get("university","")
        skill=request.POST.get("skill","")
        about_you=request.POST.get("about_you","")
        previous_work=request.POST.get("previous_work","")

        profile=Profile(name=name, phone=phone, email=email, degree=degree, school=school,
        university=university, skill=skill, about_you=about_you, previous_work=previous_work)
        profile.save()
    return render(request, 'resume.html')

def cv(request,id):
    user_profile=Profile.objects.get(pk=id)
    return render(request, "cv.html", {'user_profile':user_profile})
