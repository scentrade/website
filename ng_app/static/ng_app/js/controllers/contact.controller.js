(function(){
  'use strict';

  angular.module('scentrade.controllers')
    .controller('ContactController', ContactController);

  ContactController.$inject = ['$scope', '$rootScope', '$http', 'API', 'djangoForm', 'formUtils'];

  function ContactController($scope, $rootScope, $http, API, djangoForm, formUtils){
    $rootScope.bodyClass = 'contact';
    $rootScope.title = 'Contacto';

    var vm = this;

    vm.submitContactForm = submitContactForm;

    // -----------------------------------------------------------------------------

    function submitContactForm(){
      var $form = $('form#contact-form');

      if( $scope['contact_data'] ){
        formUtils.submitButtonLoading($form, true);

        $http.post(API.makeURL('contact'), $scope['contact_data'])
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
  }
})();