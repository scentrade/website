(function(){
  'use strict';

  angular.module('scentrade.services')
    .factory('formUtils', formUtils);

  function formUtils(){
    var formUtils = {
      'submitButtonLoading': submitButtonLoading
    };

    return formUtils;

    function submitButtonLoading($form, isLoading){
      var $submitButton = $form.find('button[type="submit"]');
      if( isLoading ){
        $submitButton.data('initial-html', $submitButton.html());
        $submitButton.html($submitButton.data('loading-html'));
      } else {
        $submitButton.html($submitButton.data('initial-html'));
      }
    }
  }
})();