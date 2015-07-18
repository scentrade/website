(function(){
  'use strict';

  angular.module('scentrade')
    .constant('API_PAGE_SIZE', 20)
    .constant('API_URL_DEV', 'http://scentrade:8000/[language]/api/')
    .constant('API_URL_PROD', 'http://www.scentrade.co/[language]/api/');
})();