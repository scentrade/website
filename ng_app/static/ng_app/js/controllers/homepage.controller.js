(function(){
  'use strict';

  angular.module('scentrade.controllers')
    .controller('HomePageController', HomePageController);

  HomePageController.$inject = ['$scope', '$rootScope', '$http', 'API', '$modal'];

  function HomePageController($scope, $rootScope, $http, API, $modal){
    $rootScope.bodyClass = 'homepage';
    $rootScope.title = 'Inicio';

    var vm = this;
    vm.openFreeTrialModal = openFreeTrialModal;

    // -----------------------------------------------------------------------------

    $http.get(API.makeURL('clients'))
      .success(function(response, status){
        vm.clients = response.results;
      });

    $http.get(API.makeURL('testimonials?limit=3'))
      .success(function(response, status){
        vm.testimonials = response.results;
      });

    function openFreeTrialModal(){
      var modalInstance = $modal.open({
        templateUrl: 'free-trial-modal.html',
        controller: 'ModalFreeTrialController',
        controllerAs: 'vm',
        resolve: {
          items: function () {
            return $scope.items;
          }
        }
      });

      /*modalInstance.result.then(function (selectedItem) {
        $scope.selected = selectedItem;
      }, function () {
        $log.info('Modal dismissed at: ' + new Date());
      });*/
    }
  }
})();