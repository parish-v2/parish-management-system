var selected_row_id = 1;
// tables.js: import this when using selectable-table class
$(document).ready(function () {
  $("tbody tr:first-child").addClass("selected");
  
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
  







});
