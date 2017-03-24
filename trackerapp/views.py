from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect, HttpResponse
from django.core.context_processors import csrf
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.hashers import check_password, make_password
from models import UserExtend
import datetime
import ftplib
import time
import os
import json
import pygmaps

# Create your views here.
def home(request):
    context = {}
    if request.user.is_authenticated():
        path="/tmp/download"
        filename = "file"
        dict = UserExtend.objects.filter(username=request.user).values()[0]
        if dict.get('emi') != "":
            filename = dict.get('emi')
        complete_path = os.path.join(path,filename)
        ftp=ftplib.FTP('ftp.diaskills.co')
        ftp.login("anil123456","Kiet12345")
        ftp.cwd('/')
        try:
            ftp.retrbinary('RETR ' + filename,open('/tmp/download/' + filename,'wb').write)
            file_pointer = open(complete_path,"rb")
            list = []
            last=[]
            fp = file_pointer.readline()
            while fp != "":
                list.append(fp)
                fp = file_pointer.readline()

            last = list[-3].strip().split('/')
            speed = int(last[3])
            latitude = float(last[4])
            longitude = float(last[5])
            context.update({'speedometer': speed,'latitude': latitude,'longitude': longitude})
        except:
            time.sleep(0.50)
        # ftp.cwd('/home/FTP-shared/download')
        # ftp.quit()
        # os.remove(complete_path)
        if request.method == "POST":
            response_data= {'speed' : speed,'latitude': latitude,'longitude': longitude}
            return HttpResponse(json.dumps(response_data), content_type="application/json")
    return render(request, "home.html", context)

def register(request):
    context = {}
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        if request.method == "POST":
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            confirm_password = request.POST['confirm_password']
            if User.objects.filter(username=username).count() == 0:
                password = make_password(password, salt=None, hasher='default')
                user = User(username=username, email=email, password=password, is_active=False)
                user.save()
                userextend = UserExtend(username=username)
                userextend.save()
                return HttpResponseRedirect('/')
            else:
                context.update({"error":"Username already exist"})
    return render(request, "registration/register.html", context)

def login(request):
    context = {}
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        context.update(csrf(request))
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                active_user = User.objects.filter(username=username).values()[0].get('is_active')
                if active_user == True:
                    auth.login(request, user)
                    if user.is_superuser:
                        list = UserExtend.objects.filter(username=request.user).values()
                        if len(list) == 0:
                            userextend = UserExtend(username=request.user)
                            userextend.save()
                    return HttpResponseRedirect('/')
                else:
                    context.update({"error" : "Activate your account."})
            else:
                context.update({"error" : "Either username or password is wrong."})
    return render(request, "registration/login.html", context)

def logout(request):
    if request.user.is_authenticated():
        auth.logout(request)
    return HttpResponseRedirect('/')

def change_password(request):
    context = {}
    if request.user.is_authenticated():
        if request.method == "POST":
            current_password = request.POST['current_password']
            new_password = request.POST['new_password']
            confirm_password = request.POST['confirm_password']
            hash_password = User.objects.filter(username=request.user).values()[0].get('password')
            if check_password(current_password, hash_password):
                if new_password == confirm_password:
                    user = User.objects.get(username__exact=request.user)
                    user.set_password(new_password)
                    user.save()
                    return HttpResponseRedirect('/')
            else:
                context.update({"error": "You typed wrong password."})
    else:
        return HttpResponseRedirect('/')
    return render(request, "registration/change_password.html",context)

def profile(request):
    context = {}
    context.update({"selected":"selected"})
    if request.user.is_authenticated():
        email = User.objects.filter(username=request.user).values()[0].get('email')
        firstname = User.objects.filter(username=request.user).values()[0].get('first_name')
        lastname = User.objects.filter(username=request.user).values()[0].get('last_name')
        dob = UserExtend.objects.filter(username=request.user).values()[0].get('dob')
        gender = UserExtend.objects.filter(username=request.user).values()[0].get('gender')
        if dob != None:
            day = '{:02d}'.format(dob.day)
            month = '{:02d}'.format(dob.month)
            year = '{:04d}'.format(dob.year)
        else:
            day = '{:02d}'.format(1)
            month = '{:02d}'.format(1)
            year = '{:04d}'.format(1900)
        context.update({"email":email,"firstname":firstname,"lastname":lastname,"dob":{"day":day,"month":month,"year":year},"gender":gender})
        if request.method == "POST":
            email = request.POST['email']
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            dob = request.POST['dob']
            gender = request.POST['gender']
            user = User.objects.get(username__exact=request.user)
            user.email = email
            user.first_name = firstname
            user.last_name = lastname
            user.save()
            userextend = UserExtend.objects.get(username__exact=request.user)
            userextend.dob = dob
            userextend.gender = gender
            userextend.save()
            return HttpResponseRedirect('/profile/')
    else:
        return HttpResponseRedirect('/')
    return render(request, "registration/profile.html",context)

def contact(request):
    context = {}
    if request.method == 'POST':
        subject = "Customer queries"
        from_email = "ankit.malhotra00@gmail.com"
        to_email = "ankit.1310027@kiet.edu"
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        body = "Name: "+name+"\n"+"From: "+email+"\n"+"Meassage: "+message
        print body
        send_mail(subject,body,from_email,[to_email],fail_silently=True)
    return render(request,'home.html',context)

def activation(request):
    context = {}
    if request.method == "POST":
        username = request.POST.getlist('username')
        emi = request.POST.getlist('emi')
        sub = request.POST.getlist('sub')
        length = len(username)
        i=0
        while i < length:
            userextend = UserExtend.objects.get(username__exact=username[i])
            userextend.emi = emi[i]
            userextend.subscription = sub[i]
            userextend.subscription_date = datetime.date.today()
            userextend.save()
            user = User.objects.get(username__exact=username[i])
            user.is_active = True
            user.save()
            i=i+1
        return HttpResponseRedirect('/activation/')
    else:
        inactive_users = []
        lists = User.objects.filter(is_active=False).values()
        i=0
        for list in lists:
            i = i+1
            inactive_users.append({"username":list.get('username'),"s_no":str(i)})
        context.update({"inactive_users":inactive_users})
    return render(request,'activation.html',context)

def individual_activation(request):
    context = {}
    if request.method == "POST":
        pass
        username = request.POST['username']
        emi = request.POST['emi']
        sub = request.POST['sub']
        userextend = UserExtend.objects.get(username__exact=username)
        userextend.emi = emi
        userextend.subscription = sub
        userextend.subscription_date = datetime.date.today()
        userextend.save()
        user = User.objects.get(username__exact=username)
        user.is_active = True
        user.save()
    return HttpResponseRedirect('/activation/')
