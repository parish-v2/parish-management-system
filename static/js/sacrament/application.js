// String.prototype.replaceAt=function(index, replacement) {
//   return this.substr(0, index) + replacement+ this.substr(index + replacement.length);
// }

// $.fn.replace_name = function(number, name) {
//   this.attr(name, name.replaceAt(5,number));
//   return this;
// };
// function rename(sponsor_count){
//   $("#sponsor"+sponsor_count).find('p').find('input').each(
//     function(){
//       $(this).attr("name", $(this).attr("name").replaceAt(5,sponsor_count+""))
//       // alert($(this).attr('name'))
//     }
//   )
//  }

// var sponsor_count = 1
// function duplicateChildNodes (parentId,container_id){
//     var parent = document.getElementById(parentId);
//     var parent_clone = parent.cloneNode(true);
//     parent_clone.id = "sponsor"+sponsor_count
//     var container = document.getElementById(container_id);
//     container.appendChild(parent_clone);
//     rename(sponsor_count)
//     sponsor_count++;
//   }


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
// function cloneMore(selector, type) {
//   var newElement = $(selector).clone(true);
//   var total = $('#id_' + type + '-TOTAL_FORMS').val();
//   newElement.find(':input').each(function() {
//       var name = $(this).attr('name').replace('-' + (total-1) + '-','-' + total + '-');
//       var id = 'id_' + name;
//       $(this).attr({'name': name, 'id': id}).val('').removeAttr('checked');
//   });
//   newElement.find('label').each(function() {
//       var newFor = $(this).attr('for').replace('-' + (total-1) + '-','-' + total + '-');
//       $(this).attr('for', newFor);
//   });
//   total++;
//   $('#id_' + type + '-TOTAL_FORMS').val(total);
//   $(selector).after(newElement);
// }



$('#input-minister').select2({
    width:"100%",
    ajax: {
      url: "/sacrament/ministers",
      dataType: 'json'
      }
  });

$('#existing').select2({
  placeholder: "Name",
  allowClear: true,
  width:"100%",
  ajax: {
    url: "/sacrament/profiles",
    dataType: 'json'
    }
});

$('#existing').on('select2:unselect', function (e) {
  $("#id_profile-first_name").val("");
  $("#id_profile-middle_name").val("");
  $("#id_profile-last_name").val("");
  $("#id_profile-suffix").val("");
  $("#id_profile-gender").val("");
  $("#id_profile-birthdate").val("");
  $("#id_profile-birthplace").val("");
  $("#id_profile-residence").val("");
  $("#profile_ID").val("");

  $("#id_profile-first_name").removeAttr('readonly');
  $("#id_profile-middle_name").removeAttr('readonly');
  $("#id_profile-last_name").removeAttr('readonly');
  $("#id_profile-suffix").removeAttr('readonly');
  $("#id_profile-gender").removeAttr('readonly');
  $("#id_profile-birthdate").removeAttr('readonly');
  $("#id_profile-birthplace").removeAttr('readonly');
  $("#id_profile-residence").removeAttr('readonly');
})

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
        $("#profile_ID").val(data["id"]);
        
        $("#id_profile-first_name").attr("readonly", "readonly");
        $("#id_profile-middle_name").attr("readonly", "readonly");
        $("#id_profile-last_name").attr("readonly", "readonly");
        $("#id_profile-suffix").attr("readonly", "readonly");
        $("#id_profile-gender").attr("readonly", "readonly");
        $("#id_profile-birthdate").attr("readonly", "readonly");
        $("#id_profile-birthplace").attr("readonly", "readonly");
        $("#id_profile-residence").attr("readonly", "readonly");

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
  placeholder: "Name",
  allowClear: true,
  width:"100%",
  ajax: {
    url: "/sacrament/grooms",
    dataType: 'json'
    }
});

