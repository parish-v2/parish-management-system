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
function cloneMore(selector, type) {
  var newElement = $(selector).clone(true);
  var total = $('#id_' + type + '-TOTAL_FORMS').val();
  newElement.find(':input').each(function() {
      var name = $(this).attr('name').replace('-' + (total-1) + '-','-' + total + '-');
      var id = 'id_' + name;
      $(this).attr({'name': name, 'id': id}).val('').removeAttr('checked');
  });
  newElement.find('label').each(function() {
      var newFor = $(this).attr('for').replace('-' + (total-1) + '-','-' + total + '-');
      $(this).attr('for', newFor);
  });
  total++;
  $('#id_' + type + '-TOTAL_FORMS').val(total);
  $(selector).after(newElement);
}

$('#existing').select2({
  width:"100%",
  ajax: {
    url: "/sacrament/profiles",
    dataType: 'json'
    }
});

$('#existing').on('select2:select', function (e) {
  data = e.params.data;
  $.ajax({
    url : "/sacrament/profiles/"+data["id"],
    beforeSend: function(xhr){xhr.setRequestHeader("X-CSRFToken", Cookies.get('csrftoken'))},
    type : "GET",
    success : function(json) {
        profile = JSON.parse(json)[0]["fields"];
        $("#id_profile-first_name").val(profile["first_name"]);
        $("#id_profile-middle_name").val(profile["middle_name"]);
        $("#id_profile-last_name").val(profile["last_name"]);
        $("#id_profile-suffix").val(profile["suffix"]);
        $("#id_profile-gender").val(profile["gender"]);
        $("#id_profile-birthdate").val(profile["birthdate"]);
        $("#id_profile-birthplace").val(profile["birthplace"]);
        $("#id_profile-residence").val(profile["residence"]);


    },

    // handle a non-successful response
    error : function(xhr,errmsg,err) {
        $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
            " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
        console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
    }
  });
});

$('#groom_existing').select2({
  width:"100%",
  ajax: {
    url: "/sacrament/profiles",
    dataType: 'json'
    }
});

$('#groom_existing').on('select2:select', function (e) {
  $("#id_groom-first_name").val("");
  $("#id_groom-middle_name").val("");
  $("#id_groom-last_name").val("");
  $("#id_groom-suffix").val("");
  $("#id_groom-gender").val("");
  $("#id_groom-birthdate").val("");
  $("#id_groom-birthplace").val("");
  $("#id_groom-residence").val("");
  $("#id_marriage-groom_father_first_name").val("");
  $("#id_marriage-groom_father_middle_name").val("");
  $("#id_marriage-groom_father_last_name").val("");
  $("#id_marriage-groom_father_suffix").val("");
  $("#id_marriage-groom_mother_first_name").val("");
  $("#id_marriage-groom_mother_middle_name").val("");
  $("#id_marriage-groom_mother_last_name").val("");
  $("#id_marriage-groom_mother_suffix").val("");
  data = e.params.data;
  $.ajax({
    url : "/sacrament/profiles/"+data["id"],
    beforeSend: function(xhr){xhr.setRequestHeader("X-CSRFToken", Cookies.get('csrftoken'))},
    type : "GET",
    success : function(json) {
      parsed_json = JSON.parse(json);
      console.log(parsed_json);
      parsed_json.forEach(function(json){
          if(json["model"] == "sacrament.profile"){
            groom = json["fields"];
            $("#id_groom-first_name").val(groom["first_name"]);
            $("#id_groom-middle_name").val(groom["middle_name"]);
            $("#id_groom-last_name").val(groom["last_name"]);
            $("#id_groom-suffix").val(groom["suffix"]);
            $("#id_groom-gender").val(groom["gender"]);
            $("#id_groom-birthdate").val(groom["birthdate"]);
            $("#id_groom-birthplace").val(groom["birthplace"]);
            $("#id_groom-residence").val(groom["residence"]);
          }
          else if(json["model"] == "sacrament.baptism"){
            baptism = json["fields"];
            $("#id_marriage-groom_father_first_name").val(baptism["father_first_name"]);
            $("#id_marriage-groom_father_middle_name").val(baptism["father_last_name"]);
            $("#id_marriage-groom_father_last_name").val(baptism["father_middle_name"]);
            $("#id_marriage-groom_father_suffix").val(baptism["father_suffix"]);
            $("#id_marriage-groom_mother_first_name").val(baptism["mother_first_name"]);
            $("#id_marriage-groom_mother_middle_name").val(baptism["mother_last_name"]);
            $("#id_marriage-groom_mother_last_name").val(baptism["mother_middle_name"]);
            $("#id_marriage-groom_mother_suffix").val(baptism["mother_suffix"]);
          }
      })
  },

    // handle a non-successful response
    error : function(xhr,errmsg,err) {
        $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
            " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
        console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
    }
  });
});


