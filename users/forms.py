from django.contrib.auth.models import User
from django import forms


class UserForm(forms.ModelForm):
    """!
    Clase que contiene los campos del formulario

    @author Pedro Alvarez (alvarez.pedrojesus at gmail.com)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>
        GNU Public License versión 2 (GPLv2)</a>
    """

    # Nombre de usuario
    username = forms.CharField(
        label='Nombre de Usuario:',
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip',
                'title': 'Indique el nombre de usuario',
            }
        )
    )

    # Nombres
    first_name = forms.CharField(
        label='Nombres:',
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip',
                'title': 'Indique los Nombres',
            }
        )
    )

    # Apellidos
    last_name = forms.CharField(
        label='Apellidos:',
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip',
                'title': 'Indique los Apellidos',
            }
        )
    )

    # Correo
    email = forms.EmailField(
        label='Correo Electrónico:',
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control input-sm email-mask',
                'data-toggle': 'tooltip',
                'title': 'Indique el correo electrónico'
            }
        )
    )

    class Meta:
        """!
        Meta clase del formulario que establece algunas propiedades

        @author Pedro Alvarez (alvarez.pedrojesus at gmail.com)
        """

        model = User
        fields = ['username', 'first_name', 'last_name', 'email',]
