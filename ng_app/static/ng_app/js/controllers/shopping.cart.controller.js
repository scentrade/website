(function(){
  'use strict';

  angular.module('scentrade.controllers')
    .controller('ShoppingCartController', ShoppingCartController);

  ShoppingCartController.$inject = ['$scope', '$http', 'API', '$timeout'];

  function ShoppingCartController($scope, $http, API, $timeout){
    var vm = this;
    vm.fetchCart = fetchCart;
    // fetch the first time
    vm.fetchCart();

    // Communicating between controllers
    // http://stackoverflow.com/a/26060511/923323
    $scope.$on('cart.update', function(){
      vm.fetchCart();
      angular.element('div.checkout').addClass('updated');
      $timeout(function(){
        angular.element('div.checkout').removeClass('updated');
      }, 500);
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