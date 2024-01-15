from django import forms

from .models import (
    CallResult,
    ClientType,
    Disposition,
    Subdisposition,
    Wom,
)


class WomForm(forms.ModelForm):
    """!
    Clase que contiene los campos del formulario

    @author Pedro Alvarez (alvarez.pedrojesus at gmail.com)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>
        GNU Public License versión 2 (GPLv2)</a>
    """

    def __init__(self, *args, **kwargs):
        """!
        Método que permite inicializar el formulario

        @author Pedro Alvarez (alvarez.pedrojesus at gmail.com)
        @param self <b>{object}</b> Objeto que instancia la clase
        @param *args <b>{tupla}</b> Tupla de valores, inicialmente vacia
        @param *kwargs <b>{dict}</b> Diccionario de datos, inicialmente vacio
        """

        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        disposition_list = [('', 'Selecione...')]
        for disposition in Disposition.objects.filter(project=user.agent.project):
            disposition_list.append((disposition.id, disposition.name))
        self.fields['disposition'].choices = disposition_list

    # Nombre del cliente
    client_name = forms.CharField(
        label='APP ID - Nombre:',
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip',
                'title': 'Indique el nombre del cliente',
            }
        )
    )

    # Nombre del minorista
    retailer_name = forms.CharField(
        label='Retailer Name:',
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip',
                'title': 'Indique el nombre del minorista',
            }
        )
    )

    # Cédula o dni
    id_number = forms.CharField(
        label='Cédula o DNI:',
        max_length=20,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip',
                'title': 'Indique el nombre del cliente',
            }
        ),
        required=False
    )

    # Número de teléfono
    phone = forms.CharField(
        label='Teléfono:',
        max_length=20,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip',
                'title': 'Indique el número de teléfono',
            }
        )
    )

    # Tipo de cliente
    client_type = forms.ModelChoiceField(
        label='Tipo de cliente:',
        queryset=ClientType.objects.all(),
        empty_label='Seleccione...',
        widget=forms.Select(attrs={
            'class': 'form-control select2', 'data-toggle': 'tooltip',
            'title': 'Seleccione el tipo de cliente',
        })
    )

    # Disposición
    disposition = forms.ModelChoiceField(
        label='Disposición:',
        queryset=Disposition.objects.all(),
        empty_label='Seleccione...',
        widget=forms.Select(attrs={
            'class': 'form-control select2', 'data-toggle': 'tooltip',
            'title': 'Seleccione la disposición',
            'onchange': "combo_update(this.value, 'base', 'Subdisposition', 'disposition',\
                'pk', 'name', 'id_subdisposition')",
        })
    )

    # Subdisposition
    subdisposition = forms.ModelChoiceField(
        label='Subdisposición:',
        queryset=Subdisposition.objects.all(),
        empty_label='Seleccione...',
        widget=forms.Select(attrs={
            'class': 'form-control select2', 'data-toggle': 'tooltip',
            'title': 'Seleccione el puente.', 'disabled': 'true',
        })
    )

    # Resultados de llamadas
    call_result = forms.ModelChoiceField(
        label='Resultado de la llamada:',
        queryset=CallResult.objects.all(),
        empty_label='Seleccione...',
        widget=forms.Select(attrs={
            'class': 'form-control select2', 'data-toggle': 'tooltip',
            'title': 'Seleccione el resultado de la llamada.',
        })
    )

    class Meta:
        """!
        Meta clase del formulario que establece algunas propiedades

        @author Pedro Alvarez (alvarez.pedrojesus at gmail.com)
        """

        model = Wom
        fields = [
            'client_name', 'id_number', 'retailer_name', 'phone', 'client_type',
            'subdisposition', 'call_result',
        ]


class SurveyForm(forms.Form):
    """!
    Clase que contiene los campos del formulario

    @author Pedro Alvarez (alvarez.pedrojesus at gmail.com)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>
        GNU Public License versión 2 (GPLv2)</a>
    """

    # Archivo
    file = forms.FileField(
        label='Archivo:',
        widget=forms.ClearableFileInput(attrs={
            'class': 'custom-file-input',
        }),
    )
