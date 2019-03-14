function updateElementIndex(el, prefix, ndx) {
    console.log("AAA");
    var id_regex = new RegExp('(' + prefix + '-\\d+)'); //creates regex of "(form-0)(form-1).."
    //console.log(id_regex);
    var replacement = prefix + '-' + ndx; //makes string containing form-0, form-1 ...
    console.log(replacement);
    if ($(el).attr("for")) $(el).attr("for", $(el).attr("for").replace(id_regex, replacement));//replaces for in label
    if (el.id) el.id = el.id.replace(id_regex, replacement); //replaces id
    if (el.name) el.name = el.name.replace(id_regex, replacement); //replaces name
}

function addForm(btn, prefix) {
    var formCount = parseInt($('#id_' + prefix + '-TOTAL_FORMS').val());
    var row = $('.dynamic-form:first').clone(true).get(0);//select 1st dynamic form class/ clone it and its children / get the 1st element(the main container)
    //console.log(row);
    var a = $(row).removeAttr('id').insertAfter($('.dynamic-form:last'));//remove id / insert next to dynamic-formset class
    //console.log(a);
    $(row).children().not(':last').each(function() { //select all children of row except for last, then iterate them all
        //console.log("A");
        updateElementIndex(this, prefix, formCount); //updates id of newly created elements
        $(this).val("");
        // console.log(this);
    });
    $(row).find('.delete-row').click(function() {
        deleteForm(this, prefix);
    });
    $('#id_' + prefix + '-TOTAL_FORMS').val(formCount + 1);
    return false;
}

function deleteForm(btn, prefix) {
    $(btn).parents('.dynamic-form').remove();
    var forms = $('.dynamic-form');
    $('#id_' + prefix + '-TOTAL_FORMS').val(forms.length);
    for (var i=0, formCount=forms.length; i<formCount; i++) {
        $(forms.get(i)).children().not(':last').children().each(function() {
            updateElementIndex(this, prefix, i);
        });
    }
    return false;
}