from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    FormView,
    ListView,
    TemplateView,
    UpdateView
)
from django.views.generic.dates import DayArchiveView

from base.models import (
    CallResult,
    Subdisposition,
)

from .forms import (
    SurveyForm,
    WomForm,
)
from .models import Wom


class HomeTemplateView(TemplateView):
    """!
    Clase que muestra la página inicial

    @author Pedro Alvarez (alvarez.pedrojesus at gmail.com)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>
        GNU Public License versión 2 (GPLv2)</a>
    """

    template_name = 'base/base.html'


class Error403TemplateView(TemplateView):
    """!
    Clase que muestra la página de error de permisos

    @author Pedro Alvarez (alvarez.pedrojesus at gmail.com)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>
        GNU Public License versión 2 (GPLv2)</a>
    """

    template_name = 'base/error_403.html'


class WomListView(PermissionRequiredMixin, ListView):
    """!
    Clase que lista los registros de atención al cliente en wom

    @author Pedro Alvarez (alvarez.pedrojesus at gmail.com)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>
        GNU Public License versión 2 (GPLv2)</a>
    """

    permission_required = 'base.view_wom'
    model = Wom
    template_name = 'base/wom/list.html'

    def get_queryset(self):
        """!
        Función que obtiene la lista de registros de atención al cliente asociados al usuario
        En caso de ser supervisor obtiene todos los datos

        @author Pedro Alvarez (alvarez.pedrojesus at gmail.com)
        @param self <b>{object}</b> Objeto que instancia la clase
        @return queryset <b>{object}</b> lista de objetos wom asociados al usuario
        """

        group1 = self.request.user.groups.filter(name='Supervisor')
        group2 = self.request.user.groups.filter(name='Analista')
        if group1 or group2:
            return Wom.objects.all()

        return Wom.objects.filter(user=self.request.user)


class WomCreateView(PermissionRequiredMixin, CreateView):
    """!
    Clase que permite a un usuario registrar solicitudes de mudanzas

    @author Pedro Alvarez (alvarez.pedrojesus at gmail.com)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>
        GNU Public License versión 2 (GPLv2)</a>
    """

    permission_required = 'base.add_wom'
    model = Wom
    form_class = WomForm
    template_name = 'base/wom/create.html'
    success_url = reverse_lazy('base:wom_list')

    def get_form_kwargs(self):
        """!
        Método que permite pasar el usuario actualmente logueado al formulario

        @author Pedro Alvarez (alvarez.pedrojesus at gmail.com)
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Retorna un diccionario con el usuario actualmente logueado
        """

        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def form_valid(self, form):
        """!
        Función que valida si el formulario está correcto

        @author Pedro Alvarez (alvarez.pedrojesus at gmail.com)
        @param self <b>{object}</b> Objeto que instancia la clase
        @param form <b>{object}</b> Objeto que contiene el formulario
        @return super <b>{object}</b> Formulario validado
        """

        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class WomUpdateView(PermissionRequiredMixin, UpdateView):
    """!
    Clase que permite a un usuario actualizar los registros WOM

    @author Pedro Alvarez (alvarez.pedrojesus at gmail.com)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>
        GNU Public License versión 2 (GPLv2)</a>
    """

    permission_required = 'base.change_wom'
    model = Wom
    form_class = WomForm
    template_name = 'base/wom/create.html'
    success_url = reverse_lazy('base:wom_list')

    def dispatch(self, request, *args, **kwargs):
        """!
        Metodo que valida si el usuario del sistema tiene permisos para entrar
        a esta vista

        @author Pedro Alvarez (alvarez.pedrojesus at gmail.com)
        @param self <b>{object}</b> Objeto que instancia la clase
        @param request <b>{object}</b> Objeto que contiene la petición
        @param *args <b>{tupla}</b> Tupla de valores, inicialmente vacia
        @param **kwargs <b>{dict}</b> Diccionario de datos, inicialmente vacio
        @return Redirecciona al usuario a la página de error de permisos si no
            es su perfil
        """

        wom_id = self.kwargs['pk']
        if Wom.objects.filter(pk=wom_id, user=self.request.user).exists():
            return super().dispatch(request, *args, **kwargs)
        return redirect('base:error_403')

    def get_form_kwargs(self):
        """!
        Método que permite pasar el usuario actualmente logueado al formulario

        @author Pedro Alvarez (alvarez.pedrojesus at gmail.com)
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Retorna un diccionario con el usuario actualmente logueado
        """

        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def get_initial(self):
        """!
        Función que agrega valores predeterminados a los campos del formulario

        @author Pedro Alvarez (alvarez.pedrojesus at gmail.com)
        @param self <b>{object}</b> Objeto que instancia la clase
        @return initial_data <b>{object}</b> Valores predeterminado de los
            campos del formulario
        """

        initial_data = super().get_initial()
        initial_data['disposition'] = self.object.subdisposition.disposition
        initial_data['subdisposition'] = self.object.subdisposition
        return initial_data


