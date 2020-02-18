$(function () {
  $('#travel_table').DataTable({
    "pagingType": "first_last_numbers" 
  });

  $('.dataTables_length').addClass('bs-select');
  $( "button" ).click(function() {
    $(".modal").css("display", "block");
  });

  $( "#close" ).click(function() {
    $(".modal").css("display", "none");
  });
});
