(function(){
  'use strict';

  angular.module('scentrade.controllers')
    .controller('BlogSingleController', BlogSingleController);

  BlogSingleController.$inject = ['$scope', '$rootScope', '$http', '$routeParams', 'API'];

  function BlogSingleController($scope, $rootScope, $http, $routeParams, API){
    $rootScope.bodyClass = 'blog-single';
    $rootScope.title = 'Blog';

    var vm = this;

    $http.get(API.makeURL('blog/posts/' + $routeParams['postSlug']))
      .success(function(response){
        vm.post = response;
      });
  }
})();