var request;

$(function () {
  $('#travel_table').DataTable({
    "pagingType": "first_last_numbers" 
  });

  $('.dataTables_length').addClass('bs-select');

  $("button").click(function() {
    $("#status").val($(this).text())
    $("#pk").val($(this).val())
    $(".modal").css("display", "block");
  });

  $(document).on("submit", "form", function(e){
    e.preventDefault();

    if (request) {
      request.abort();
    }

    var $form = $(this);
    var $inputs = $form.find("input, select, button, textarea");
    $inputs.prop("disabled", true);

    var json = {
      pk: $("#pk").val(),
      status: $("#status").val(),
      reason: $("#reason").val()
    };
    var crf_token = getCookie('csrftoken');
    alert(JSON.stringify(json))

    request = $.ajax({
      url: "/portal/travel/mgr/change_status/",
      type: "POST",
      headers:{"X-CSRFToken": crf_token},
      data: JSON.stringify(json),
      contentType: "application/json",
    });

    request.done(function (response, textStatus, jqXHR){
      console.log("Hooray, it worked!");
    });

    request.fail(function (jqXHR, textStatus, errorThrown){
      console.error(
        "The following error occurred: "+
        textStatus, errorThrown, jqXHR
      );
    });
    $inputs.prop("disabled", false);

  });

  $("#close").click(function(){
    $(".modal").css("display", "none");
  });

  $(document).keyup(function(e) {
    if (e.key === "Escape") { 
      $(".modal").css("display", "none");
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
