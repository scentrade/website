(function(){
  'use strict';

  angular.module('scentrade.controllers')
    .controller('HomePageController', HomePageController);

  HomePageController.$inject = ['$scope', '$rootScope', '$http', 'API', '$modal', '$window'];

  function HomePageController($scope, $rootScope, $http, API, $modal, $window){
    $rootScope.bodyClass = 'homepage';
    $rootScope.title = 'Inicio';

    var vm = this;
    vm.openFreeTrialModal = openFreeTrialModal;

    // -----------------------------------------------------------------------------

    $http.get(API.makeURL('clients'))
      .success(function(response, status){
        vm.clients = response.results;
      });

    $http.get(API.makeURL('testimonials?limit=3'))
      .success(function(response, status){
        vm.testimonials = response.results;
      });

    function openFreeTrialModal(){
      var modalInstance = $modal.open({
        templateUrl: 'free-trial-modal.html',
        controller: 'ModalFreeTrialController',
        controllerAs: 'vm',
      });
    }

    $($window).on('scroll', function(){
      $('.homepage-item:in-viewport').addClass('reveal');
    });

    // Diamond functionality
    // -----------------------------------------------------------------------------
    var $whatWeDo = $('section#what-we-do'),
      $whatWeDoServices = $('div#what-we-do-services'),
      $whatWeDoHome = $('div#what-we-do-home');

    $whatWeDoServices.on('mouseover', function(){
      $('section#what-we-do').addClass('over-services');
    });

    $whatWeDoServices.on('mouseleave', function(){
      $('section#what-we-do').removeClass('over-services');
    });

    $whatWeDoHome.on('mouseover', function(){
      $('section#what-we-do').addClass('over-home');
    });

    $whatWeDoHome.on('mouseleave', function(){
      $('section#what-we-do').removeClass('over-home');
    });
  }
})();