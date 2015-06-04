(function(){
  'use strict';

  angular.module('scentrade.controllers')
    .controller('ServicesController', ServicesController);

  ServicesController.$inject = ['$scope', '$rootScope', '$modal', '$window'];

  function ServicesController($scope, $rootScope, $modal, $window){
    $rootScope.bodyClass = 'services';
    $rootScope.title = 'Servicios';

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

    $($window).on('scroll', function(){
      if( $('div.reveal-items-container:in-viewport').length > 0 ){
        $('.reveal-item').each(function(index){
          var $this = $(this);
          setTimeout(function(){
            $this.addClass('reveal');
          }, 300 * index);
        });
      }
    });
  }
})();