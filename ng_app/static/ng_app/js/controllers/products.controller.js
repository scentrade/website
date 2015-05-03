(function(){
  'use strict';

  angular.module('scentrade.controllers')
    .controller('ProductsController', ProductsController);

  ProductsController.$inject = ['$scope', '$rootScope'];

  function ProductsController($scope, $rootScope){
    $rootScope.bodyClass = 'products';
    $rootScope.title = 'Productos';
  }
})();