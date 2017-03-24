function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$(document).ready(function(){
  $('.check').click(function(){
    var id = this.id;
    var userid = "#" + id + "user";
    var emiid = "#" + id + "emi";
    var subid = "#" + id + "sub";
    var csrftoken = getCookie('csrftoken');
    user = $(userid).val();
    emi = $(emiid).val();
    sub = $(subid).val();
    if(emi.length != 15){
      alert("Your emi number must equal to 15!");
      $(emiid).focus();
    }else{
      $.ajax({
				type: 'POST',
				url :'/individual_activation/',
				data: {
					username: user,
          emi: emi,
          sub: sub,
					csrfmiddlewaretoken: csrftoken,
				},
				success: function(data){
          alert("Sucsess")
          location.reload();
				}
			});
    }
  });
  $('#activate_all').click(function(){
    $('.emi').each(function(i){
      var emi = $(this).val();
      if(emi.length != 15){
        alert("Your emi number must equal to 15!");
        $("#form").submit(function(e){
          e.preventDefault();
        });
        $(this).focus();
        return false;
      }
    });
  });
});
