from django.shortcuts import render,redirect
from .forms import *
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from datetime import datetime

def inicio(request):
    return render(request,'views/inicio.html')

#Vista de Votaciones
def crearVotacion(request):
    form = votacionForm()
    if request.user.is_superuser or request.user.is_staff:
        if request.method == 'POST':
            form = votacionForm(request.POST)
            if form.is_valid():
                Votacion = form.save(commit=False)
                Votacion.propietario = request.user
                Votacion.save()
                messages.add_message(request, messages.SUCCESS, 'Votación creada correctamente')
                return redirect('listarvotaciones')
            else:
                form = votacionForm()
                messages.add_message(request, messages.ERROR, 'Error al procesar la solicitud')
    else:
        messages.add_message(request, messages.ERROR, 'Error, No tienes permisos para Acceder')
        return redirect('inicio')
    return render(request,'views/votaciones/crearVotacion.html',{'form':form})

def editarVotacion(request,ide):
    instancia = votacion.objects.get(ide=ide)
    form = votacionForm(instance=instancia)
    if request.user.is_superuser or request.user.is_staff:
        if request.method == "POST":
            form = votacionForm(request.POST, instance=instancia)
            if form.is_valid():
                instancia = form.save(commit=False)
                instancia.save()
                messages.add_message(request, messages.SUCCESS, 'Votación editada correctamente')
                return redirect('listarvotaciones')
            else:
                form = votacionForm()
                messages.add_message(request, messages.ERROR, 'Error, no se puede editar la votación')
    else:
        messages.add_message(request, messages.ERROR, 'Error: No tiene permisos para Acceder')
        return redirect('inicio')
    return render(request,'views/votaciones/editarVotacion.html',{'form':form,'data':instancia})

def eliminarVotacion(request,ide):
    if request.user.is_superuser or request.user.is_staff:
        instancia = votacion.objects.get(ide=ide)
        form = eliminarForm()
        if request.method == 'POST':
            form = eliminarForm(request.POST)
            if form.is_valid():
                instancia.delete()
                messages.add_message(request, messages.SUCCESS, 'Votación Eliminada correctamente')
                return redirect('listarvotaciones')
            else:
                form = votacionForm()
                messages.add_message(request, messages.ERROR, 'Error al procesar la solicitud')
    else:
        messages.add_message(request, messages.ERROR, 'Error, no tienes permiso para acceder')
        return redirect('listarvotaciones')
    return render(request,'views/votaciones/eliminarVotacion.html')

def listarVotaciones(request):
    Votaciones = None
    if not request.user.is_authenticated: 
        return redirect('login')
    else:
        Votaciones = votacion.objects.filter(propietario=request.user)
    context = {
        'data':Votaciones
    }
    return render(request,'views/votaciones/listarVotaciones.html',context)

#Vista de votantes
def crearVotantes(request,ide):
    form = votanteForm()
    Votacion = votacion.objects.get(ide=ide)
    if request.user.is_superuser or request.user.is_staff:
        if request.method == 'POST':
            form = votanteForm(request.POST)
            if not votante.objects.filter(ide=request.POST.get('ide')):
                if form.is_valid():
                    Votante = form.save(commit=False)
                    Votante.votacion = Votacion
                    Votante.save()
                    messages.add_message(request, messages.SUCCESS, 'Votante creado correctamente')
                    return redirect('listarvotaciones')
                else:
                    form = votanteForm()
                    messages.add_message(request, messages.ERROR, 'Error al procesar la solicitud')
            else:
                Votante = votante.objects.get(ide=request.POST.get('ide'))
                for key, value in Votante.votacion.items():
                    if int(key) == ide:
                        messages.add_message(request, messages.ERROR, 'Error, el votante ya esta asignado a la votación')
                        return redirect('listarvotaciones')
                    else:
                        Inicial = Votante.votacion
                        Data = {} 
                        Data[Votacion.ide] ={
                            'votacion':Votacion.ide
                        }
                        Resultado = {}
                        if Inicial != None:
                            Resultado = Inicial | Data
                            Votante.votacion = Resultado
                            Votante.save()
                        else:
                            Votante.votacion = Data
                            Votante.save()
                            messages.add_message(request, messages.SUCCESS, 'Votante Asignado a la votación correctamente')
                        return redirect('listarvotaciones')
    else:
        messages.add_message(request, messages.ERROR, 'Error, No tienes permisos para Acceder')
        return redirect('inicio')
    return render(request,'views/votantes/crearVotantes.html',{'form':form , 'ide':ide})

