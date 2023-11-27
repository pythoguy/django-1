from django.urls import path
from appp import views



def conditional_view(request):
    if request.user.is_authenticated:
        return views.formm(request)
    else:
        return views.portt(request)

urlpatterns = [

    path("", conditional_view, name="conditional_view"),

    # home
    path("home",views.portt,name="home"),


    # signup
    path("signup",views.signup,name="signup"),

    # data saved after signup
    path("savedata",views.savedata),

    # login
    path("loginn",views.loginn,name="loginn"),

    # logged in def
    path("loggedin",views.loggedin),

    # logout
    path("logoutt",views.logoutt),

    # admission form
    path("formm",views.formm,name="formm"),

    # student data saved
    path("datasaved",views.datasaved),

    # show data of registered students
    path("showdata", views.showdata, name="showdata"),
    
    
    # download data of registered students
    path("downloadd", views.downloadd, name="downloadd"),










    
    # show payments of registered students for update
    path("showupdate", views.showupdate, name="showupdate"),
    

    # update Pyments of students template
    path("updatepymts/<int:x>", views.updatepymts , name="updatepymts"),
    
    # updated Pyments of students link
    path("pymtupdate/<int:x>", views.pymtupdate , name="pymtupdate"),
    







    
    # show courses of registered students for update
    path("showcourse", views.showcourse, name="showcourse"),
    
    # update courses of registered students template
    path("updatecourse/<int:x>", views.updatecourse, name="updatecourse"),


    # updated Pyments of students link
    path("courseupdate/<int:x>", views.courseupdate , name="courseupdate"),



    

#     # delete data in student
#     path("delete/<int:x>", views.detethis),
]