$('#groom_existing').on('select2:unselect', function (e) {
  $("#id_groom-first_name").val("");
  $("#id_groom-middle_name").val("");
  $("#id_groom-last_name").val("");
  $("#id_groom-suffix").val("");
  $("#id_groom-gender").val("");
  $("#id_groom-birthdate").val("");
  $("#id_groom-birthplace").val("");
  $("#id_groom-residence").val("");
  $("#groom_ID").val("");
  $("#id_marriage-groom_father_first_name").val("");
  $("#id_marriage-groom_father_middle_name").val("");
  $("#id_marriage-groom_father_last_name").val("");
  $("#id_marriage-groom_father_suffix").val("");
  $("#id_marriage-groom_mother_first_name").val("");
  $("#id_marriage-groom_mother_middle_name").val("");
  $("#id_marriage-groom_mother_last_name").val("");
  $("#id_marriage-groom_mother_suffix").val("");

  $("#id_groom-first_name").removeAttr('readonly');
  $("#id_groom-middle_name").removeAttr('readonly');
  $("#id_groom-last_name").removeAttr('readonly');
  $("#id_groom-suffix").removeAttr('readonly');
  $("#id_groom-gender").removeAttr('readonly');
  $("#id_groom-birthdate").removeAttr('readonly');
  $("#id_groom-birthplace").removeAttr('readonly');
  $("#id_groom-residence").removeAttr('readonly');
  $("#id_marriage-groom_father_first_name").removeAttr('readonly');
  $("#id_marriage-groom_father_middle_name").removeAttr('readonly');
  $("#id_marriage-groom_father_last_name").removeAttr('readonly');
  $("#id_marriage-groom_father_suffix").removeAttr('readonly');
  $("#id_marriage-groom_mother_first_name").removeAttr('readonly');
  $("#id_marriage-groom_mother_middle_name").removeAttr('readonly');
  $("#id_marriage-groom_mother_last_name").removeAttr('readonly');
  $("#id_marriage-groom_mother_suffix").removeAttr('readonly');
})

