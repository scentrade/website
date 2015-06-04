(function(){
  'use strict';

  angular.module('scentrade.controllers')
    .controller('AboutUsController', AboutUsController);

  AboutUsController.$inject = ['$scope', '$rootScope', '$window'];

  function AboutUsController($scope, $rootScope, $window){
    $rootScope.bodyClass = 'about-us';
    $rootScope.title = 'Nosotros';

    $($window).on('scroll', function(){
      if( $('div.reveal-items-container:in-viewport').length > 0 ){
        $('.reveal-item').each(function(index){
          var $this = $(this);
          setTimeout(function(){
            $this.addClass('reveal');
          }, 400 * index);
        });
      }
    });
  }
})();