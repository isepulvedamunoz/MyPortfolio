from django.shortcuts import render
from .models import Personal_info, Profesional_info, educ_info, Projects


def index(request):
    personal = Personal_info.objects.all()
    info = Profesional_info.objects.all()
    educ = educ_info.objects.all()
    project = Projects.objects.all()

    context = {
        'personal': personal,
        'info': info,
        'educ': educ,
        'project': project

    }


    return render(request, 'app_main_page/front_page.html', context)
