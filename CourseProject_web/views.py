from django.shortcuts import redirect, render

from projects.models import Project

from django.contrib.auth.decorators import login_required

from documents.forms import DocumentForm

from documents.models import Document

from stages.models import Stage

from django.shortcuts import get_object_or_404

@login_required
def supervisor_project(request, project_id):

    project = get_object_or_404(Project, id=project_id)

    if request.user != project.supervisor:
        return redirect('index')

    if request.method == 'POST':
        new_status = request.POST.get('status')
        project.status = new_status
        project.save()

    documents = Document.objects.filter(project=project)
    stages = Stage.objects.filter(project=project)

    return render(request, 'supervisor/project.html', {
        'project': project,
        'documents': documents,
        'stages': stages,
    })

@login_required
def supervisor_dashboard(request):

    if request.user.role != 'supervisor':
        return redirect('index')

    projects = Project.objects.filter(supervisor=request.user)

    return render(request, 'supervisor/dashboard.html', {
        'projects': projects
    })

@login_required
def documents_list(request):
    project = Project.objects.filter(student=request.user).first()

    if not project:
        return render(request, 'student/no_project.html')

    documents = Document.objects.filter(project=project)
    stages = Stage.objects.filter(project=project)

    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            doc = form.save(commit=False)
            doc.project = project
            doc.uploaded_by = request.user
            doc.save()
            return redirect('documents')
    else:
        form = DocumentForm()

    return render(request, 'student/documents.html', {
        'documents': documents,
        'form': form,
        'stages': stages,
    })

@login_required
def documents_page(request):

    project = Project.objects.first()

    return render(
        request,
        'student/documents.html',
        {
            'project': project
        }
    )


@login_required
def stages_page(request):

    project = Project.objects.first()

    return render(
        request,
        'student/stages.html',
        {
            'project': project
        }
    )

@login_required
def documents_page(request):
    project = request.user.project
    return render(request, 'student/documents.html', {'project': project})

@login_required
def upload_document(request):
    project = request.user.project

    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)

        if form.is_valid():
            doc = form.save(commit=False)
            doc.project = project
            doc.uploaded_by = request.user
            doc.save()

    else:
        form = DocumentForm()

    return render(request, 'student/upload.html', {'form': form})

def index(request):
    return render(request, 'index.html')


@login_required
def student_dashboard(request):

    project = Project.objects.filter(student=request.user).first()

    if not project:
        return render(request, 'student/no_project.html')

    stages = project.stages.all()

    if stages.exists():
        completed = stages.filter(status='approved').count()
        total = stages.count()
        progress = int((completed / total) * 100)
    else:
        progress = 0

    return render(
        request,
        'student/dashboard.html',
        {
            'project': project,
            'progress': progress,  # 🔥 ВОТ ЭТОГО НЕ ХВАТАЛО
        }
    )


def supervisor_dashboard(request):

    projects = Project.objects.all()

    return render(
        request,
        'supervisor/dashboard.html',
        {
            'projects': projects,
        }
    )

def my_project(request):
    project = request.user.project

    stages = project.stages.all()

    total = stages.count()
    done = stages.filter(status='approved').count()

    progress = 0
    if total > 0:
        progress = int((done / total) * 100)

    return render(request, 'student/project.html', {
        'project': project,
        'stages': stages,
        'progress': progress,
    })