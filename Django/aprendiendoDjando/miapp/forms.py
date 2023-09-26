from django import forms
from django.core import validators

class ForArticle(forms.Form):
    title = forms.CharField(
        label="Título",
        max_length= 20,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': ' Ingresa el título',
                'class' : 'titulo_form_article'
            }
        ),
        validators=[
            validators.MinLengthValidator(4, 'El título es demasiado corto'),
            validators.RegexValidator(
                regex=r'^[a-zA-Z0-9ñ ]*$',
                message='El título debe contener solo caracteres alfanuméricos',
                code="invalid_title" 
            ),
        ]
    )

    content = forms.CharField(
        label = "Contenido",
        widget=forms.Textarea(
            attrs={
                'placeholder': ' Ingresa el contenido',
                'class' : 'contenido_form_article'
            }
        ),
        validators =[
            validators.MaxLengthValidator(20, "El límite es 20 caracteres")
        ]

    )

    '''
    #Otra forma de hacer de personalizar el widget
    content.widget.attrs.update(
        {
            'placeholder': ' Ingresa el contenido',
            'class' : 'contenido_form_article',
            'id' : 'contenido_form'
        }
    )'''

    public_options = [
        (1, "Si"),
        (0, "No")
    ]

    public = forms.TypedChoiceField(
        label="¿Publicado?",
        choices = public_options 
    )
