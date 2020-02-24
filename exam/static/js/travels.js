var request;

$(function () {
  $('#travel_table').DataTable({
    "pagingType": "first_last_numbers" 
  });

  $('.dataTables_length').addClass('bs-select');

  $("button").click(function() {
    if ($(this).text() == 'DELETE'){
      var confirmed = confirm("Are your sure you want to delete Record: " + $(this).val()) 

      if (confirmed == true) {
        var json = {
          pk: $(this).val()
        };
        var crf_token = getCookie('csrftoken');

        request = $.ajax({
          url: "/portal/travel/delete/",
          type: "POST",
          headers:{"X-CSRFToken": crf_token},
          data: JSON.stringify(json),
          contentType: "application/json",
        });

        request.done(function (response, textStatus, jqXHR){
          alert("Done!")
          location.reload(true);
        });

        request.fail(function (jqXHR, textStatus, errorThrown){
          alert("Something went wrong!")
          console.error(
            "The following error occurred: "+
            textStatus, errorThrown, jqXHR
          );
        });
      }
    } else { 
      location.replace("/portal/travel/form/" + $(this).val() + "/")
    }
  });
});

function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
      var cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
