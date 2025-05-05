from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.core.mail import EmailMessage
from .models import *
import random
import string


def about(request):
    return render(request,"about.html")
def index(request):
    return render(request,"index.html")
def contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        from_email=request.POST.get('emails')
        to_email="fakeman7556@gmail.com"
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        messagess=f"Name :  {name}\n\nFrom :  {from_email}\n\nSubject :  {subject}\n\nMessage :  {message}"
        print(messages)
        mail=EmailMessage(subject,messagess,from_email,[to_email])
        mail.send()
        messages.success(request, "Thank You for contacting us, we will update you soon")
    return render(request,"contact.html")

def register(request):
    if request.method == "POST":
        try:
            first_name = request.POST.get("fname")
            last_name = request.POST.get("lname")
            gender = request.POST.get("gender")
            dob = request.POST.get("dob")
            email = request.POST.get("email")
            phone_no = request.POST.get("ph_no")
            country = request.POST.get("country")
            state = request.POST.get("state")
            city = request.POST.get("city")
            hobbies = ",".join(request.POST.getlist("hobbies"))
            hobbies_data=hobbies
            avatar = request.FILES.get("avatar")

            stu=Student.objects.create(
                first_name=first_name,
                last_name=last_name,
                gender=gender,
                dob=dob,
                email=email,
                phone_no=phone_no,
                country=country,
                state=state,
                city=city,
                hobbies=hobbies_data,
                avatar=avatar
            )
            stu.save()
            subject="Registered to Scope India"
            message="You are succesfully registered into scope india"
            mail=EmailMessage(subject,message,"fakeman7556@gmail.com",[email])
            mail.send()
            messages.success(request, f"Registration successful! You can now log in.")
        except Exception as e:
            messages.error(request, f"Registration failed! Error: {str(e)}")
            return redirect("/myapp/register")
    return render(request, "register.html")

def login2(request):
    error_message={}
    if request.method == 'POST':
        get_mail = request.POST.get('email')
        user_email = Student.objects.filter(email=get_mail).exists()
        if user_email:
            user_email1 = Student.objects.get(email=get_mail)
            otp_num=''.join(random.choices(string.digits,k=5))
            user_email1.otp = otp_num
            user_email1.save()
            subjects = "Your OTP Code for Registration"
            messages = f"Hello,\n\nYour OTP code is {otp_num}. Please enter this on the verification page.\n\nBest regards,\nSCOPE INDIA"
            from_email = 'fakeman7556@gmail.com'
            msgsend = EmailMessage(subjects, messages, from_email, [get_mail])
            msgsend.send()
            return redirect('/myapp/login3')  
        else:
            error_message = 'Email not found. Please register and try again.'
    return render(request, 'login2.html', {'error': error_message})

def login3(request):
    error_messages={}
    if request.method == 'POST':
        get_otp = request.POST.get('otp')
        get_password = request.POST.get('password')
        if not error_messages: 
            try:
                user_pass = Student.objects.get(otp=get_otp)
                user_pass.password = get_password
                user_pass.save()
                print("get_password") 
                return redirect('/myapp/login')
            except :
                error_messages['otp_error'] = 'Invalid OTP. Please try again.'
                print(error_messages)
    return render(request,"login3.html", {'errors': error_messages})

def forgot(request):
    error_message={}
    if request.method == 'POST':
        get_mail = request.POST.get('email')
        user_email = Student.objects.filter(email=get_mail).exists()
        if user_email:
            user_email1 = Student.objects.get(email=get_mail)
            otp_num=''.join(random.choices(string.digits,k=5))
            user_email1.otp = otp_num
            user_email1.save()
            subjects = "Your OTP Code for Registration"
            messages = f"Hello,\n\nYour OTP code is {otp_num}. Please enter this on the verification page.\n\nBest regards,\nSCOPE INDIA"
            from_email = 'akhilgs2003@gmail.com'
            msgsend = EmailMessage(subjects, messages, from_email, [get_mail])
            msgsend.send()
            return redirect('/myapp/forgot2')  
        else:
            error_message = 'Email not found. Please check and try again.'
    return render(request, 'forgot.html', {'error': error_message})

