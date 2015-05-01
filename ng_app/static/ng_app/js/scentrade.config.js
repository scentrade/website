(function(){
  'use strict';

  angular
      .module('scentrade.config')
      .config(config);

  config.$inject = ['$httpProvider', '$locationProvider'];

  function config($httpProvider, $locationProvider){
    // http://django-angular.readthedocs.org/en/latest/integration.html#xmlhttprequest
    $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';

    $locationProvider.html5Mode(true);

    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
  }
})();