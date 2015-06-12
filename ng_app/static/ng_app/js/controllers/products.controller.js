(function(){
  'use strict';

  angular.module('scentrade.controllers')
    .controller('ProductsController', ProductsController);

  ProductsController.$inject = ['$scope', '$rootScope', '$http', 'API', '$location', '$routeParams'];

  function ProductsController($scope, $rootScope, $http, API, $location, $routeParams){
    $rootScope.bodyClass = 'products';
    $rootScope.title = 'Productos';

    var vm = this;
    vm.addProductToCart = addProductToCart;
    vm.fetchProducts = fetchProducts;
    // fetch products first time
    vm.fetchProducts();
    vm.selectedTab = 'all';

    // -----------------------------------------------------------------------------

    function fetchProducts(params){
      var url = API.makeURL('store/products');
      if( params ) url += params;
      $http.get(url)
        .success(function(response, status){
          vm.products = response.results;
        });
    }

    function addProductToCart(id){
      $http.post(API.makeURL('cart/add'), {'product_id': id})
        .success(function(response, status){
          $rootScope.$broadcast('cart.update', true);
        });
    }
  }
})();