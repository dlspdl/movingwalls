function addDays(date, days) {
  const dt = new Date(Number(date))
  dt.setDate(date.getDate() + days)
  return dt
}

const date = new Date();
const newDate = addDays(date, 2);

$(function () {
  $(".dateinput").attr("autocomplete", "off");

  if ( $("input[name='end_date']").val() == "" ) {    
    $("input[name='end_date']").prop('disabled', true);
  }

  $("input[name='end_date']").datepicker({
    format: 'yyyy-mm-dd',
    startDate: newDate
  });

  $("input[name='start_date']").datepicker({
    format: 'yyyy-mm-dd',
    startDate: newDate
    }).on('changeDate', function (selected) {
    $("input[name='end_date']").datepicker(
      'setStartDate', 
      addDays(new Date($("input[name='start_date']").val()),1)
    );
    $("input[name='end_date']").prop('disabled', false);
  });
});

