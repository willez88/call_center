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


class ClientTypeAdmin(admin.ModelAdmin):
    """!
    Clase que agrega modelo ClientType al panel administrativo

    @author Pedro Alvarez (alvarez.pedrojesus at gmail.com)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>
        GNU Public License versión 2 (GPLv2)</a>
    """

    # Mostrar los campos
    list_display = ('name',)


class DispositionAdmin(admin.ModelAdmin):
    """!
    Clase que agrega modelo Disposition al panel administrativo

    @author Pedro Alvarez (alvarez.pedrojesus at gmail.com)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>
        GNU Public License versión 2 (GPLv2)</a>
    """

    # Mostrar los campos
    list_display = ('name',)


class SubdispositionAdmin(admin.ModelAdmin):
    """!
    Clase que agrega modelo Subdisposition al panel administrativo

    @author Pedro Alvarez (alvarez.pedrojesus at gmail.com)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>
        GNU Public License versión 2 (GPLv2)</a>
    """

    # Mostrar los campos
    list_display = ('name', 'disposition',)


class CallResultAdmin(admin.ModelAdmin):
    """!
    Clase que agrega modelo CallResult al panel administrativo

    @author Pedro Alvarez (alvarez.pedrojesus at gmail.com)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>
        GNU Public License versión 2 (GPLv2)</a>
    """

    # Mostrar los campos
    list_display = ('name',)


class WomAdmin(admin.ModelAdmin):
    """!
    Clase que agrega modelo Wom al panel administrativo

    @author Pedro Alvarez (alvarez.pedrojesus at gmail.com)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>
        GNU Public License versión 2 (GPLv2)</a>
    """

    # Mostrar los campos
    list_display = ('client_name',)


admin.site.register(Project, ProjectAdmin)
admin.site.register(ClientType, ClientTypeAdmin)
admin.site.register(Disposition, DispositionAdmin)
admin.site.register(Subdisposition, SubdispositionAdmin)
admin.site.register(CallResult, CallResultAdmin)
admin.site.register(Wom, WomAdmin)
