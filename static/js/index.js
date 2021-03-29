$(document).ready(function (){

    $(".mainMenu .listMenu").click(function (){
        $(".mainMenu .listMenu").not(this).removeClass('active');
        $(this).toggleClass('active');
    });

});

