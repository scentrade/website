(function(){
  $(function(){
    $(window).on('scroll', function(){
      if( $('div.reveal-items-container:in-viewport').length > 0 ){
        $('.reveal-item').each(function(index){
          var $this = $(this);
          setTimeout(function(){
            $this.addClass('reveal');
          }, 400 * index);
        });
      } else {
        $('.reveal-item').removeClass('reveal');
      }
    });

    var $body = $('body');

    $body.on('click', 'a#open-button', function(event){
      event.preventDefault();
      $('section#free-trial').addClass('open');
    });

    var closeTimeout;

    $body.on('mouseleave', 'section#free-trial', function(){
      var $section = $(this);
      closeTimeout = window.setTimeout(function(){
        $section.removeClass('open');
      }, 1000);
    });

    $body.on('mousemove', 'section#free-trial', function(){
      window.clearTimeout(closeTimeout);
    });
  });
})();