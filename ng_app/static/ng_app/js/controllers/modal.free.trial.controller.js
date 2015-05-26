(function(){
  'use strict';

  angular.module('scentrade.controllers')
    .controller('ModalFreeTrialController', ModalFreeTrialController);

  ModalFreeTrialController.$inject = ['$scope', '$modalInstance', '$http', 'API', 'djangoForm', 'formUtils'];

  function ModalFreeTrialController($scope, $modalInstance, $http, API, djangoForm, formUtils){
    var vm = this;

    vm.submit = submit;
    vm.close = close;

    // -----------------------------------------------------------------------------

    function submit(){
      var $form = $('form#contact-form');

      if( $scope['contact_data'] ){
        formUtils.submitButtonLoading($form, true);

        $http.post(API.makeURL('free-trial'), $scope['contact_data'])
          .success(function(response, status){
            formUtils.submitButtonLoading($form, false);
            vm.successMessage = response['detail'];
            vm.success = true;
          })
          .error(function(response, status){
            djangoForm.setErrors($scope['contact_form'], response['form_errors']);
            formUtils.submitButtonLoading($form, false);
          });
      }
    }

    function close(){
      $modalInstance.close();
    }
  }
})();