$('#groom_existing').on('select2:select', function (e) {
  data = e.params.data;  
  $.ajax({
    url : "/sacrament/profiles/"+data["id"],
    beforeSend: function(xhr){xhr.setRequestHeader("X-CSRFToken", Cookies.get('csrftoken'))},
    type : "GET",
    success : function(json) {
      parsed_json = JSON.parse(json);
      // console.log(parsed_json);
      $("#id_marriage-groom_father_first_name").removeAttr("readonly");
      $("#id_marriage-groom_father_middle_name").removeAttr("readonly");
      $("#id_marriage-groom_father_last_name").removeAttr("readonly");
      $("#id_marriage-groom_father_suffix").removeAttr("readonly");
      $("#id_marriage-groom_mother_first_name").removeAttr("readonly");
      $("#id_marriage-groom_mother_middle_name").removeAttr("readonly");
      $("#id_marriage-groom_mother_last_name").removeAttr("readonly");
      $("#id_marriage-groom_mother_suffix").removeAttr("readonly");

      $("#id_marriage-groom_father_first_name").val('');
      $("#id_marriage-groom_father_middle_name").val('');
      $("#id_marriage-groom_father_last_name").val('');
      $("#id_marriage-groom_father_suffix").val('');
      $("#id_marriage-groom_mother_first_name").val('');
      $("#id_marriage-groom_mother_middle_name").val('');
      $("#id_marriage-groom_mother_last_name").val('');
      $("#id_marriage-groom_mother_suffix").val('');
      
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
            $("#groom_ID").val(groom["id"]);

            $("#id_groom-first_name").attr("readonly", "readonly");
            $("#id_groom-middle_name").attr("readonly", "readonly");
            $("#id_groom-last_name").attr("readonly", "readonly");
            $("#id_groom-suffix").attr("readonly", "readonly");
            $("#id_groom-gender").attr("readonly", "readonly");
            $("#id_groom-birthdate").attr("readonly", "readonly");
            $("#id_groom-birthplace").attr("readonly", "readonly");
            $("#id_groom-residence").attr("readonly", "readonly");
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

            $("#id_marriage-groom_father_first_name").attr("readonly", "readonly");
            $("#id_marriage-groom_father_middle_name").attr("readonly", "readonly");
            $("#id_marriage-groom_father_last_name").attr("readonly", "readonly");
            $("#id_marriage-groom_father_suffix").attr("readonly", "readonly");
            $("#id_marriage-groom_mother_first_name").attr("readonly", "readonly");
            $("#id_marriage-groom_mother_middle_name").attr("readonly", "readonly");
            $("#id_marriage-groom_mother_last_name").attr("readonly", "readonly");
            $("#id_marriage-groom_mother_suffix").attr("readonly", "readonly");
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
  placeholder: "Name",
  allowClear: true,
  width:"100%",
  ajax: {
    url: "/sacrament/brides",
    dataType: 'json'
    }
});

$('#bride_existing').on('select2:unselect', function (e) {
  $("#id_bride-first_name").val("");
  $("#id_bride-middle_name").val("");
  $("#id_bride-last_name").val("");
  $("#id_bride-suffix").val("");
  $("#id_bride-gender").val("");
  $("#id_bride-birthdate").val("");
  $("#id_bride-birthplace").val("");
  $("#id_bride-residence").val("");
  $("#bride_ID").val("");
  $("#id_marriage-bride_father_first_name").val("");
  $("#id_marriage-bride_father_middle_name").val("");
  $("#id_marriage-bride_father_last_name").val("");
  $("#id_marriage-bride_father_suffix").val("");
  $("#id_marriage-bride_mother_first_name").val("");
  $("#id_marriage-bride_mother_middle_name").val("");
  $("#id_marriage-bride_mother_last_name").val("");
  $("#id_marriage-bride_mother_suffix").val("");

  $("#id_bride-first_name").removeAttr('readonly');
  $("#id_bride-middle_name").removeAttr('readonly');
  $("#id_bride-last_name").removeAttr('readonly');
  $("#id_bride-suffix").removeAttr('readonly');
  $("#id_bride-gender").removeAttr('readonly');
  $("#id_bride-birthdate").removeAttr('readonly');
  $("#id_bride-birthplace").removeAttr('readonly');
  $("#id_bride-residence").removeAttr('readonly');
  $("#id_marriage-bride_father_first_name").removeAttr('readonly');
  $("#id_marriage-bride_father_middle_name").removeAttr('readonly');
  $("#id_marriage-bride_father_last_name").removeAttr('readonly');
  $("#id_marriage-bride_father_suffix").removeAttr('readonly');
  $("#id_marriage-bride_mother_first_name").removeAttr('readonly');
  $("#id_marriage-bride_mother_middle_name").removeAttr('readonly');
  $("#id_marriage-bride_mother_last_name").removeAttr('readonly');
  $("#id_marriage-bride_mother_suffix").removeAttr('readonly');
})

$('#bride_existing').on('select2:select', function (e) {
  data = e.params.data;
  $.ajax({
    url : "/sacrament/profiles/"+data["id"],
    beforeSend: function(xhr){xhr.setRequestHeader("X-CSRFToken", Cookies.get('csrftoken'))},
    type : "GET",
    success : function(json) {
        parsed_json = JSON.parse(json);
        // console.log(parsed_json);
        $("#id_marriage-bride_father_first_name").removeAttr('readonly');
        $("#id_marriage-bride_father_middle_name").removeAttr('readonly');
        $("#id_marriage-bride_father_last_name").removeAttr('readonly');
        $("#id_marriage-bride_father_suffix").removeAttr('readonly');
        $("#id_marriage-bride_mother_first_name").removeAttr('readonly');
        $("#id_marriage-bride_mother_middle_name").removeAttr('readonly');
        $("#id_marriage-bride_mother_last_name").removeAttr('readonly');
        $("#id_marriage-bride_mother_suffix").removeAttr('readonly');

        $("#id_marriage-bride_father_first_name").val('');
        $("#id_marriage-bride_father_middle_name").val('');
        $("#id_marriage-bride_father_last_name").val('');
        $("#id_marriage-bride_father_suffix").val('');
        $("#id_marriage-bride_mother_first_name").val('');
        $("#id_marriage-bride_mother_middle_name").val('');
        $("#id_marriage-bride_mother_last_name").val('');
        $("#id_marriage-bride_mother_suffix").val('');
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
              $("#bride_ID").val(bride["id"]);

              $("#id_bride-first_name").attr("readonly", "readonly");
              $("#id_bride-middle_name").attr("readonly", "readonly");
              $("#id_bride-last_name").attr("readonly", "readonly");
              $("#id_bride-suffix").attr("readonly", "readonly");
              $("#id_bride-gender").attr("readonly", "readonly");
              $("#id_bride-birthdate").attr("readonly", "readonly");
              $("#id_bride-birthplace").attr("readonly", "readonly");
              $("#id_bride-residence").attr("readonly", "readonly");
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

              $("#id_marriage-bride_father_first_name").attr("readonly", "readonly");
              $("#id_marriage-bride_father_middle_name").attr("readonly", "readonly");
              $("#id_marriage-bride_father_last_name").attr("readonly", "readonly");
              $("#id_marriage-bride_father_suffix").attr("readonly", "readonly");
              $("#id_marriage-bride_mother_first_name").attr("readonly", "readonly");
              $("#id_marriage-bride_mother_middle_name").attr("readonly", "readonly");
              $("#id_marriage-bride_mother_last_name").attr("readonly", "readonly");
              $("#id_marriage-bride_mother_suffix").attr("readonly", "readonly");
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
