
function move_datepicker_values()
{
    jQuery('.datepicker').each(function (i, obj){
        id = obj.id;
        value = jQuery('#initial-'+id).val();
        if (value) {
            jQuery('#'+id).val(value.split('-').reverse().join('-'));
        }
    })
}

function setDatePickerById(widget_id)
{
    var widget = "#" + widget_id;
    jQuery(widget).datepicker({
        changeMonth: true,
        changeYear: true,
        yearRange: '-100y:c+nn',
        showOn: "button",
        buttonImage: "/static/img/calendar.gif",
        buttonImageOnly: true,
        showOtherMonths: true,
        selectOtherMonths: true,
        dateFormat: "dd-mm-yy",
        firstDay: 1
    });
    comonDatePickers(widget);
}

function comonDatePickers(widget)
{
    jQuery(widget).datepicker( "option", "monthNames", ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"] );
    jQuery(widget).datepicker( "option", "monthNamesShort", ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"] );
    jQuery(widget).datepicker( "option", "dayNamesShort", ['Domingo', 'Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado'] );
    jQuery(widget).datepicker( "option", "dayNamesShort", ['Dom', 'Lun', 'Mar', 'Mie', 'Jue', 'Vie', 'Sab'] );
    jQuery(widget).datepicker( "option", "dayNamesMin", ['Do', 'Lu', 'Ma', 'Mi', 'Ju', 'Vi', 'Sa'] );
}

function setDatePickersByClass(widget_class)
{
    var widget = "." + widget_class;
    jQuery(widget).datepicker({
        changeMonth: true,
        changeYear: true,
        yearRange: '-100y:c+nn',
        showOn: "button",
        buttonImage: "/static/img/calendar.gif",
        buttonImageOnly: true,
        showOtherMonths: true,
        selectOtherMonths: true,
        dateFormat: "dd-mm-yy",
        firstDay: 1
    });
    comonDatePickers(widget);
}

function setMaxDateToToday(widget_class)
{
    var widget = "." + widget_class;
    jQuery(widget).datepicker({
        changeMonth: true,
        changeYear: true,
        yearRange: '-100y:c+nn',
        showOn: "button",
        buttonImage: "/static/img/calendar.gif",
        buttonImageOnly: true,
        showOtherMonths: true,
        selectOtherMonths: true,
        maxDate: 0,
        dateFormat: "dd-mm-yy",
        firstDay: 1
    });
    comonDatePickers(widget);
}

jQuery(document).ready(function(){
    setDatePickersByClass('datepicker');
    setMaxDateToToday('datepicker_max_date_today');
    // move_datepicker_values();
});


