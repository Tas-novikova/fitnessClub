/*$(document).ready(function() {
  var button = $('#button-up');
  $(window).scroll (function () {
    if ($(this).scrollTop () > 300) {
      button.fadeIn();
    } else {
      button.fadeOut();
    }
});
button.on('click', function(){
$('body, html').animate({
scrollTop: 0
}, 800);
return false;
});
});

});

});*/
window.addEventListener('load', function(){
    window.onscroll = function() {scrollFunction()};

    function scrollFunction() {
        if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50){
            document.querySelector('.topBtn').style.display = 'block';
        }else{
            document.querySelector('.topBtn').style.display = 'none';
        }
    }

    // scroll body to 0px on click
    function topFunction() {
        document.body.scrollTop = 0; // for Safari
        document.documentElement.scrollTop = 0;
    }
})