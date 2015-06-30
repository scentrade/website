(function(){
  'use strict';

  angular.module('scentrade.controllers')
    .controller('CartController', CartController);

  CartController.$inject = ['$scope', '$http', 'API', '$timeout'];

  function CartController($scope, $http, API, $timeout){
    var vm = this;

    vm.deleteProduct = deleteProduct;
    vm.updateProduct = updateProduct;
    vm.submitForm = submitForm;

    // -----------------------------------------------------------------------------

    fetchCart();

    function fetchCart(onlyTotal){
      if( !onlyTotal ) onlyTotal = false;

      $http.get(API.makeURL('cart'))
        .success(function(response, status){
          if(onlyTotal){
            vm.cart.total = response.total;
          } else {
            vm.cart = response;
          }

          var reference = 'Compra en Scentrade.co ' + new Date().getTime();
          var signature = "26ta6kdhkhqmt5v64o12gh43hl~505378~" + reference + "~" + response.total + "~COP";
          vm.reference = reference;
          vm.signature = CryptoJS.MD5(signature).toString();
        });
    }

    function deleteProduct(id){
      $http.post(API.makeURL('cart/remove'), {'product_id': id})
        .success(function(){
          fetchCart();
        });
    }

    function updateProduct(id, quantity){
      if( !quantity ) quantity = 1;

      $http.post(API.makeURL('cart/update'), {'product_id': id, 'product_quantity': quantity})
        .success(function(){
          fetchCart(true);
        });
    }

    function submitForm(){
      if( $scope['personal_info_form'].$valid ){
        vm.loading = true;
        $http.post(API.makeURL('store/buyers'), vm['buyer_data'])
          .success(function(response){
            vm['buyer_email'] = response['email'];

            $http.post(API.makeURL('store/purchases'), {'buyer': response['id'], 'cart': JSON.stringify(vm.cart)})
              .success(function(response){
                vm['response_url'] = 'http://www.scentrade.co/es/carrito/finalizado?purchase=' + response['id'];
                $('form#payu-payment').trigger('submit');
              });
          })
          .error(function(response){
            vm.loading = false;
          });
      }
    }
  }
})();