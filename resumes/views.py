from django.shortcuts import render,redirect,get_object_or_404
from .models import Resume
from .form import ResumeForm

# Create your views here.
def index(req):
    if req.method == "POST":
        form = ResumeForm(req.POST)

        if form.is_valid():
            form.save()
            redirect("resumes:index")
        else:
            render(req, "resumes/new.html", {"form":form})

    resumes = Resume.objects.all()
    return render(req, "resumes/index.html", {"resumes":resumes})

def new(req):
    form = ResumeForm()
    return render(req, "resumes/new.html", {"form":form})

def show(req, id):
    resume = get_object_or_404(Resume, pk=id)

    if req.method == "POST":
        form = ResumeForm(req.POST, instance=resume)

        if form.is_valid():
            form.save()
            redirect("resumes:show", resume.id)
        else:
            render(req, "resumes/edit.html", {"form":form})

    return render(req, "resumes/show.html", {"resume":resume})

def edit(req, id):
    resume = get_object_or_404(Resume, pk=id)
    form = ResumeForm(instance=resume)
    return render(req, "resumes/edit.html", {"form":form, "resume":resume})

def delete(req, id):
    resume = get_object_or_404(Resume, pk=id)
    resume.delete()
    return redirect("resumes:index")