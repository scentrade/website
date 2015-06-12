(function(){
  'use strict';

  angular.module('scentrade.controllers')
    .controller('AboutUsController', AboutUsController);

  AboutUsController.$inject = ['$scope', '$rootScope'];

  function AboutUsController($scope, $rootScope){
    $rootScope.bodyClass = 'about-us';
    $rootScope.title = 'Nosotros';
  }
})();