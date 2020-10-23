    var form_hide = $('.form_hide');
    var form_ug = $('.form_ug');
    form_hide.hide();
    var checkB = document.querySelector("input[name=checkB]");
    checkB.addEventListener('change', function() {
        if(this.checked){
            form_hide.hide();
            form_ug.show();
        }
        else{
            form_hide.show();
            form_ug.hide();
        }


    });