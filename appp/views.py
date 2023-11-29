from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login ,logout
# from django.contrib.auth.models import User
from appp.models import User , Studentdata
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required

# Form save and email sending
import pdfkit
from django.template.loader import render_to_string
from django.contrib import messages

from django.conf import settings
from django.core.mail import EmailMessage , send_mail




# # Create your views here.


# # 1st interface def=======================================================>>>>>>>>>>>>>

def portt(requst):
    return render(requst,"interface.html")

# # signup def========================================================>>>>>>>>>>>>

def signup(request):
    return render(request,"auth/signup.html")


# login def===========================================================>>>>>>>>>>>>>

def loginn(request):
    return render(request, "auth/login.html")

# after signup=======================================================>>>>>>>>>>>>>>

def savedata(request):
    if request.method == "POST":
        
        Username = request.POST.get("username")
        Email = request.POST.get("email")
        Fname = request.POST.get("fname")
        Lname = request.POST.get("lname")
        Password = request.POST.get("password")

        userinfo = User(username = Username,email = Email,first_name =Fname,last_name = Lname ,password = make_password(Password))
        userinfo.save()

        # print(f"{Username}xxxxxxx")

        return redirect("loginn")
    

# # after login=============================================================>>>>>>>>>>>>>>>>>>>>

def loggedin(request):
    if request.method == "POST":
        Email = request.POST.get("email")
        Password = request.POST.get("password")

        check = authenticate(email = Email, password = Password)

        # print(f"{Email},{Password}")

        # print(check, "xxxxxxxxxxxx")

        if check is not None:    
            # print("heloooooooooooooooooooooo")
            login(request, check)
            # return render(request, "basic/2nd.html")
            return redirect("formm")


    return render(request, "auth/login.html")


# logout================================================>>>>>>>>>>>>>>>>>>>>>>>

def logoutt(request):
    logout(request)
    return redirect("loginn")


# admission form========================================================>>>>>>>>>>>>>>>
@login_required(login_url="/loginn")
def formm(request):
    return render(request, "basic/form.html")


# # students data saved====================================================>>>>>>>>>>>>>

def save_and_email(request):
    if request.method == 'POST':
        # Extract data from the request
        Datee = request.POST.get("date")
        Nname = request.POST.get("name")
        Fathername = request.POST.get("fname")
        Collegee = request.POST.get("college")
        Phoneno = request.POST.get("phone")
        Altphno = request.POST.get("altphno")
        Eemail = request.POST.get("email")
        Amtpaid = request.POST.get("paid")
        Modofpymt = request.POST.get("modeofpayment")
        Balance = request.POST.get("balance")
        Coursetype = request.POST.get("coursetype")
        Course = request.POST.get("courses")
        Addtnlslc = request.POST.get("addtnlslc")

        
        instance = Studentdata.objects.create(
            Date=Datee,
            Name=Nname,
            Father_name=Fathername,
            College=Collegee,
            Phone=Phoneno,
            Alternate_phone=Altphno,
            Email=Eemail,
            Paid_Amount=Amtpaid,
            Mode_of_payment=Modofpymt,
            Balance_amount=Balance,
            Type_of_course=Coursetype,
            Cources_name=Course,
            additional_course=Addtnlslc
        )

        # Generate HTML content from the template
        html_content = render_to_string('basic/email_template.html', {'user': instance})

        # Get the path to wkhtmltopdf executable
        wkhtmltopdf_path = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'

        # Generate PDF from HTML with explicit path to wkhtmltopdf
        pdf_file = pdfkit.from_string(html_content, False, configuration=pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path))

        # Attach PDF to the email
        subject = 'Student Registration Details'
        message = 'Please find the attached receipt for your student registration.'
        from_email = 'your@example.com'
        to_email = Eemail 

        email = EmailMessage(subject, message, from_email, [to_email])
        email.attach('Receipt.pdf', pdf_file, 'application/pdf')

        
        email.send()

        messages.success(request, 'Registration successful. Receipt sent to your email.')
        return redirect('showdata')


    return redirect('formm')

    


# showdata of registered students
@login_required(login_url="/loginn")
def showdata(request):
    data = Studentdata.objects.all()
    return render(request, "basic/showdata.html", {"data" : data})







# show payment page of registered students for updation
@login_required(login_url="/loginn")
def showupdate(request):
    data = Studentdata.objects.all()
    return render(request, "basic/showpayment.html", {"data" : data})




# update Payments of students================================>>>>>>>>>>>
@login_required(login_url="/loginn")
def updatepymts(request, x):
    data = Studentdata.objects.get(id = x)
    return render(request, "basic/paymentform.html", {"data" : data})

## edit and update Pyments of students==========================>>>>>
@login_required(login_url="/loginn")
def pymtupdate(request , x):
    x = Studentdata.objects.get(id = x)
    if request.method == "POST":
        Datee = request.POST.get("date")
        Nname = request.POST.get("name")
        Amtpaid = request.POST.get("paid")
        Modofpymt = request.POST.get("modeofpayment")
        Balance = request.POST.get("balance")
        
        x.Date = Datee
        x.Name =  Nname
        x.Paid_Amount = Amtpaid
        x.Mode_of_payment = Modofpymt
        x.Balance_amount = Balance

        x.save()

        return redirect("showupdate")
    return redirect("showupdate")



# download===============================================================>>>>>>>>>>>>>>

def downloadd(request):
    data = Studentdata.objects.all()
    return render(request, "basic/download.html", {"data" : data})















# show course page of registered students for updation
@login_required(login_url="/loginn")
def showcourse(request):
    data = Studentdata.objects.all()
    return render(request, "basic/showcourse.html", {"data" : data})

# update Course of students================================>>>>>>>>>>>
@login_required(login_url="/loginn")
def updatecourse(request, x):
    data = Studentdata.objects.get(id = x)
    return render(request, "basic/courseform.html", {"data" : data})


# edit and update Course of students==========================>>>>>
@login_required(login_url="/loginn")
def courseupdate(request , x):
    x = Studentdata.objects.get(id = x)
    if request.method == "POST":
        Datee = request.POST.get("date")
        Nname = request.POST.get("name")
        Coursetypee = request.POST.get("coursetype")
        Coursee = request.POST.get("courses")
        Addtnlslcc = request.POST.get("addtnlslc")
        
        x.Date = Datee
        x.Name =  Nname
        x.Type_of_course = Coursetypee
        x.Cources_name = Coursee
        x.additional_course = Addtnlslcc

        x.save()

        return redirect("showcourse")
    return redirect("showcourse")







def sending(request):
    print(settings.EMAIL_HOST_USER)

    mail = EmailMessage('tunak tunak da da da', 'this is discription', settings.EMAIL_HOST_USER, ["prajapatisahil022@gmail.com"])
    mail.send()
    return HttpResponse("Sent")




