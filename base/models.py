from django.contrib.auth.models import User
from django.db import models


class Project(models.Model):
    """!
    Clase que contiene los proyectos

    @author Pedro Alvarez (alvarez.pedrojesus at gmail.com)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>
        GNU Public License versión 2 (GPLv2)</a>
    """

    # Nombre del pais
    name = models.CharField(
        'nombre', max_length=80, db_comment='Nombre del proyecto',
    )

    def __str__(self):
        """!
        Función para representar la clase de forma amigable

        @author Pedro Alvarez (alvarez.pedrojesus at gmail.com)
        @param self <b>{object}</b> Objeto que instancia la clase
        @return string <b>{object}</b> Objeto con el nombre
        """

        return self.name
    
    class Meta:
        """!
        Meta clase del modelo que establece algunas propiedades

        @author Pedro Alvarez (alvarez.pedrojesus at gmail.com)
        """

        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'


class ClientType(models.Model):
    """!
    Clase que contiene el tipo de cliente

    @author Pedro Alvarez (alvarez.pedrojesus at gmail.com)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>
        GNU Public License versión 2 (GPLv2)</a>
    """

    # Nombre
    name = models.CharField(
        'nombre', max_length=30, db_comment='Nombre del tipo de cliente',
    )

    def __str__(self):
        """!
        Función para representar la clase de forma amigable

        @author Pedro Alvarez (alvarez.pedrojesus at gmail.com)
        @param self <b>{object}</b> Objeto que instancia la clase
        @return string <b>{object}</b> Objeto con el nombre
        """

        return self.name

    class Meta:
        """!
        Meta clase del modelo que establece algunas propiedades

        @author Pedro Alvarez (alvarez.pedrojesus at gmail.com)
        """

        verbose_name = 'Tipo de cliente'
        verbose_name_plural = 'Tipos de cliente'


class Disposition(models.Model):
    """!
    Clase que contiene las disposiciones

    @author Pedro Alvarez (alvarez.pedrojesus at gmail.com)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>
        GNU Public License versión 2 (GPLv2)</a>
    """

    # Nombre
    name = models.CharField(
        'nombre', max_length=100, db_comment='Nombre la disposición',
    )

    # Relación con el modelo Project
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, verbose_name='proyecto', null=True,
        db_comment='Relación con el modelo proyecto',
    )

    def __str__(self):
        """!
        Función para representar la clase de forma amigable

        @author Pedro Alvarez (alvarez.pedrojesus at gmail.com)
        @param self <b>{object}</b> Objeto que instancia la clase
        @return string <b>{object}</b> Objeto con el nombre
        """

        return self.name + ' | ' + str(self.project)

    class Meta:
        """!
        Meta clase del modelo que establece algunas propiedades

        @author Pedro Alvarez (alvarez.pedrojesus at gmail.com)
        """

        verbose_name = 'Disposición'
        verbose_name_plural = 'Disposiciones'


class Subdisposition(models.Model):
    """!
    Clase que contiene las subdisposiciones

    @author Pedro Alvarez (alvarez.pedrojesus at gmail.com)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>
        GNU Public License versión 2 (GPLv2)</a>
    """

    # Nombre
    name = models.CharField(
        'nombre', max_length=100, db_comment='Nombre la subdisposición',
    )

    # Relación con el modelo Disposition
    disposition = models.ForeignKey(
        Disposition, on_delete=models.CASCADE, verbose_name='Disposición',
        db_comment='Relación con el modelo disposición',
    )

    def __str__(self):
        """!
        Función para representar la clase de forma amigable

        @author Pedro Alvarez (alvarez.pedrojesus at gmail.com)
        @param self <b>{object}</b> Objeto que instancia la clase
        @return string <b>{object}</b> Objeto con el nombre
        """

        return self.name

    class Meta:
        """!
        Meta clase del modelo que establece algunas propiedades

        @author Pedro Alvarez (alvarez.pedrojesus at gmail.com)
        """

        verbose_name = 'Subdisposición'
        verbose_name_plural = 'Subdisposiciones'


class CallResult(models.Model):
    """!
    Clase que contiene los resultados de llamada

    @author Pedro Alvarez (alvarez.pedrojesus at gmail.com)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>
        GNU Public License versión 2 (GPLv2)</a>
    """

    # Nombre
    name = models.CharField(
        'nombre', max_length=50, db_comment='Nombre del resultado de la llamada',
    )

    def __str__(self):
        """!
        Función para representar la clase de forma amigable

        @author Pedro Alvarez (alvarez.pedrojesus at gmail.com)
        @param self <b>{object}</b> Objeto que instancia la clase
        @return string <b>{object}</b> Objeto con el nombre
        """

        return self.name

    class Meta:
        """!
        Meta clase del modelo que establece algunas propiedades

        @author Pedro Alvarez (alvarez.pedrojesus at gmail.com)
        """

        verbose_name = 'Resultado de llamda'
        verbose_name_plural = 'Resultados de llamada'


class Wom(models.Model):
    """!
    Clase que contiene el formulario de llamadas

    @author Pedro Alvarez (alvarez.pedrojesus at gmail.com)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>
        GNU Public License versión 2 (GPLv2)</a>
    """

    # Nombre del cliente
    client_name = models.CharField(
        'nombre del cliente', max_length=100, db_comment='Nombre del cliente',
    )

    # Cédula o dni
    id_number = models.CharField(
        'cédula o dni', max_length=20, null=True, blank=True,
        db_comment='Cédula o dni del cliente',
    )

    # Nombre del minorista
    retailer_name = models.CharField(
        max_length=100, db_comment='Nombre del minorista',
    )

    # Teléfono
    phone = models.CharField(
        'teléfono', max_length=20, db_comment='Teléfono',
    )

    # Fecha
    date = models.DateField(
        'fecha', auto_now_add=True, db_comment='Fecha del registro',
    )

    # Relación con el modelo ClientType
    client_type = models.ForeignKey(
        ClientType, on_delete=models.CASCADE, verbose_name='tipo de cliente',
        db_comment='Relación con el modelo tipo de cliente',
    )

    # Relación con el modelo subdisposition
    subdisposition = models.ForeignKey(
        Subdisposition, on_delete=models.CASCADE, verbose_name='subdisposición',
        db_comment='Relación con el modelo subdisposición',
    )

    # Relación con el modelo CallResult
    call_result = models.ForeignKey(
        CallResult, on_delete=models.CASCADE, verbose_name='resultado de llamada',
        db_comment='Relación con el modelo resultado de llamada',
    )

    # Relación con el modelo User
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='usuario',
        db_comment='Relación con el modelo usuario',
    )

    def get_project(self):
        """!
        Función que obtiene el proyecto de un agente

        @author Pedro Alvarez (alvarez.pedrojesus at gmail.com)
        @param self <b>{object}</b> Objeto que instancia la clase
        @return string <b>object</b> Objeto con el correo
        """

        return self.user.agent.project

    # Agrega una descripción corta al nombre de la Función
    get_project.short_description = 'proyecto'

    def __str__(self):
        """!
        Función para representar la clase de forma amigable

        @author Pedro Alvarez (alvarez.pedrojesus at gmail.com)
        @param self <b>{object}</b> Objeto que instancia la clase
        @return string <b>{object}</b> Objeto con el nombre
        """

        return self.client_name
