from django.shortcuts import render,HttpResponse
from .models import Student
from django.views import View,generic

# Other view:
'''class StudentView(View):
    def get(self,request):
        records = Student.objects.all()
        return render(request,"myapp/data.html",{"data":records})'''

# Generic Detail View:
'''class StudentView(generic.DetailView):
    model = Student
    template_name = "myapp/data.html" '''

# ListView:
class StudentView(generic.ListView):
    template_name = "myapp/data.html"
    context_object_name = "details"

    def get_queryset(self):
        students = Student.objects.order_by("marks")
        return students


# Home View:
def home(request):
    return render(request,"myapp/home.html",{})

# Insertion:
def insert_data(request):
    if request.method == "POST":
        s = Student(roll = request.POST.get("roll"),name = request.POST.get("name"),marks = request.POST.get("marks"))
        s.save()
        return HttpResponse("Data inserted!")

# Updation:
def update_data(request):
    if request.method == "POST":
        s = Student(roll = request.POST.get("roll"))
        s.name = request.POST.get("name")
        s.marks = request.POST.get("marks")
        s.save()
        return HttpResponse("Data Updated!")

# Deletion:
def delete_data(request):
    if request.method == "POST":
        s = Student.objects.filter(roll = request.POST.get("roll")).first()
        s.delete()
        return HttpResponse("Data Deleted!")

# Display particular:
def display_data(request):
    if request.method == "POST":
        s = Student.objects.filter(roll = request.POST.get("roll")).first()
        return HttpResponse(f"Roll : {s.roll}<br>Name: {s.name}<br>Marks: {s.marks}")

# Display all:
def fetch_all(request):
    if request.method == "GET":
        content = Student.objects.all()
        return render(request,"myapp/index.html",{"details":content})


