(function(){
  'use strict';

  angular.module('scentrade.controllers')
    .controller('ServicesController', ServicesController);

  ServicesController.$inject = ['$scope', '$rootScope'];

  function ServicesController($scope, $rootScope){
    $rootScope.bodyClass = 'services';
    $rootScope.title = 'Servicios';
  }
})();