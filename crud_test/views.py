from django.shortcuts import render, redirect
from main .models import StudentModel

def home(request):
    if request.method == 'POST':
        nm = request.POST.get('name')
        em = request.POST.get('email')
        cs = request.POST.get('course')
        record = StudentModel(name=nm, email=em, course=cs)
        record.save()

    data = StudentModel.objects.all()
    return render(request, 'index.html', {'data':data})

def delete(request, id):
    data = StudentModel.objects.get(pk=id)
    data.delete()
    return redirect('/')

def update(request, id):
    data = StudentModel.objects.get(id = id)
    if request.method == 'POST':
        nm = request.POST.get('name')
        em = request.POST.get('email')
        cs = request.POST.get('course')
        da = request.POST.get('date')
        record = StudentModel(id=id, name=nm, email=em, course=cs, date=da)
        record.save()
        data = {}
    
    
    return render(request, 'update.html', {'data':data})