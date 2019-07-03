from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Noticia(models.Model):
	 autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	 titulo = models.CharField(max_length = 100, default = '', blank = False)
	 noticia = models.TextField(blank = False)
	 subtitulo = models.CharField(max_length = 100, default = '', blank = True, null = True)
	 resumo = models.TextField(max_length = 500, default='', blank = False)
	 capa  = models.ImageField(upload_to = 'images/', blank = True, default = None)
	 data = models.DateTimeField(null = False)
