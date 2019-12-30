from django.shortcuts import render,redirect
from .forms import StudentForm
from .models import Student
def index(request):
    students=Student.objects.all()
    return render(request,'index.html',{'students':students})

def updateStudent(request,id):
    st=Student.objects.get(pk=id)
    form =StudentForm(instance=st)
    if request.method=='POST':
        form = StudentForm(request.POST,instance=st)
        if form.is_valid():
            form.save()
            return redirect('home')
    # return render(request,'s')
    render(request,'student_form.html')





def createStudent(request):
    form=StudentForm()
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'student_form.html',{'form':form})
