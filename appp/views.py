from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login ,logout
# from django.contrib.auth.models import User
from appp.models import User , Studentdata
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required



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

def datasaved(request):
    if request.method == "POST":
        
        Datee = request.POST.get("date")
        Nname = request.POST.get("name")
        Fathername = request.POST.get("fname")
        Collegee = request.POST.get("college")
        Phoneno = request.POST.get("phone")
        Altphno = request.POST.get("altphno")
        Amtpaid = request.POST.get("paid")
        Modofpymt = request.POST.get("modeofpayment")
        Balance = request.POST.get("balance")
        Coursetype = request.POST.get("coursetype")
        Course = request.POST.get("courses")
        Addtnlslc = request.POST.get("addtnlslc")

        studata = Studentdata(Date = Datee, Name =  Nname, Father_name = Fathername, College = Collegee, Phone = Phoneno, Alternate_phone = Altphno, Paid_Amount = Amtpaid,Mode_of_payment = Modofpymt, Balance_amount = Balance, Type_of_course = Coursetype, Cources_name = Course, additional_course = Addtnlslc)       
        studata.save()

        # print(f"{Fname}xxxxxxx")

        return redirect("showdata")
    


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





