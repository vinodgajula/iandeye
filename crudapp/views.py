from django.shortcuts import render,redirect
from  .models import UserDetails
def homePageView(request):
    return render(request,'home.html')

def create(request):
    print("create method got triggered.")
    if request.method=="POST":
        print("This is post HTML call.")
        return render(request,'about.html')

def signUpDashBoard(request):
    return render(request, 'signup-board.html')

def adminSignUpDashBoard(request):
    return render(request, 'admin-signup-board.html')

def loginDashBoard(request):
    return render(request, 'login-board.html')

def adminLoginDashBoard(request):
    return render(request, 'admin-login-board.html')

def insertUser(request):
    #print("Vinod", request.POST)
    #print(request.POST["availableResources"])
    data = {k: v for k, v in request.POST.items()}
    data.pop('csrfmiddlewaretoken')
    print(data)
    if data["password"] == data["conformPassword"]:
        data.pop("conformPassword")
        user = UserDetails(**data)
        user.save()
        return render(request,'signup.html', {"firstName": data["firstName"]})
    else:
        return render(request,'password-input-error.html')

def selectUser(request):
    #print("Vinod", request.POST)
    data = {k: v for k, v in request.POST.items()}
    data.pop('csrfmiddlewaretoken')
    print(data)
    user = UserDetails.objects.filter(email = data["email"], password = data["password"])
    #user = UserDetails.objects.filter()
    print("Select query: ", user, type(user))
    #user = dict(user)
    for row in user:
        print(row.firstName)
        return render(request,'login.html', {"firstName": row.firstName})
    return render(request,'login-error.html')

def viewUsers(request):
    users = UserDetails.objects.filter()
    if users:
        return render(request,'view-users.html', {"users": users})
    return render(request,'login-error.html')

