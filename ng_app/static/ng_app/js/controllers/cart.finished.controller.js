(function(){
  'use strict';

  angular.module('scentrade.controllers')
    .controller('CartFinishedController', CartFinishedController);

  CartFinishedController.$inject = ['$scope', '$http', '$routeParams', 'API'];

  function CartFinishedController($scope, $http, $routeParams, API){
    var vm = this;

    // -----------------------------------------------------------------------------

    console.log($routeParams);

    $http.get(API.makeURL('store/purchases/' + $routeParams['purchase']))
      .success(function(response){
        response.cart = JSON.parse(response.cart);
        vm.purchase = response;
      });
  }
})();