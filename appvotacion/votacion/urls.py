from django.urls import path,include
from votacion import views

urlpatterns = [
path("",views.inicio,name='inicio'),
path('accounts/',include('django.contrib.auth.urls')),
path('registro',views.register,name='registro'),
#URl Votacion
path('crearvotacion',views.crearVotacion,name='crearvotacion'),
path('editarvotacion/<int:ide>',views.editarVotacion,name='editarvotacion'),
path('eliminarvotacion/<int:ide>',views.eliminarVotacion,name='eliminarvotacion'),
path('listarvotaciones',views.listarVotaciones,name='listarvotaciones'),
path('validarvotante',views.validarVotante,name='validarvotante'),
path('prevotacion/<int:ide>',views.prevotacion,name='prevotacion'),
path('votacion/<int:ide>/<int:idvotante>',views.realizarVotacion,name='votacion'),
path('votar/<int:ide>/<int:idvotante>/<int:idcandidato>',views.Votar,name='votar'),
#URL Votantes
path('crearvotante/<int:ide>',views.crearVotantes,name='crearvotante'),
path('editarvotante/<int:ide>',views.editarVotantes,name='editarvotante'),
path('eliminarvotante/<int:ide>',views.eliminarVotantes,name='eliminarvotante'),
path('listarvotantes/<int:ide>',views.listarVotantes,name='listarvotantes'),
#URL Candidatos
path('crearcandidato/<int:ide>',views.crearCandidatos,name='crearcandidato'),
path('editarcandidato/<int:ide>',views.editarCandidatos,name='editarcandidato'),
path('eliminarcandidato/<int:ide>',views.eliminarCandidatos,name='eliminarcandidato'),
path('listarcandidatos/<int:ide>',views.listarCandidatos,name='listarcandidatos'),
#URL resultados
path('vistaresultados/<int:ide>',views.vistaResultados,name='vistaresultados'),    
]