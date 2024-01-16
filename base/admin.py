from django.contrib import admin

from .models import (
    CallResult,
    ClientType,
    Disposition,
    Project,
    Subdisposition,
    Wom,
)


class ProjectAdmin(admin.ModelAdmin):
    """!
    Clase que agrega modelo Project al panel administrativo

    @author Pedro Alvarez (alvarez.pedrojesus at gmail.com)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>
        GNU Public License versión 2 (GPLv2)</a>
    """

    # Mostrar los campos
    list_display = ('name',)

    # Buscar por campos
    search_fields = (
        'name',
    )


class ClientTypeAdmin(admin.ModelAdmin):
    """!
    Clase que agrega modelo ClientType al panel administrativo

    @author Pedro Alvarez (alvarez.pedrojesus at gmail.com)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>
        GNU Public License versión 2 (GPLv2)</a>
    """

    # Mostrar los campos
    list_display = ('name',)

    # Buscar por campos
    search_fields = (
        'name',
    )


class DispositionAdmin(admin.ModelAdmin):
    """!
    Clase que agrega modelo Disposition al panel administrativo

    @author Pedro Alvarez (alvarez.pedrojesus at gmail.com)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>
        GNU Public License versión 2 (GPLv2)</a>
    """

    # Mostrar los campos
    list_display = ('name', 'project',)

    # Buscar por campos
    search_fields = (
        'name',
    )

    # Aplica select2 en campos desplegables
    autocomplete_fields = (
        'project',
    )


class SubdispositionAdmin(admin.ModelAdmin):
    """!
    Clase que agrega modelo Subdisposition al panel administrativo

    @author Pedro Alvarez (alvarez.pedrojesus at gmail.com)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>
        GNU Public License versión 2 (GPLv2)</a>
    """

    # Mostrar los campos
    list_display = ('name', 'disposition',)

    # Buscar por campos
    search_fields = (
        'name',
    )

    # Aplica select2 en campos desplegables
    autocomplete_fields = (
        'disposition',
    )


class CallResultAdmin(admin.ModelAdmin):
    """!
    Clase que agrega modelo CallResult al panel administrativo

    @author Pedro Alvarez (alvarez.pedrojesus at gmail.com)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>
        GNU Public License versión 2 (GPLv2)</a>
    """

    # Mostrar los campos
    list_display = ('name',)

    # Buscar por campos
    search_fields = (
        'name',
    )


class WomAdmin(admin.ModelAdmin):
    """!
    Clase que agrega modelo Wom al panel administrativo

    @author Pedro Alvarez (alvarez.pedrojesus at gmail.com)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>
        GNU Public License versión 2 (GPLv2)</a>
    """

    # Mostrar los campos
    list_display = (
        'client_name', 'id_number', 'retailer_name', 'phone', 'date',
        'client_type', 'subdisposition', 'call_result', 'user',
    )

    # Aplica select2 en campos desplegables
    autocomplete_fields = (
        'client_type', 'subdisposition', 'call_result', 'user',
    )


admin.site.register(Project, ProjectAdmin)
admin.site.register(ClientType, ClientTypeAdmin)
admin.site.register(Disposition, DispositionAdmin)
admin.site.register(Subdisposition, SubdispositionAdmin)
admin.site.register(CallResult, CallResultAdmin)
admin.site.register(Wom, WomAdmin)
