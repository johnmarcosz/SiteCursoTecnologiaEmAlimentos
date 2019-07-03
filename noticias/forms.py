from django import forms
from .models import Noticia


class noticiaForm(forms.ModelForm):
	class Meta:
		model = Noticia
		fields = ('titulo', 'noticia', 'subtitulo', 'resumo', 'capa')

	def __init__(self, *args, **kwargs):
		super(noticiaForm, self).__init__(*args, **kwargs)
		self.fields['titulo'].widget.attrs.update({'placeholder' : 'Título da notícia'})
		self.fields['subtitulo'].widget.attrs.update({'placeholder' : 'Acontencimento principal da notícia', 'size' : '60'})
		self.fields['noticia'].widget.attrs.update({'placeholder' : 'Conteúdo a ser apresentado na notícia'})
		self.fields['resumo'].widget.attrs.update({'placeholder' : 'Insira um resumo desta notícia para ser apresentado na página inicial'})
