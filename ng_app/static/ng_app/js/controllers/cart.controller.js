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

                    var signatureTemplate = '{ApiKey}~{merchantId}~{referenceCode}~{amount}~{currency}';

                    var reference = 'Compra en Scentrade.co ' + response['id'];
                    var signature = signatureTemplate.assign({
                      ApiKey: '26ta6kdhkhqmt5v64o12gh43hl',
                      merchantId: '505378',
                      referenceCode: reference,
                      amount: vm.cart.total,
                      currency: 'COP'
                    });

                    vm.reference = reference;
                    vm.signature = CryptoJS.MD5(signature).toString();

                    var testSignature = signatureTemplate.assign({
                      ApiKey: '6u39nqhq8ftd0hlvnjfs66eh8c',
                      merchantId: '500238',
                      referenceCode: reference,
                      amount: 3,
                      currency: 'USD'
                    });

                    vm['test_signature'] = CryptoJS.MD5(testSignature).toString();
                    vm['test_response_url'] = 'http://scentrade:8000/es/carrito/finalizado?purchase=' + response['id'];

                    // update cart total if delivery_preference is "shipping_in_capital"
                    if( vm['buyer_data']['delivery_preference'] == 'shipping_in_capital' ){
                      var currentTotal = vm.cart.total;
                      vm.cart.total = parseInt(currentTotal) + 6000;
                    }

                    $timeout(function(){
                      $('form#payu-payment').trigger('submit');
                    }, 1000);
                  });
            })
            .error(function(response){
              vm.loading = false;
            });
      }
    }
  }
})();