String.prototype.replaceAt=function(index, replacement) {
  return this.substr(0, index) + replacement+ this.substr(index + replacement.length);
}

$.fn.replace_name = function(number, name) {
  this.attr(name, name.replaceAt(5,number));
  return this;
};
function rename(sponsor_count){
  $("#sponsor"+sponsor_count).find('p').find('input').each(
    function(){
      $(this).attr("name", $(this).attr("name").replaceAt(5,sponsor_count+""))
      // alert($(this).attr('name'))
    }
  )
 }

var sponsor_count = 1
function duplicateChildNodes (parentId,container_id){
    var parent = document.getElementById(parentId);
    var parent_clone = parent.cloneNode(true);
    parent_clone.id = "sponsor"+sponsor_count
    var container = document.getElementById(container_id);
    container.appendChild(parent_clone);
    rename(sponsor_count)
    sponsor_count++;
  }


//   function cloneMore(selector, type) {
//     var newElement = $(selector).clone(true);
//     var total = $('#id_' + type + '-TOTAL_FORMS').val();
//     newElement.find(':input').each(function() {
//         var name = $(this).attr('name').replace('-' + (total-1) + '-','-' + total + '-');
//         var id = 'id_' + name;
//         $(this).attr({'name': name, 'id': id}).val('').removeAttr('checked');
//     });
//     newElement.find('label').each(function() {
//         var newFor = $(this).attr('for').replace('-' + (total-1) + '-','-' + total + '-');
//         $(this).attr('for', newFor);
//     });
//     total++;
//     $('#id_' + type + '-TOTAL_FORMS').val(total);
//     $(selector).after(newElement);
// }
