import email
from django.shortcuts import render, HttpResponseRedirect
from . form import StudentRegistration
from . models import userList
# Create your views here.

#This function well add new user in the database
def viewsUser(request):
    if request.method == 'POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = userList(name=nm, email=em,password=pw)
            reg.save()
            fm=StudentRegistration()
    else:
        fm=StudentRegistration()
    stud = userList.objects.all()

    return render(request, 'login/addandshow.html', {'form':fm, 'stu':stud})

#This function well update/edit form the database
def update_data(request, id):
    if request.method == 'POST':
        pi = userList.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save
    else:
        pi = userList.objects.get(pk=id)
        fm=StudentRegistration(instance=pi)
    return render(request, 'login/updatestudent.html', {'form':fm})


#This function well delete the user form the database
def delete_data(request, id):
    if request.method =='POST':
        pi = userList.objects.get(pk=id)
        print(pi)
        pi.delete()
        
    return HttpResponseRedirect('/')
