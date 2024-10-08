import pandas as pd

from datetime import datetime
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
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
    Project,
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

    @author William Páez (paez.william8 at gmail.com)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>
        GNU Public License versión 2 (GPLv2)</a>
    """

    template_name = 'base/base.html'


class Error403TemplateView(TemplateView):
    """!
    Clase que muestra la página de error de permisos

    @author William Páez (paez.william8 at gmail.com)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>
        GNU Public License versión 2 (GPLv2)</a>
    """

    template_name = 'base/403.html'


class Error404TemplateView(TemplateView):
    """!
    Clase que muestra la página de error 404

    @author William Páez (paez.william8 at gmail.com)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>
        GNU Public License versión 2 (GPLv2)</a>
    """

    template_name = 'base/404.html'


class WomListView(PermissionRequiredMixin, ListView):
    """!
    Clase que lista los registros de atención al cliente en wom

    @author William Páez (paez.william8 at gmail.com)
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

        @author William Páez (paez.william8 at gmail.com)
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

    @author William Páez (paez.william8 at gmail.com)
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

        @author William Páez (paez.william8 at gmail.com)
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Retorna un diccionario con el usuario actualmente logueado
        """

        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def form_valid(self, form):
        """!
        Función que valida si el formulario está correcto

        @author William Páez (paez.william8 at gmail.com)
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

    @author William Páez (paez.william8 at gmail.com)
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

        @author William Páez (paez.william8 at gmail.com)
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

        @author William Páez (paez.william8 at gmail.com)
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Retorna un diccionario con el usuario actualmente logueado
        """

        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def get_initial(self):
        """!
        Función que agrega valores predeterminados a los campos del formulario

        @author William Páez (paez.william8 at gmail.com)
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

    @author William Páez (paez.william8 at gmail.com)
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

        @author William Páez (paez.william8 at gmail.com)
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

        @author William Páez (paez.william8 at gmail.com)
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

    @author William Páez (paez.william8 at gmail.com)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>
        GNU Public License versión 2 (GPLv2)</a>
    """

    template_name = 'base/calendars/archive_day.html'
    queryset = Wom.objects.all()
    date_field = 'date'
    month_format = '%m'

    def dispatch(self, request, *args, **kwargs):
        """!
        Metodo que valida si el usuario del sistema tiene permisos para entrar
        a esta vista

        @author William Páez (paez.william8 at gmail.com)
        @param self <b>{object}</b> Objeto que instancia la clase
        @param request <b>{object}</b> Objeto que contiene la petición
        @param *args <b>{tupla}</b> Tupla de valores, inicialmente vacia
        @param **kwargs <b>{dict}</b> Diccionario de datos, inicialmente vacio
        @return Redirecciona al usuario a la página de error de permisos 
        """

        woms = Wom.objects.filter(
            date=datetime(kwargs['year'], kwargs['month'], kwargs['day'])
        )
        if not woms:
            return redirect('base:error_403')
        if self.request.user.groups.filter(name='Supervisor'):
            return super().dispatch(request, *args, **kwargs)
        return redirect('base:error_403')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        subdispositions = {}
        for subdisposition in Subdisposition.objects.all():
            subdispositions[subdisposition.name] = subdisposition
        
        # Proyecto Colombia
        total_subdispositions_colombia = {}
        sum_subdispositions_colombia = 0
        for key, value in subdispositions.items():
            c = 0
            for wom in self.object_list.filter(user__agent__project__name='Colombia'):
                if wom.subdisposition.name == value.name:
                    c = c + 1
            if c > 0:
                total_subdispositions_colombia[value.name] = (value, c)
            sum_subdispositions_colombia = sum_subdispositions_colombia + c
        context['total_subdispositions_colombia'] = total_subdispositions_colombia
        context['sum_subdispositions_colombia'] = sum_subdispositions_colombia

        total_call_results_colombia = {}
        sum_call_results_colombia = 0
        for call_result in CallResult.objects.all():
            c = 0
            for wom in self.object_list.filter(user__agent__project__name='Colombia'):
                if wom.call_result.name == call_result.name:
                    c = c + 1
            if c > 0:
                total_call_results_colombia[call_result.name] = (call_result, c)
            sum_call_results_colombia = sum_call_results_colombia + c
        context['total_call_results_colombia'] = total_call_results_colombia
        context['sum_call_results_colombia'] = sum_call_results_colombia

        total_users_colombia = {}
        sum_users_colombia = 0
        for user in User.objects.filter(groups__name='Agente'):
            c = 0
            for wom in self.object_list.filter(user__agent__project__name='Colombia'):
                if wom.user.username == user.username:
                    c = c + 1
            if c > 0:
                total_users_colombia[user.username] = (user, c)
            sum_users_colombia = sum_users_colombia + c
        context['total_users_colombia'] = total_users_colombia
        context['sum_users_colombia'] = sum_users_colombia

        # Proyecto Perú
        total_subdispositions_peru = {}
        sum_subdispositions_peru = 0
        for key, value in subdispositions.items():
            c = 0
            for wom in self.object_list.filter(user__agent__project__name='Perú'):
                if wom.subdisposition.name == value.name:
                    c = c + 1
            if c > 0:
                total_subdispositions_peru[value.name] = (value, c)
            sum_subdispositions_peru = sum_subdispositions_peru + c
        context['total_subdispositions_peru'] = total_subdispositions_peru
        context['sum_subdispositions_peru'] = sum_subdispositions_peru

        total_call_results_peru = {}
        sum_call_results_peru = 0
        for call_result in CallResult.objects.all():
            c = 0
            for wom in self.object_list.filter(user__agent__project__name='Perú'):
                if wom.call_result.name == call_result.name:
                    c = c + 1
            if c > 0:
                total_call_results_peru[call_result.name] = (call_result, c)
            sum_call_results_peru = sum_call_results_peru + c
        context['total_call_results_peru'] = total_call_results_peru
        context['sum_call_results_peru'] = sum_call_results_peru

        total_users_peru = {}
        sum_users_peru = 0
        for user in User.objects.filter(groups__name='Agente'):
            c = 0
            for wom in self.object_list.filter(user__agent__project__name='Perú'):
                if wom.user.username == user.username:
                    c = c + 1
            if c > 0:
                total_users_peru[user.username] = (user, c)
            sum_users_peru = sum_users_peru + c
        context['total_users_peru'] = total_users_peru
        context['sum_users_peru'] = sum_users_peru

        # Proyecto Wom
        total_subdispositions_wom = {}
        sum_subdispositions_wom = 0
        for key, value in subdispositions.items():
            c = 0
            for wom in self.object_list.filter(user__agent__project__name='WOM'):
                if wom.subdisposition.name == value.name:
                    c = c + 1
            if c > 0:
                total_subdispositions_wom[value.name] = (value, c)
            sum_subdispositions_wom = sum_subdispositions_wom + c
        context['total_subdispositions_wom'] = total_subdispositions_wom
        context['sum_subdispositions_wom'] = sum_subdispositions_wom

        total_call_results_wom = {}
        sum_call_results_wom = 0
        for call_result in CallResult.objects.all():
            c = 0
            for wom in self.object_list.filter(user__agent__project__name='WOM'):
                if wom.call_result.name == call_result.name:
                    c = c + 1
            if c > 0:
                total_call_results_wom[call_result.name] = (call_result, c)
            sum_call_results_wom = sum_call_results_wom + c
        context['total_call_results_wom'] = total_call_results_wom
        context['sum_call_results_wom'] = sum_call_results_wom

        total_users_wom = {}
        sum_users_wom = 0
        for user in User.objects.filter(groups__name='Agente'):
            c = 0
            for wom in self.object_list.filter(user__agent__project__name='WOM'):
                if wom.user.username == user.username:
                    c = c + 1
            if c > 0:
                total_users_wom[user.username] = (user, c)
            sum_users_wom = sum_users_wom + c
        context['total_users_wom'] = total_users_wom
        context['sum_users_wom'] = sum_users_wom
        return context


class SurveyFormView(FormView):
    """!
    Clase que permite subir archivos y hacer filtros

    @author William Páez (paez.william8 at gmail.com)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>
        GNU Public License versión 2 (GPLv2)</a>
    """

    form_class = SurveyForm
    template_name = 'base/surveys/upload.html'

    def dispatch(self, request, *args, **kwargs):
        """!
        Metodo que valida si el usuario del sistema tiene permisos para entrar
        a esta vista

        @author William Páez (paez.william8 at gmail.com)
        @param self <b>{object}</b> Objeto que instancia la clase
        @param request <b>{object}</b> Objeto que contiene la petición
        @param *args <b>{tupla}</b> Tupla de valores, inicialmente vacia
        @param **kwargs <b>{dict}</b> Diccionario de datos, inicialmente vacio
        @return Redirecciona al usuario a la página de error de permisos 
        """

        if self.request.user.groups.filter(name='Supervisor'):
            return super().dispatch(request, *args, **kwargs)
        return redirect('base:error_403')

    def post(self, request, *args, **kwargs):
        project = request.POST.get('project')
        project = get_object_or_404(Project, pk=project)
        df = pd.read_csv(request.FILES['file'], delimiter=';')
        surveys = [list(row) for row in df.values]
        results = {}
        question1 = 0
        question2 = 0
        question3 = 0
        question4 = 0
        question5 = 0
        for survey in surveys:
            date = str(survey[3])
            if date != 'nan':
                date = datetime.strptime(date, '%d/%m/%Y')
                woms = Wom.objects.filter(
                    date=date, phone=survey[1], user__agent__project=project,
                )
                for wom in woms:
                    if 1 == survey[4]:
                        question1 = question1 + 1
                        results[wom.subdisposition.name] = (wom.subdisposition, question1, '', '', '', '')
                    elif 2 == survey[4]:
                        question2 = question2 + 1
                        results[wom.subdisposition.name] = (wom.subdisposition, '', question2, '', '', '')
                    elif 3 == survey[4]:
                        question3 = question3 + 1
                        results[wom.subdisposition.name] = (wom.subdisposition, '', '', question3, '', '')
                    elif 4 == survey[4]:
                        question4 = question4 + 1
                        results[wom.subdisposition.name] = (wom.subdisposition, '', '', '', question4, '')
                    elif 5 == survey[4]:
                        question5 = question5 + 1
                        results[wom.subdisposition.name] = (wom.subdisposition, '', '', '', '', question5)
        return render(
            request, 'base/surveys/result.html', {'results': results, 'project': project}
        )


class CalendarTemplateView(TemplateView):
    """!
    Clase que muestra el calendario

    @author William Páez (paez.william8 at gmail.com)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>
        GNU Public License versión 2 (GPLv2)</a>
    """

    template_name = 'base/calendars/list.html'
