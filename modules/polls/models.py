from django.db import models

# Create your models here.

class Pregunta(models.Model):
	titulo = models.CharField(max_length=200, help_text='queremos que guardes el titulo de la pregunta')
	creacion = models.DateTimeField(auto_now_add=True)
	modificacion = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name='pregunta'
		verbose_name_plural = 'preguntas'
		ordering = ['-creacion']
		#esto ordena las preguntas por fecha donde trae las últimas primero.

	def __str__(self):
	#poner un nombre cuando traemos un conjunto de preguntas.
		return '%s' % (self.titulo)

class Opcion(models.Model):
	pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
	titulo = models.CharField(max_length=200, help_text='Queremos que guardes el título de la opcion')
	votos = models.IntegerField(help_text='Votos de la opcion')

	class Meta:
		verbose_name='opcion'
		verbose_name_plural = 'opciones'
		ordering = ['votos']

	def __str__(self): #Esto hace que cuando nos muestre el nombre (en este caso el titulo) en el administrador o la pagina
		return '%s' % (self.titulo)
