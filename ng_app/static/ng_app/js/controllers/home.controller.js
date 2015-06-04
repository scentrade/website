(function(){
  'use strict';

  angular.module('scentrade.controllers')
    .controller('HomeController', HomeController);

  HomeController.$inject = ['$scope', '$rootScope', '$window'];

  function HomeController($scope, $rootScope, $window){
    $rootScope.bodyClass = 'home';
    $rootScope.title = 'Hogar';

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