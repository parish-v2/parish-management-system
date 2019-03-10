// Submit post on submit

function getRegistryData() {
  $.ajax({
    url: "/sacrament/post/requestregistrynumber",
    beforeSend: function(xhr){xhr.setRequestHeader("X-CSRFToken", Cookies.get('csrftoken'))},
    type: 'POST',
    data : { 
      "id" : selected_row_id,
      "sacrament" : "baptism"
    },
    success: function(res){
      console.log("registry_number: "+res.registry_number);
      console.log("recordNumber: "+res.record_number);
      console.log("page_numer: "+res.page_number);

      $("#input-first-name").val(res.first_name);
      $("#input-middle-name").val(res.middle_name);
      $("#input-last-name").val(res.last_name);
      $("#input-suffix").val(res.suffix);

      $("#registry-input").val(res.registry_number);
      $("#record-input").val(res.record_number);
      $("#page-input").val(res.page_number);
    },
    error: function(xhr, textStatus, errorThrown) {
        console.log('error');
    }
});
}

function updateRegistry() {
  

    var id = selected_row_id;
    var registry_number = $("#registry-input").val();
    var record_number = $("#record-input").val();
    var page_number = $("#page-input").val();

    $.ajax({
      url : "/sacrament/post/", // the endpoint
      beforeSend: function(xhr){xhr.setRequestHeader("X-CSRFToken", Cookies.get('csrftoken'))},
      type : "POST", // http method
      data : { 
        id : id,
        registry_number : registry_number,
        record_number : record_number,
        page_number : page_number,
        sacrament : "baptism"
      }, // data sent with the post request

      // handle a successful response
      success : function(json) {
          $('#post-text').val(''); // remove the value from the input
          console.log(json); // log the returned json to the console
          console.log("success"); // another sanity check
          //window.location.reload();
      },

      // handle a non-successful response
      error : function(xhr,errmsg,err) {
          $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
              " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
          console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
      }
  });
}


function sendAjax(successCallback, from) {
  var urli = site+"/sacrament/post/"+from+"/"+selected_row_id;
  console.log(urli);
  $.ajax({
    type: 'POST',
    url: urli,
    beforeSend: function(xhr){xhr.setRequestHeader("X-CSRFToken", Cookies.get('csrftoken'))},
    contentType: 'application/json;',
    dataType: 'json',
    success: function(res){response_text=res;successCallback()},
    error: function(xhr, textStatus, errorThrown) {
        console.log('error');
    }
});
}


var selected_row_id = 1;
// tables.js: import this when using selectable-table class
$(document).ready(function () {

  $(".selectable-table tbody tr:first-child").addClass("selected");
  
  function select_row(element,dclick) {
    if (!$(element).hasClass("selected")||dclick) {
      $('.selected').removeClass('selected');
      $(element).addClass('selected');
      $("#open-record-btn").prop('disabled', false);
      selected_row_id = $(element).find("td:first-child").html();

    } else {
      
        $(element).removeClass('selected');
        selected_row_id=-1;
        $("#open-record-btn").prop('disabled', true);
      
      
    }
    //$(element).attr('style', 'background-color:red;')
  }


  // on-click selectable row
  $('.selectable-table').on('click', '.selectable-row', function () {
    select_row(this);
    
    console.log("selected_row_id: "+selected_row_id);
  });

  $('.selectable-table').on('dblclick', '.selectable-row', function () {
    select_row(this, true);
    $("#open-record-btn").trigger('click');
  });
  
  $('#ministers').select2({
    ajax: {
      url: site+"/sacrament/ministers",
      dataType: 'json'
      // Additional AJAX parameters go here; see the end of this chapter for the full code of this example
    }
  });






});
