(function(){
  'use strict';

  angular.module('scentrade')
    .constant('API_PAGE_SIZE', 20)
    .constant('API_URL_DEV', 'http://scentrade:8003/[language]/api/')
    .constant('API_URL_PROD', 'http://scentrade.co/[language]/api/');
})();