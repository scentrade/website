(function($){

  $(function(){
    var offset = 50;

    /*if( $('body').hasClass('homepage') ){
      offset = $('section#homepage-hero').outerHeight() - $('header#scentrade-header nav.navbar').outerHeight();
    }

    $(window).on('resize', function(){
      if( $('body').hasClass('homepage') ){
        offset = $('section#homepage-hero').outerHeight() - $('header#scentrade-header nav.navbar').outerHeight();
      }
    });*/

    $(window).on('scroll', function(){
      if( $(window).scrollTop() > offset ){
        $('header nav.navbar').addClass('scrolling');
      } else {
        $('header nav.navbar').removeClass('scrolling');
      }
    });

    var $scentradeHeader = $('header#scentrade-header');

    $scentradeHeader.on('click', '.checkout__button', function(event){
      event.preventDefault();
      $scentradeHeader.find('.checkout').addClass('checkout--active');
    });

    $scentradeHeader.on('click', '.checkout__cancel', function(event){
      event.preventDefault();
      $scentradeHeader.find('.checkout').removeClass('checkout--active');
    });

  });

})(jQuery);