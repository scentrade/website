(function(){
  'use strict';

  angular.module('scentrade.directives')
    .directive('owlCarousel', owlCarousel);

  function owlCarousel(){
    var directive = {
      restrict: 'EA',
      scope: {
        // the same as the directive name so it works as the
        // attribute directive initializer but the background image at
        // the same time
        source: '=',
        owlCarousel: '=',
        items: '=',
        itemsDesktop: '=',
        itemsMobile: '=',
        autoPlay: '=',
      },
      link: link,
      templateUrl: 'partials/directives/owl-carousel.html'
    };

    return directive;

    function link(scope, element, attrs){
      scope.$watch('source', function(data){
        if( data ){
          element.owlCarousel({
            items: scope['items'],
            itemsDesktop: scope['itemsDesktop'],
            itemsMobile: scope['itemsMobile'],
            autoPlay: scope['autoPlay'],
          });
        }
      });
    }
  }
})();