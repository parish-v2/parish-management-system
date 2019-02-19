 
  $(document).ready(function() {

    var selected_id = 0;

    function change_bg(element) {


      if(!$(element).hasClass("selected")){
        $('.selected').removeClass('selected');
        $(element).addClass('selected');
      } else {
        $(element).removeClass('selected');
      }

      //$(element).attr('style', 'background-color:red;')
    }

    $('.selectable-table').on('click', '.selectable-row', function() {
      
      change_bg(this);
      var v = $(this).find("td:first-child");
      
      
    });

    
 
  });
