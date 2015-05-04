(function(){
  'use strict';

  angular.module('scentrade.controllers')
    .controller('HomePageController', HomePageController);

  HomePageController.$inject = ['$scope', '$rootScope', '$http', 'API'];

  function HomePageController($scope, $rootScope, $http, API){
    $rootScope.bodyClass = 'homepage';
    $rootScope.title = 'Inicio';

    var vm = this;

    $http.get(API.makeURL('clients'))
      .success(function(response, status){
        vm.clients = response.results;
      });

    $http.get(API.makeURL('testimonials?limit=3'))
      .success(function(response, status){
        vm.testimonials = response.results;
      });
  }
})();