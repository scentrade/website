(function(){
  'use strict';

  angular.module('scentrade.controllers')
    .controller('CartController', CartController);

  CartController.$inject = ['$scope', '$http'];

  function CartController($scope, $http){
    var vm = this;

    // -----------------------------------------------------------------------------

    var signature = "26ta6kdhkhqmt5v64o12gh43hl~505378~ScentradeWebSitePayment109090~20000~COP";
    console.log(signature);
    console.log(CryptoJS.MD5(signature).toString());
    vm.signature = CryptoJS.MD5(signature).toString();
  }
})();