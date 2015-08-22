(function(){
  'use strict';

  angular.module('scentrade.controllers')
      .controller('ProductsController', ProductsController);

  ProductsController.$inject = ['$scope', '$rootScope', '$http', 'API', '$location', '$routeParams', 'API_PAGE_SIZE'];

  function ProductsController($scope, $rootScope, $http, API, $location, $routeParams, API_PAGE_SIZE){
    $rootScope.bodyClass = 'products';
    $rootScope.title = 'Productos';
    $rootScope.metaDescription = 'Productos para empresas y para el hogar con aromas únicos y personalizados.';

    var vm = this;
    vm.addProductToCart = addProductToCart;
    vm.fetchProducts = fetchProducts;
    // fetch products first time
    vm.fetchProducts($routeParams['target']);
    vm.selectedTab = 'all';
    vm.goToPreviousPage = goToPreviousPage;
    vm.goToNextPage = goToNextPage;
    vm.goToPage = goToPage;
    vm.currentPage = $routeParams['page'] || 1;
    vm.categoryChanged = categoryChanged;
    vm.loadingProducts = false;

    // -----------------------------------------------------------------------------

    $http.get(API.makeURL('store/categories'))
        .success(function(response){
          vm.categories = response.results;

          if( $routeParams['category'] ){
            vm.category = _.findWhere(vm.categories, {
              id: parseInt($routeParams['category'])
            });
          }
        });

    if( $routeParams['target'] ){
      vm.selectedTab = $routeParams['target'];
    }

    function fetchProducts(target){
      var page = $routeParams['page'] - 1 || 0,
          offset = API_PAGE_SIZE * page;

      if( angular.isUndefined(target) ) target = 'all';
      var url = API.makeURL('store/products') + '?offset=' + offset;
      if( target != 'all' ) url += '&target=' + target;
      if( $routeParams['category'] ) url += '&category=' + $routeParams['category'];

      vm.loadingProducts = true;

      $http.get(url)
          .success(function(response, status){
            vm.loadingProducts = false;

            vm.products = response.results;
            vm.next = response.next;
            vm.previous = response.previous;

            vm.pages = function(){
              var pages = [];
              for(var i=0; i<response.count/API_PAGE_SIZE; i++){
                pages.push(i+1);
              }
              return pages;
            }();
          });
    }

    function goToPreviousPage(){
      var page = 1;
      if( $routeParams['page'] ) page = parseInt($routeParams['page']) - 1;
      $location.search('page', (page == 0) ? null : page);
    }

    function goToNextPage(){
      var page = 1;
      if( $routeParams['page'] ) page = parseInt($routeParams['page']) + 1;
      $location.search('page', page);
    }

    function goToPage(page){
      $location.search('page', page);
    }

    function addProductToCart(id){
      $http.post(API.makeURL('cart/add'), {'product_id': id})
          .success(function(response, status){
            $rootScope.$broadcast('cart.update', true);
          });
    }

    function categoryChanged(){
      if( vm.category ){
        $location.search('category', vm.category.id);
      } else {
        $location.search('category', null);
      }
      $scope.$on('$routeUpdate', function(){
        if( vm.loadingProducts === false ) fetchProducts($routeParams['target']);
      });
    }
  }
})();