def editarVotantes(request,ide):
    instancia = votante.objects.get(ide=ide)
    form = votanteForm(instance=instancia)
    if request.user.is_superuser or request.user.is_staff:
        if request.method == "POST":
            form = votanteForm(request.POST, instance=instancia)
            if form.is_valid():
                instancia = form.save(commit=False)
                instancia.save()
                messages.add_message(request, messages.SUCCESS, 'Votante editado correctamente')
                return redirect('../listarvotantes/' + str(instancia.votacion.ide))
            else:
                form = votanteForm()
                messages.add_message(request, messages.ERROR, 'Error, no se puede editar al votante')
    else:
        messages.add_message(request, messages.ERROR, 'Error: No tiene permisos para Acceder')
        return redirect('inicio')
    return render(request,'views/votantes/editarVotantes.html',{'form':form , 'data':instancia})

def eliminarVotantes(request,ide):
    if request.user.is_superuser or request.user.is_staff:
        instancia = votante.objects.get(ide=ide)
        form = eliminarForm()
        if request.method == 'POST':
            form = eliminarForm(request.POST)
            if form.is_valid():
                instancia.delete()
                messages.add_message(request, messages.SUCCESS, 'Votante Eliminado correctamente')
                return redirect('../listarvotantes/' + str(instancia.votacion.ide))
            else:
                form = eliminarForm()
                messages.add_message(request, messages.ERROR, 'Error al procesar la solicitud')
    else:
        messages.add_message(request, messages.ERROR, 'Error, no tienes permiso para acceder')
        return redirect('inicio')
    return render(request,'views/votantes/eliminarVotantes.html',{'form':form})

def listarVotantes(request,ide):
    Votacion = votacion.objects.get(ide=ide)
    Votantes = votante.objects.filter(votacion=ide)
    return render(request,'views/votantes/listarVotantes.html',{'data':Votantes,'votacion':Votacion })

#Vista de Candidatos
def crearCandidatos(request,ide):
    Votacion = votacion.objects.get(ide=ide)
    form = candidatoForm()
    if request.user.is_superuser or request.user.is_staff:
        if request.method == 'POST':
            form = candidatoForm(request.POST,request.FILES)
            if form.is_valid():
                Candidato = form.save(commit=False)
                Candidato.votacion = Votacion
                Candidato.save()
                messages.add_message(request, messages.SUCCESS, 'Candidato creado correctamente')
                return redirect('listarvotaciones')
            else:
                print(form.errors)
                form = candidatoForm()
                messages.add_message(request, messages.ERROR, 'Error al procesar la solicitud')
    else:
        messages.add_message(request, messages.ERROR, 'Error, No tienes permisos para Acceder')
        return redirect('inicio')
    return render(request,'views/candidatos/crearCandidatos.html',{'form':form ,'ide':ide})

def editarCandidatos(request,ide):
    instancia = candidato.objects.get(ide=ide)
    form = candidatoForm(instance=instancia)
    if request.user.is_superuser or request.user.is_staff:
        if request.method == "POST":
            form = candidatoForm(request.POST, instance=instancia)
            if form.is_valid():
                instancia = form.save(commit=False)
                instancia.save()
                messages.add_message(request, messages.SUCCESS, 'Candidato editado correctamente')
                return redirect('../listarcandidatos/'+str(instancia.votacion.ide))
            else:
                form = candidatoForm()
                messages.add_message(request, messages.ERROR, 'Error, no se puede editar al votante')
    else:
        messages.add_message(request, messages.ERROR, 'Error: No tiene permisos para Acceder')
        return redirect('inicio')
    return render(request,'views/candidatos/editarCandidatos.html',{'form':form,'data':instancia})

def eliminarCandidatos(request,ide):
    if request.user.is_superuser or request.user.is_staff:
        instancia = candidato.objects.get(ide=ide)
        form = eliminarForm()
        if request.method == 'POST':
            form = eliminarForm(request.POST)
            if form.is_valid():
                instancia.delete()
                messages.add_message(request, messages.SUCCESS, 'Candidato Eliminado correctamente')
                return redirect('../listarcandidatos/'+str(instancia.votacion.ide))
            else:
                form = eliminarForm()
                messages.add_message(request, messages.ERROR, 'Error al procesar la solicitud')
    else:
        messages.add_message(request, messages.ERROR, 'Error, no tienes permiso para acceder')
        return redirect('inicio')
    return render(request,'views/candidatos/eliminarCandidatos.html',{'form':form})

def listarCandidatos(request,ide):
    Votacion = votacion.objects.get(ide=ide)
    Candidatos = candidato.objects.filter(votacion=ide)
    return render(request,'views/candidatos/listarCandidatos.html',{'data':Candidatos,'votacion':Votacion })

