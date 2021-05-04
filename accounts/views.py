from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth


# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid details')
            return redirect('login')
    else:
        return render(request, "login.html")


def register(request):
    if request.method == "POST":
        user_name=request.POST['user_name']
        password1= request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1 == password2:
            if User.objects.filter(username=user_name).exists():
                messages.info(request, 'Username already taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=user_name, password=password1, email=email)
                user.save;
                print("user created")
        else:
            print("Password not matched")
        return redirect('/')
    else:
        return render(request, 'registration.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

def Enquiry(request):
    if request.method == "POST":
        Student_name= request.POST['Student_name']
        Course_name=request.POST['Course_name']
        Contact_number= request.POST['contact_number']
        Enquiry_date=request.POST['Enquiry_date']
        user = auth.authenticate(Student_name=Student_name,Course_name=Course_name, Contact_number=Contact_number,Enquiry_date=Enquiry_date)
        if user is not None:
            auth.Enquiry(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid details')
            return redirect('Enquiry')
    else:
        return render(request, "Enquiry.html")

