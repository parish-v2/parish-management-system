var selected_row_id = 0;
// tables.js: import this when using selectable-table class
$(document).ready(function () {

  
  function select_row(element) {
    if (!$(element).hasClass("selected")) {
      $('.selected').removeClass('selected');
      $(element).addClass('selected');
    } else {
      $(element).removeClass('selected');
    }
    //$(element).attr('style', 'background-color:red;')
  }


  // on-click selectable row
  $('.selectable-table').on('click', '.selectable-row', function () {
    select_row(this);
    selected_row_id = $(this).find("td:first-child").html();
  });
  







});
