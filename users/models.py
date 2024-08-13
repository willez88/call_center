from django.contrib.auth.models import User
from django.db import models

from base.models import Project


class Agent(models.Model):
    """!
    Clase que contiene los datos de un agente

    @author William Páez (paez.william8 at gmail.com)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>
        GNU Public License versión 2 (GPLv2)</a>
    """

    # Relación con el modelo Project
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, verbose_name='proyecto',
        db_comment='Relación con el modelo proyecto',
    )

    # Relación con el modelo User
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, verbose_name='usuario',
        db_comment='Relación con el modelo usuario',
    )

    def __str__(self):
        """!
        Función para representar la clase de forma amigable

        @author William Páez (paez.william8 at gmail.com)
        @param self <b>{object}</b> Objeto que instancia la clase
        @return string <b>{object}</b> Objeto con el valor
        """

        return self.user.first_name + ' ' + self.user.last_name + ' | ' + str(self.project)

    class Meta:
        """!
        Meta clase del modelo que establece algunas propiedades

        @author William Páez (paez.william8 at gmail.com)
        """

        verbose_name = 'Agente'
        verbose_name_plural = 'Agentes'
