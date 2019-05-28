from django.urls import path
from .views import (
	IndexView,
	PreguntaDetail,
	PreguntaCreate,
	PreguntaUpdate,
	PreguntaDelete
	)

# Se pueden pasar datos desde la url, la info está en el pdf "Django_parte_3_url_views_request" 
app_name = 'polls'
urlpatterns = [
	path('', IndexView.as_view(), name='index'),
	path( # Esta seria una forma mas visible de una url, tal vez nos conviene usarla así para que sea mas entendible
		route='detalle/<int:pk>',
		view=PreguntaDetail.as_view(),
		name='detalle'
	),
	path('pregunta/create/', PreguntaCreate.as_view(), name = 'pregunta_create'),
	path('pregunta/update/<int:pk>', PreguntaUpdate.as_view(), name = 'pregunta_update'),
	path('pregunta/delete/<int:pk>', PreguntaDelete.as_view(), name = 'pregunta_delete'),
]
