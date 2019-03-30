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
      console.log(res);
      $("#input-first-name").val(res.first_name);
      $("#input-middle-name").val(res.middle_name);
      $("#input-last-name").val(res.last_name);
      $("#input-suffix").val(res.suffix);
      $("#input-gender").val(res.gender),
      $("#input-status").val(res.status);
      $("#input-birthdate").val(res.birthdate),
      $("#input-birthplace").val(res.birthplace),
      $("#input-legitimacy").val(res.legitimacy),
      $("#input-minister").select2("trigger", "select", {
          data: { id: res.minister, text: res.minister_name}
      });
        //parent details - mother
      $("#input-mother-first-name").val(res.mother_first_name),
      $("#input-mother-middle-name").val(res.mother_middle_name),
      $("#input-mother-last-name").val(res.mother_last_name),
      $("#input-mother-suffix").val(res.mother_suffix),
        //parent details - father,
      $("#input-father-first-name").val(res.father_first_name),
      $("#input-father-middle-name").val(res.father_middle_name),
      $("#input-father-last-name").val(res.father_last_name),
      $("#input-father-suffix").val(res.father_suffix),
      $("#registry-input").val(res.registry_number);
      $("#record-input").val(res.record_number);
      $("#page-input").val(res.page_number);
    },
    error: function(xhr, textStatus, errorThrown) {
        console.log('error');
    }
  }
);
}

function getPaymentData(sacrament) {
  // clear the payment grid,
  // to be replaced with new values
  $("#jsGrid").jsGrid("option", "data", []);
  $.ajax({
    url: "/sacrament/post/paymentdetails",
    beforeSend: function(xhr){xhr.setRequestHeader("X-CSRFToken", Cookies.get('csrftoken'))},
    type: 'POST',
    data : { 
      "id" : selected_row_id,
      "sacrament" : "baptism"
    },
    success: function(res){
      if (res.sponsors.length === 0) {
          $("#payments-body").html(
              `
                          <tr scope="row" class="us even">
                                  <td colspan="2" class="text-center">No items to show.</td>
                          </tr>
                      `
          );
      } else {
          last_id = selected_row_id;
          data.sponsors.forEach(function (element) {
              $("#sponsors-body").html(
                  $("#sponsors-body").html() + `
                          <tr scope="row" class="us even">
                                  <td>${element.name}</td>
                                  <td class="status">${element.residence}</td>
                          </tr>
                      `
              )
          });
      }
    },
    error: function(xhr, textStatus, errorThrown) {
        console.log('error');
    }
  });
  get_payment_history(sacrament);
}

function updateRegistry() {
    error=false;
    $.ajax({
      url : "/sacrament/post/update", // the endpoint
      beforeSend: function(xhr){xhr.setRequestHeader("X-CSRFToken", Cookies.get('csrftoken'))},
      type : "POST", // http method
      data : { 
        id : selected_row_id,
        // profile details
        first_name: $("#input-first-name").val(),
        middle_name: $("#input-middle-name").val(),
        last_name: $("#input-last-name").val(),
        suffix: $("#input-suffix").val(),
        gender: $("#input-gender").val(),
        birthdate: $("#input-birthdate").val(),
        birthplace: $("#input-birthplace").val(),
        legitimacy: $("#input-legitimacy").val(),
        minister: $("#input-minister").val(),
        status: $("#input-status").val(),
        //parent details - mother
        mother_first_name: $("#input-mother-first-name").val(),
        mother_middle_name: $("#input-mother-middle-name").val(),
        mother_last_name: $("#input-mother-last-name").val(),
        mother_suffix: $("#input-mother-suffix").val(),
        //parent details - father,
        father_first_name: $("#input-father-first-name").val(),
        father_middle_name: $("#input-father-middle-name").val(),
        father_last_name: $("#input-father-last-name").val(),
        father_suffix: $("#input-father-suffix").val(),
        // registry details
        registry_number : $("#registry-input").val(),
        record_number : $("#record-input").val(),
        page_number : $("#page-input").val(),
        sacrament : "baptism"
      }, // data sent with the post request

      // handle a successful response
      success : function(json) {
          $('#post-text').val(''); // remove the value from the input
          console.log(json); // log the returned json to the console
          console.log("success"); // another sanity check
          //toastr.info("Updated!")
          location.reload();
      },

      // handle a non-successful response
      error : function(xhr,errmsg,err) {
          $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
              " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
          console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
          error=true;
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
  
  $('#input-minister').select2({
    width:"100%",
    dropdownParent: $('#approve-modal'),
    ajax: {
      url: "/sacrament/ministers",
      dataType: 'json'
      }
  });

});


function get_payment_history(sacrament) {
  $.ajax({
    type: 'GET',
    url: '/finance/payments/sacrament-payment-history',
    contentType: 'application/json;',
    dataType: 'json',
    data: {
      id:selected_row_id,
      sacrament:sacrament
    },
    success: function(res){
      console.log(res);
      res.invoices.forEach(function(invoice){
        $("#jsGrid").jsGrid("insertItem", { existing:true, receivedBy: invoice.received_by, AmountPaid: invoice.amount_paid, Discount: invoice.discount, or_no:invoice.or_no})
      });
    },
    error: function(xhr, textStatus, errorThrown) {
        console.log('error');
    }
});
}
