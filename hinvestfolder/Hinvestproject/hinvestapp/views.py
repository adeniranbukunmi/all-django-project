from django.shortcuts import render,redirect
from .models import students

# Create your views here.

def index(request):
    data=students.objects.all()
    print(data)
    content={"data":data}
    return render(request, "index.html" , content)

def insertdata(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        print(name, email, age, gender)
        query=students(name=name, email=email, age=age, gender=gender)
        query.save()
        return redirect("/")
    return render(request, "index.html")

def update(request, id):
# remove all the dot get
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        age=request.POST['age']
        gender=request.POST['gender']
        edit=students.objects.get(id=id)
        edit.name=name
        edit.email=email
        edit.age=age
        edit.gender=gender
        edit.save()
        return redirect("/")
    
    d=students.objects.get(id=id)
    content={"d":d}
    return render(request, "edit.html" , content)

def delete(request, id):
    d=students.objects.get(id=id)
    d.delete()
    return redirect("/")
    
   
