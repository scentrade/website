(function(){
  'use strict';

  angular.module('scentrade.controllers')
    .controller('HomeController', HomeController);

  HomeController.$inject = ['$scope', '$rootScope'];

  function HomeController($scope, $rootScope){
    $rootScope.bodyClass = 'home';
    $rootScope.title = 'Hogar';
  }
})();