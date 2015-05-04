(function(){
  'use strict';

  angular.module('scentrade.controllers')
    .controller('ProductsController', ProductsController);

  ProductsController.$inject = ['$scope', '$rootScope', '$http', 'API'];

  function ProductsController($scope, $rootScope, $http, API){
    $rootScope.bodyClass = 'products';
    $rootScope.title = 'Productos';

    var vm = this;
    vm.addProductToCart = addProductToCart;

    // -----------------------------------------------------------------------------

    $http.get(API.makeURL('store/products'))
      .success(function(response, status){
        vm.products = response.results;
      });

    function addProductToCart(id){
      $http.post(API.makeURL('cart/add'), {'product_id': id})
        .success(function(response, status){
          console.log(response);
          $rootScope.$broadcast('cart.update', true);
        });
    }
  }
})();