class WomDeleteView(PermissionRequiredMixin, DeleteView):
    """!
    Clase que permite a un usuario eliminar datos

    @author Pedro Alvarez (alvarez.pedrojesus at gmail.com)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>
        GNU Public License versión 2 (GPLv2)</a>
    """

    permission_required = 'base.delete_wom'
    model = Wom
    template_name = 'base/wom/delete.html'
    success_url = reverse_lazy('base:wom_list')

    def dispatch(self, request, *args, **kwargs):
        """!
        Metodo que valida si el usuario del sistema tiene permisos para entrar
        a esta vista

        @author Pedro Alvarez (alvarez.pedrojesus at gmail.com)
        @param self <b>{object}</b> Objeto que instancia la clase
        @param request <b>{object}</b> Objeto que contiene la petición
        @param *args <b>{tupla}</b> Tupla de valores, inicialmente vacia
        @param **kwargs <b>{dict}</b> Diccionario de datos, inicialmente vacio
        @return Redirecciona al usuario a la página de error de permisos si no
            es su perfil
        """

        wom_id = self.kwargs['pk']
        if Wom.objects.filter(pk=wom_id, user=self.request.user).exists():
            return super().dispatch(request, *args, **kwargs)
        return redirect('base:error_403')

    def delete(self, request, *args, **kwargs):
        """!
        Función que retorna el mensaje de confirmación de la eliminación

        @author Pedro Alvarez (alvarez.pedrojesus at gmail.com)
        @param self <b>{object}</b> Objeto que instancia la clase
        @param request <b>{object}</b> Objeto que contiene los datos de la
            petición
        @param *args <b>{tuple}</b> Tupla de valores, inicialmente vacia
        @param **kwargs <b>{dict}</b> Diccionario de datos, inicialmente vacio
        @return super <b>{object}</b> Objeto con el mensaje de confirmación
            de la eliminación
        """

        return super().delete(request, *args, **kwargs)


class WomDayArchiveView(DayArchiveView):
    """!
    Clase que permite calcular estadísticas de subdisposiciones, resultado de llamadas
    y usuarios agentes de forma diaria

    @author Pedro Alvarez (alvarez.pedrojesus at gmail.com)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>
        GNU Public License versión 2 (GPLv2)</a>
    """

    template_name = 'base/wom/archive_day.html'
    queryset = Wom.objects.all()
    date_field = 'date'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        subdispositions = {}
        for subdisposition in Subdisposition.objects.all():
            subdispositions[subdisposition.name] = subdisposition
        total_subdispositions = {}
        sum_subdispositions = 0
        for key, value in subdispositions.items():
            c = 0
            for wom in self.object_list:
                if wom.subdisposition.name == value.name:
                    c = c + 1
            if c > 0:
                total_subdispositions[value.name] = (value, c)
            sum_subdispositions = sum_subdispositions + c
        context['total_subdispositions'] = total_subdispositions
        context['sum_subdispositions'] = sum_subdispositions

        total_call_results = {}
        sum_call_results = 0
        for call_result in CallResult.objects.all():
            c = 0
            for wom in self.object_list:
                if wom.call_result.name == call_result.name:
                    c = c + 1
            if c > 0:
                total_call_results[call_result.name] = (call_result, c)
            sum_call_results = sum_call_results + c
        context['total_call_results'] = total_call_results
        context['sum_call_results'] = sum_call_results

        total_users = {}
        sum_users = 0
        for user in User.objects.filter(groups__name='Agente'):
            c = 0
            for wom in self.object_list:
                if wom.user.username == user.username:
                    c = c + 1
            if c > 0:
                total_users[user.username] = (user, c)
            sum_users = sum_users + c
        context['total_users'] = total_users
        context['sum_users'] = sum_users
        return context


class SurveyFormView(FormView):
    """!
    Clase que permite subir archivos y hacer filtros

    @author Pedro Alvarez (alvarez.pedrojesus at gmail.com)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>
        GNU Public License versión 2 (GPLv2)</a>
    """

    model = User
    form_class = SurveyForm
    template_name = 'base/surveys/create.html'
    success_url = reverse_lazy('base:home')
