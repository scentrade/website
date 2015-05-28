(function(){
  'use strict';

  angular
    .module('scentrade.controllers')
    .controller('MainMenuController', MainMenuController);

  MainMenuController.$inject = ['$scope', '$location'];

  function MainMenuController($scope, $location){
    $scope.isActive = function(viewLocation) {
      if( viewLocation == '/inicio' && $location.path() == '/' ){
        return true;
      } else {
        return ($location.path()).indexOf(viewLocation) > -1;
      }
    };
  }
})();