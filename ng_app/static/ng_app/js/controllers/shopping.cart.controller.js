(function(){
  'use strict';

  angular.module('scentrade.controllers')
    .controller('ShoppingCartController', ShoppingCartController);

  ShoppingCartController.$inject = ['$scope', '$http', 'API'];

  function ShoppingCartController($scope, $http, API){
    var vm = this;
    vm.fetchCart = fetchCart;
    // fetch the first time
    vm.fetchCart();

    // Communicating between controllers
    // http://stackoverflow.com/a/26060511/923323
    $scope.$on('cart.update', function(){
      vm.fetchCart();
    });

    // -----------------------------------------------------------------------------

    function fetchCart(){
      $http.get(API.makeURL('cart'))
        .success(function(response, status){
          vm.cart = response;
        });
    }
  }
})();