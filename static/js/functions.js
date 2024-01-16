/**
 * @brief Función que agrega los botones de descarga a una dataTable
 *
 * @author Pedro Alvarez (alvarez.pedrojesus at gmail.com)
 * @copyright <a href='http://www.gnu.org/licenses/gpl-3.0.html'>GNU Public License versión 3 (GPLv3)</a>
 * @param table Objeto que contiene la instancia de un Datatable
 */
function button_datatable(table) {
  new $.fn.dataTable.Buttons(table, {
    buttons: [
      {
        extend: 'csvHtml5',
        fieldBoundary: '',
        fieldSeparator: ';',
        title: 'call_center',
      },
      {
        extend: 'excelHtml5',
        title: 'call_center',
      },
      {
        extend: 'pdfHtml5',
        title: 'call_center',
      },      
    ],
  });
  table.buttons().container().appendTo(table.table().container());
}
