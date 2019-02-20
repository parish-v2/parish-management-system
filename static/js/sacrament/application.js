var sponsor_count = 0
function duplicateChildNodes (parentId,container_id){
    var parent = document.getElementById(parentId);
    var parent_clone = parent.cloneNode(true);
    parent_clone.id = "sponsor"+sponsor_count
    var container = document.getElementById(container_id);
    container.appendChild(parent_clone);
    
    // NodeList.prototype.forEach = Array.prototype.forEach;
    //var children = parent_clone.childNodes;
    $(function(){
      // alert($(this).attr('name'));
      // $("#"+parent_clone.id).find('p').find('input').each(function(e){
        // e.attr("name", $(e).attr("name")+"EEEEEEEEEE"); 
      // })
      $("#"+parent_clone.id).find('p').find('input').each(function(element){
        $(element).attr("name",$(element).attr('name')+"EEE"); 
        
      }
      
      //  })

    )});
  sponsor_count += 1;
  }

    
    // });
    
        // $('this p input').attr("id","id_form-"+sponsor_count+"-"+ $(this).attr("id"));
    // })
    
    // $(this).find("input, select").each(function() {
    // $(this).attr("id", currentPrefix + sponsor_count + "_" + $(this).attr("id"));
    // $(this).attr("name", currentPrefix + sponsor_count + "_" + $(this).attr("name"));
    //});
    

    //recursive_rename(sponsor_count,parent_clone)
    // alert("here");
      //children.forEach(function(item){--------------------------
    //      var cln = item.cloneNode(true);
    //      parent_clone.appendChild(cln);
        //item.id = "id_form-"+sponsor_count+"-"+item.id;------------------------
       //});------------------
  // parent.appendChild("<hr>")
  
  
  
//   duplicateChildNodes("container");
