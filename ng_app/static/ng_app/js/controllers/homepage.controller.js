(function(){
  'use strict';

  angular.module('scentrade.controllers')
    .controller('HomePageController', HomePageController);

  HomePageController.$inject = ['$scope', '$rootScope'];

  function HomePageController($scope, $rootScope){
    $rootScope.bodyClass = 'homepage';
    $rootScope.title = 'Inicio';
  }
})();