#Vista de Resultados
def vistaResultados(request,ide):
    Votacion = votacion.objects.get(ide=ide)
    Candidatos = candidato.objects.filter(votacion=ide)
    Data={}
    for i in Candidatos:
        Votos = votos.objects.filter(votacion=Votacion.ide,candidato=i.ide).count()
        Data[i.ide] = {
            'candidato':i,
            'votos':Votos
        }
    return render(request,'views/resultados/vistaResultados.html',{'votacion':Votacion,'data':Data.items(),'usuario':request.user})


def register(request):
    if request.user.is_authenticated:
        return redirect('listarvotaciones')
    else:
        if request.method == 'POST':
            form = RegisterUserForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.is_active = True
                user.save()
                return redirect('login')
            else:
                if form.errors:
                    for key, values in form.errors.as_data().items():
                        if key == 'username':
                            messages.info(request, 'Error input fields')
                            break
                        else:
                            for error_value in values:
                                print(error_value)
                                messages.info(request, '%s' % (error_value.message))
                return HttpResponseRedirect(reverse('registro'))
        else:
            form = RegisterUserForm()
            context = {
                'form': form
            }
            return render(request, 'registration/register.html', context)


def prevotacion(request,ide):
    fecha = datetime.now().strftime(format='%Y-%m-%d %H:%M:%S')
    Votante = votante.objects.get(ide=ide)
    for key, value in Votante.votacion.items():
        if int(key) == ide:
            messages.add_message(request, messages.ERROR, 'Error, el votante ya esta asignado a la votación')
            return redirect('listarvotaciones')
        Votaciones = votacion.objects.filter(ide=key).values()
    return render(request, 'views/votaciones/prevotacion.html',{'data':Votaciones,'votante':Votante,'fecha':fecha})

def validarVotante(request):
    form = validarVotanteForm()
    if request.method == 'POST':
        form = validarVotanteForm(request.POST)
        if form.is_valid():
            Votante = votante.objects.filter(ide=request.POST['ide'],nombre=request.POST['nombre'])
            if Votante:
                return redirect('../prevotacion/'+ request.POST['ide'])
            else:
                messages.add_message(request, messages.ERROR, 'Error, no se encuentra esta información relacionada a un votante')
                return redirect('inicio')
        else:
            form = validarVotanteForm()
            messages.add_message(request, messages.ERROR, 'Error al procesar la solicitud')
    return render(request, 'views/votaciones/validarvotante.html',{'form':form})

def realizarVotacion(request,ide,idvotante):
    Voto = votos.objects.filter(votante=idvotante,votacion=ide)
    Votacion=votacion.objects.get(ide=ide)
    fecha = datetime.now().strftime(format='%Y-%m-%d %H:%M:%S')
    if fecha >= Votacion.fecha_inicio.strftime(format='%Y-%m-%d %H:%M:%S') and fecha <= Votacion.fecha_fin.strftime(format='%Y-%m-%d %H:%M:%S'):
        if Voto:
            messages.add_message(request, messages.ERROR, 'Error, Ya el votante realizó la votación')
            return redirect('inicio')
        else:
            Candidatos=candidato.objects.filter(votacion=ide)
            Votacion= votacion.objects.get(ide=ide)
            Votante = votante.objects.get(ide=idvotante)
    else:
        messages.add_message(request, messages.ERROR, 'Error, el tiempo maximo para realizar la votación a finalizado')
        return redirect('inicio')
    return render(request, 'views/votaciones/votacion.html',{'data':Candidatos,'votacion':Votacion,'votante':Votante})

def Votar(request,ide,idvotante,idcandidato):
    Votacion= votacion.objects.get(ide=ide)
    Votante = votante.objects.get(ide=idvotante)
    fecha = datetime.now().strftime(format='%Y-%m-%d %H:%M:%S')
    if fecha >= Votacion.fecha_inicio.strftime(format='%Y-%m-%d %H:%M:%S') and fecha <= Votacion.fecha_fin.strftime(format='%Y-%m-%d %H:%M:%S'):
        if Votante:
            if not votos.objects.filter(votacion=Votacion.ide,votante=Votante.ide):
                Candidato = candidato.objects.get(ide=idcandidato)
                Data=votos(votacion=Votacion,candidato =Candidato,votante =Votante)
                Data.save()
                messages.add_message(request, messages.SUCCESS, 'Votación Realizada correctamente')
                return redirect('inicio')
            else:
                messages.add_message(request, messages.ERROR, 'Ya usted realizó la votación')
                return redirect('inicio')
        else:
            messages.add_message(request, messages.ERROR, 'Error no existe el Votante')
            return redirect('inicio')
    
    