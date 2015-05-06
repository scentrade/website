(function(){
  'use strict';

  angular.module('scentrade.controllers')
    .controller('BlogController', BlogController);

  BlogController.$inject = ['$scope', '$rootScope', '$http', 'API'];

  function BlogController($scope, $rootScope, $http, API){
    $rootScope.bodyClass = 'blog';
    $rootScope.title = 'Blog';

    var vm = this;

    $http.get(API.makeURL('blog/posts'))
      .success(function(response, status){
        vm.posts = response.results;
      });
  }
})();