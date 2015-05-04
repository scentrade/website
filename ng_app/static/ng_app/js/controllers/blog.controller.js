(function(){
  'use strict';

  angular.module('scentrade.controllers')
    .controller('BlogController', BlogController);

  BlogController.$inject = ['$scope', '$rootScope'];

  function BlogController($scope, $rootScope){
    $rootScope.bodyClass = 'blog';
    $rootScope.title = 'Blog';
  }
})();