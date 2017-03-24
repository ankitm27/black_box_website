$(document).ready(function(){
  /* Every time the window is scrolled ... */
  $(window).scroll(function(){
    /* Check the location of each desired element */
    $('.fadein').each(function(i){
      var top_of_object = $(this).offset().top
      //var bottom_of_object = $(this).offset().top + $(this).outerHeight();
      var top_of_window = $(window).scrollTop() + $(window).height();
      //var bottom_of_window = $(window).scrollTop() + $(window).height();
      if(top_of_window > top_of_object){
        $(this).animate({'opacity':1},1000);
      }
    });
    $('.fadeinimg').each(function(i){
      var top_of_object = $(this).offset().top
      //var bottom_of_object = $(this).offset().top + $(this).outerHeight();
      var top_of_window = $(window).scrollTop() + $(window).height();
      //var bottom_of_window = $(window).scrollTop() + $(window).height();
      if(top_of_window > top_of_object){
        $(this).animate({'opacity':1},2000);
      }
    });
  });
  $(".person").hover(function(){
    $(this).css("-webkit-filter", "grayscale(0%)");
    $(this).css("filter", "grayscale(0%)");
    }, function(){
      $(this).css("-webkit-filter", "grayscale(100%)");
      $(this).css("filter", "grayscale(100%)");
  });
});
