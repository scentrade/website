(function(){
  'use strict';

  angular.module('scentrade.controllers')
    .controller('HomeController', HomeController);

  HomeController.$inject = ['$scope', '$rootScope'];

  function HomeController($scope, $rootScope){
    $rootScope.bodyClass = 'home';
    $rootScope.title = 'Hogar';
    $rootScope.metaDescription = 'Conozca los productos y servicios que lo harán vivir experiencias olfativas únicas en su  hogar y en su vida cotidiana.';
  }
})();