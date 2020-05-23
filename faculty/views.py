from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage

from .forms import AssignmentForm, NoticeForm
from .models import Notice, Assignment

def index(request) :
    if request.method == 'POST' :
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        filename = fs.save(uploaded_file.name, uploaded_file)
    return render(request, 'faculty/index.html', {})

def notice(request) :
    notices = Notice.objects.all()
    context = {
        'notices' : notices
    }
    return render(request, 'faculty/notice.html', context = context)

def notice_new(request) :
    if request.method == 'POST' :
        form = NoticeForm(request.POST)
        if form.is_valid() :
            form.save();
            return redirect('notice')
    else :
        form = NoticeForm()
    return render(request, 'faculty/new_notice.html', {'form' : form})

def assignment(request) :
    assignments = Assignment.objects.all()
    context = {
        'assignments' : assignments
    }
    return render(request, 'faculty/assignment.html', context = context)

def assignment_new(request) :
    if request.method == 'POST' :
        form = AssignmentForm(request.POST, request.FILES)
        if form.is_valid() :
            form.save()
            return redirect('assignment')
    else :
        form = AssignmentForm()
    return render(request, 'faculty/new_assignment.html', {'form' : form}) 
