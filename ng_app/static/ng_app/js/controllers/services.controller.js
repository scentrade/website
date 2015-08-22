(function(){
  'use strict';

  angular.module('scentrade.controllers')
    .controller('ServicesController', ServicesController);

  ServicesController.$inject = ['$scope', '$rootScope', '$modal'];

  function ServicesController($scope, $rootScope, $modal){
    $rootScope.bodyClass = 'services';
    $rootScope.title = 'Servicios';
    $rootScope.metaDescription = 'Descubra los servicios y productos para crear una estrategia integral de comunicación olfativa.';

    var vm = this;

    vm.openFreeTrialModal = openFreeTrialModal;

    // -----------------------------------------------------------------------------

    function openFreeTrialModal(){
      var modalInstance = $modal.open({
        templateUrl: 'free-trial-modal.html',
        controller: 'ModalFreeTrialController',
        controllerAs: 'vm',
      });
    }
  }
})();