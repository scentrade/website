(function(){
  'use strict';

  angular.module('scentrade.controllers')
    .controller('CartFinishedController', CartFinishedController);

  CartFinishedController.$inject = ['$scope', '$http', '$routeParams', 'API'];

  function CartFinishedController($scope, $http, $routeParams, API){
    var vm = this;

    // -----------------------------------------------------------------------------

    $http.get(API.makeURL('store/purchases/' + $routeParams['purchase']))
      .success(function(response){
        response.cart = JSON.parse(response.cart);
        vm.purchase = response;
      });

    $http.post(API.makeURL('payment-email'), {'purchase': $routeParams['purchase']})
      .success(function(response){

      });
  }
})();