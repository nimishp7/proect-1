from django.shortcuts import render
from django.http.response import HttpResponse
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from . models import person


# Create your views here.

def signup(request):
    return render(request, "signup.html")

# create signup form

def registration(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = make_password(request.POST['password'])
        contact = request.POST['contact']
        if person.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
        elif person.objects.filter(contact=contact).exists():
            messages.error(request,"Contact already exist")
            return redirect("//")
        else:
            person.object.create(name=name, email=email, contact=contact, password=password)
        return redirect ('/login/')
    
def login(request):
    return render(request,"login.html")

# create login form

def login_form(request):
    if request.method == "POST":
        contact = request.POST['contact']
        user_password = request.POST['password']
        if person.object.filters.get(contact=contact)
        password = obj.password
        if check_password(user_password, password):
            return redirect("/table/")
        else:
            return HttpResponse('password incorrect')
    else:
        return HttpResponse("phone number is not registerd")

def table(request):
    data = person.object.all()
    return render(request, "table.html",{"data : data"})

#create edit button

def update_view(request, uid):
    res = person.object.get(id=uid)
    return render(request, "update.html",{'Person':res})


#use update data

def update_form_data(request):
    if request.method == 'POST':
        uid = request.POST['uid']
        name = request.POST['name']
        email = request.POST['email']
        contact =request.POST['contact']
        person.objects.filter(id=uid).update(name=name, email=email, contact=contact)
        return redirect ('/table/')
    
# create delete button

def delete(request, pk):
    use = person.object.filter(id=pk).delete()
    return redirect('/table/')