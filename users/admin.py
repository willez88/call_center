from django.contrib import admin

from .models import Agent


class AgentAdmin(admin.ModelAdmin):
    """!
    Clase que agrega modelo Agent al panel administrativo

    @author Pedro Alvarez (alvarez.pedrojesus at gmail.com)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>
        GNU Public License versión 2 (GPLv2)</a>
    """

    # Mostrar los campos
    list_display = ('project', 'user',)

    # Aplica select2 en campos desplegables
    autocomplete_fields = (
        'project', 'user',
    )


admin.site.register(Agent, AgentAdmin)
