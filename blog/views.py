from django.shortcuts import render

def home(request):
    data = {
        "title1": "Autor | TeacherCode",
        "title2": "Ingreso de notas"
    }
    return render(request, 'core/home.html', data)

def periodo_list(request):
    data = {
        "title1": "Periodo",
        "title2": "Consulta el periodo"
    }
    return render(request, "core/periodo.html", data)

def asignatura_List(request):
    data = {
        "title1": "Asignaturas",
        "title2": "Consulta de las asignaturas"
    }
    return render(request, "core/asignatura.html", data)

def profesor_List(request):
    data = {
        "title1": "Profesores",
        "title2": "Consulta De profesores"
    }
    return render(request, "core/profesor.html", data)

def estudiante_list(request):
    data = {
        "title1": "Estudiantes",
        "title2": "Consulta De Estudiantes"
    }
    return render(request, "core/estudiante.html", data)

def nota_List(request):
    data = {
        "title1": "Notas",
        "title2": "Consulta de notas"
    }
    return render(request, "core/nota.html", data)

def detallenota_List(request):
    data = {
        "title1": "Detalles de notas",
        "title2": "Consulta De detalles de notas"
    }
    return render(request, "core/detallenota.html", data)
  