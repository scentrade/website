(function($){

  $(function(){

    var $header = $('header#scentrade-header');
    var $nav = $header.find('nav.navbar');
    var $navTrigger = $nav.find('a.nav-trigger');

    $navTrigger.on('click', function(event){
      event.preventDefault();
      $nav.toggleClass('nav-active');
    });

    $nav.on('click', 'ul.navbar-nav a', function(){
      if( $nav.hasClass('nav-active') ){
        setTimeout(function(){
          $nav.removeClass('nav-active');
        }, 100);
      }
    });

  });

})(jQuery);