$('#bride_existing').select2({
  width:"100%",
  ajax: {
    url: "/sacrament/profiles",
    dataType: 'json'
    }
});

$('#bride_existing').on('select2:select', function (e) {
  $("#id_bride-first_name").val("");
  $("#id_bride-middle_name").val("");
  $("#id_bride-last_name").val("");
  $("#id_bride-suffix").val("");
  $("#id_bride-gender").val("");
  $("#id_bride-birthdate").val("");
  $("#id_bride-birthplace").val("");
  $("#id_bride-residence").val("");
  $("#id_marriage-bride_father_first_name").val("");
  $("#id_marriage-bride_father_middle_name").val("");
  $("#id_marriage-bride_father_last_name").val("");
  $("#id_marriage-bride_father_suffix").val("");
  $("#id_marriage-bride_mother_first_name").val("");
  $("#id_marriage-bride_mother_middle_name").val("");
  $("#id_marriage-bride_mother_last_name").val("");
  $("#id_marriage-bride_mother_suffix").val("");
  data = e.params.data;
  $.ajax({
    url : "/sacrament/profiles/"+data["id"],
    beforeSend: function(xhr){xhr.setRequestHeader("X-CSRFToken", Cookies.get('csrftoken'))},
    type : "GET",
    success : function(json) {
        parsed_json = JSON.parse(json);
        console.log(parsed_json);
        parsed_json.forEach(function(json){
            if(json["model"] == "sacrament.profile"){
              bride = json["fields"];
              $("#id_bride-first_name").val(bride["first_name"]);
              $("#id_bride-middle_name").val(bride["middle_name"]);
              $("#id_bride-last_name").val(bride["last_name"]);
              $("#id_bride-suffix").val(bride["suffix"]);
              $("#id_bride-gender").val(bride["gender"]);
              $("#id_bride-birthdate").val(bride["birthdate"]);
              $("#id_bride-birthplace").val(bride["birthplace"]);
              $("#id_bride-residence").val(bride["residence"]);
            }
            else if(json["model"] == "sacrament.baptism"){
              baptism = json["fields"];
              $("#id_marriage-bride_father_first_name").val(baptism["father_first_name"]);
              $("#id_marriage-bride_father_middle_name").val(baptism["father_last_name"]);
              $("#id_marriage-bride_father_last_name").val(baptism["father_middle_name"]);
              $("#id_marriage-bride_father_suffix").val(baptism["father_suffix"]);
              $("#id_marriage-bride_mother_first_name").val(baptism["mother_first_name"]);
              $("#id_marriage-bride_mother_middle_name").val(baptism["mother_last_name"]);
              $("#id_marriage-bride_mother_last_name").val(baptism["mother_middle_name"]);
              $("#id_marriage-bride_mother_suffix").val(baptism["mother_suffix"]);
            }
        })
    },

    // handle a non-successful response
    error : function(xhr,errmsg,err) {
        $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
            " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
        console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
    }
  });
});