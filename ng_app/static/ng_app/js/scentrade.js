(function(){
  'use strict';

  angular
    .module('scentrade', [
      // angular
      'ngRoute',
      'ngSanitize',

      // third party
//      'uiGmapgoogle-maps',
//      'ng.django.forms',
//      'ngFileUpload',
      'ng.django.forms',
      'ui.bootstrap',
      'fox.scrollReveal',

      // scentrade modules
      'scentrade.config',
      'scentrade.services',
      'scentrade.routes',
      'scentrade.controllers',
      'scentrade.directives',
    ]);

  angular
    .module('scentrade.config', []);

  angular
    .module('scentrade.services', []);

  angular
    .module('scentrade.routes', []);

  angular
    .module('scentrade.controllers', []);

  angular
    .module('scentrade.directives', []);
})();