(function(){
  'use strict';

  angular.module('scentrade.services')
    .factory('API', API);

  API.$inject = ['API_URL_DEV', 'API_URL_PROD'];

  function API(API_URL_DEV, API_URL_PROD){
    var API = {
      'makeURL': makeURL
    };

    return API;

    function makeURL(path){
      var $body = $('body');
      var currentLanguage = $body.data('current-language');
      var debug = ($body.data('debug') == 'True');
      var apiUrl = function(){
        if( debug ){
          return API_URL_DEV;
        } else {
          return API_URL_PROD;
        }
      }();
      return apiUrl.replace('[language]', currentLanguage) + path;
    }
  }
})();