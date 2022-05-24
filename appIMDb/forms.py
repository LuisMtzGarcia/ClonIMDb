from django import forms

from .models import Review

class ReviewForm(forms.ModelForm):
    """ El formulario para crear una resenia. """

    class Meta:
        model = Review
        fields = ['pelicula', 'texto']
        labels = {'pelicula': '', 'texto': 'Resenia'}
        widgets = {'texto': forms.Textarea(attrs={'cols': 80})}
        # Sobrescribe el widget default de Django.
        # El widget de texto tiene por default un area de texto de 40 columnas,
        # lo cambio a 80 para que el usuario tenga mas espacio.