from django.conf import settings
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import (
    Group,
    User,
)
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import (
    FormView,
    ListView,
    UpdateView,
)

from base.functions import send_email

from .forms import (
    AgentForm,
    UserForm
)
from .models import Agent


class UserUpdateView(UpdateView):
    """!
    Clase que permite a los usuarios actualizar sus datos

    @author Pedro Alvarez (alvarez.pedrojesus at gmail.com)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>
        GNU Public License versión 2 (GPLv2)</a>
    """

    model = User
    form_class = UserForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('base:home')

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

        user_id = self.kwargs['pk']
        if self.request.user.id == user_id:
            return super().dispatch(request, *args, **kwargs)
        return redirect('base:error_403')

    def get_initial(self):
        """!
        Función que agrega valores predeterminados a los campos del formulario

        @author Pedro Alvarez (alvarez.pedrojesus at gmail.com)
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Diccionario con los valores predeterminados
        """

        initial_data = super().get_initial()
        initial_data['username'] = self.object.username
        initial_data['first_name'] = self.object.first_name
        initial_data['last_name'] = self.object.last_name
        initial_data['email'] = self.object.email
        return initial_data


class AgentListView(PermissionRequiredMixin, ListView):
    """!
    Clase que permite a usuarios supervisores listar usuarios agentes

    @author Pedro Alvarez (alvarez.pedrojesus at gmail.com)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>
        GNU Public License versión 2 (GPLv2)</a>
    """

    permission_required = 'users.view_agent'
    model = Agent
    template_name = 'users/agents/list.html'


class AgentFormView(PermissionRequiredMixin, FormView):
    """!
    Clase que permite a usuarios supervisores crear usuarios agentes

    @author Pedro Alvarez (alvarez.pedrojesus at gmail.com)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>
        GNU Public License versión 2 (GPLv2)</a>
    """

    permission_required = 'users.add_agent'
    model = User
    form_class = AgentForm
    template_name = 'users/agents/create.html'
    success_url = reverse_lazy('users:agent_list')

    def form_valid(self, form):
        """!
        Metodo que valida si el formulario es correcto

        @author Pedro Alvarez (alvarez.pedrojesus at gmail.com)
        @param self <b>{object}</b> Objeto que instancia la clase
        @param form <b>{object}</b> Objeto que contiene el formulario de
            registro
        @return Retorna el formulario validado
        """

        self.object = form.save()
        self.object.username = form.cleaned_data['username']
        self.object.first_name = form.cleaned_data['first_name']
        self.object.last_name = form.cleaned_data['last_name']
        self.object.email = form.cleaned_data['email']
        password = User.objects.make_random_password()
        self.object.set_password(password)
        self.object.is_active = True
        self.object.save()
        self.object.groups.add(Group.objects.get(name='Agente'))
        agent = Agent.objects.create(
            project=form.cleaned_data['project'],
            user=self.object
        )

        admin, admin_email = '', ''
        if settings.ADMINS:
            admin = settings.ADMINS[0][0]
            admin_email = settings.ADMINS[0][1]

        send_email(
            self.object.email, 'users/welcome.mail', 'Bienvenido a Call Center',
            {
                'first_name': self.request.user.first_name,
                'last_name': self.request.user.last_name,
                'email': self.request.user.email,
                'username': self.object.username,
                'password': password,
                'project': agent.project,
                'admin': admin,
                'admin_email': admin_email,
                'emailapp': settings.EMAIL_HOST_USER,
                'url': get_current_site(self.request).name
            }
        )
        return super().form_valid(form)
