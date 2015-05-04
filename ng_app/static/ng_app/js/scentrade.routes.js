(function(){
  'use strict';

  angular
    .module('scentrade.routes')
    .config(config);

  config.$inject = ['$routeProvider'];

  function config($routeProvider){
    var currentLanguage = '/' + $('body').data('current-language');

    $routeProvider
      .when('/', {
        templateUrl: currentLanguage + '/partials/homepage.html',
        controller: 'HomePageController',
        controllerAs: 'vm'
      })
      // This route is here because I should have my hrefs without first "/" slash
      .when('/inicio', {
        redirectTo: '/'
      })
      .when('/nosotros', {
        templateUrl: currentLanguage + '/partials/sections/about-us.html',
        controller: 'AboutUsController',
        controllerAs: 'vm'
      })
      .when('/productos', {
        templateUrl: currentLanguage + '/partials/sections/products.html',
        controller: 'ProductsController',
        controllerAs: 'vm'
      })
      .when('/servicios', {
        templateUrl: currentLanguage + '/partials/sections/services.html',
        controller: 'ServicesController',
        controllerAs: 'vm'
      })
      .when('/hogar', {
        templateUrl: currentLanguage + '/partials/sections/home.html',
        controller: 'HomeController',
        controllerAs: 'vm'
      })
      .otherwise({
        redirectTo: '/'
      });
  }
})();