def forgot2(request):
    error_messages={}
    if request.method == 'POST':
        get_otp = request.POST.get('otp')
        get_password = request.POST.get('password')
        if not error_messages: 
            try:
                user_pass = Student.objects.get(otp=get_otp)
                user_pass.password = get_password
                user_pass.save()
                print("get_password") 
                return redirect('/myapp/login')
            except :
                error_messages['otp_error'] = 'Invalid OTP. Please try again.'
                print(error_messages)
    return render(request,"forgot2.html", {'errors': error_messages})

def login(request):
    error_messages = {}
    if request.method == "POST":
        get_mail = request.POST.get('email')
        get_pass = request.POST.get('password')
        remember_me = request.POST.get('remember_me')
        user_exists = Student.objects.filter(email=get_mail).exists()
        if user_exists:
            try:
                user = Student.objects.get(email=get_mail, password=get_pass) 
                request.session['email'] = user.email 
                response = redirect('/myapp/elements')
                if remember_me:
                    response.set_cookie('email', user.email, max_age=300) 
                else:
                    response.delete_cookie('email') 
                return response
            except Student.DoesNotExist:
                error_messages['pass_error'] = 'Wrong password, Authentication failed!'
        else:
            error_messages['email_error'] = 'Email not found. Please check and try again.'
    email_cookie = request.COOKIES.get('email', '')

    return render(request, "login.html", {'errors': error_messages, 'email': email_cookie})


def elements(request):
    user_email = request.session.get('email')  # Use .get() to avoid KeyError
    if user_email:
        return render(request, 'elements.html', {'user_email': user_email})
    else:
        return HttpResponse("404 Error. Please log in.", status=401)

def profile(request):
    if "email" not in request.session:
        return redirect('/myapp/login') 
    user_email = request.session["email"]  
    try:
        user = Student.objects.get(email=user_email)
    except Student.DoesNotExist:
        return redirect('/myapp/login') 
    if request.method == "POST":
        if "update" in request.POST:
            user.first_name = request.POST.get("first_name", user.first_name)
            user.last_name = request.POST.get("last_name", user.last_name)
            user.gender = request.POST.get("gender", user.gender)
            user.dob = request.POST.get("dob", user.dob)
            user.phone_no = request.POST.get("phone_no", user.phone_no)
            user.country = request.POST.get("country", user.country)
            user.state = request.POST.get("state", user.state)
            user.city = request.POST.get("city", user.city)        
            hobbies = request.POST.getlist("hobbies")  
            user.hobbies = ",".join(hobbies) if hobbies else user.hobbies
            if "avatar" in request.FILES:  
                user.avatar = request.FILES["avatar"]           
            user.save()
            messages.success(request, "Profile updated successfully.")
            return redirect('profile') 
    context = {
        "fname": user.first_name,
        "lname": user.last_name,
        "gender": user.gender,
        "dob": user.dob.strftime("%Y-%m-%d"),
        "email": user.email,
        "avatar": user.avatar.url if user.avatar else "",
        "ph_no": user.phone_no,
        "country": user.country,
        "state": user.state,
        "city": user.city,
        "hobbies": user.hobbies.split(",") if user.hobbies else [],
    }
    return render(request, "profile.html", {"context": context})

def changepassword(request):
    error_messages={}
    user_email=request.session.get('email') 
    if request.method == "POST":
        old_pass=request.POST.get("old_password")
        new_pass=request.POST.get("new_password")      
        try:
            user_pass = Student.objects.get(password=old_pass)
            print(new_pass)
            user_pass.password = new_pass
            user_pass.save()
            request.session['password'] = new_pass
            return redirect('login')
        except :
            error_messages['pass_error'] = 'Invalid Password. Please try again.'
            print("error_messages")
    return render(request,"changepassword.html",{'errors' : error_messages})

def logout(request):
        request.session.flush()
        try:
            response=redirect('/myapp/login')
        except Student.DoesNotExist:
            return redirect('/myapp/login') 
        response.delete_cookie('email') 
        return response


