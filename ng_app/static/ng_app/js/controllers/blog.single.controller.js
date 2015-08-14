(function(){
  'use strict';

  angular.module('scentrade.controllers')
    .controller('BlogSingleController', BlogSingleController);

  BlogSingleController.$inject = ['$scope', '$rootScope', '$http', '$routeParams', 'API', '$window'];

  function BlogSingleController($scope, $rootScope, $http, $routeParams, API, $window){
    $rootScope.bodyClass = 'blog-single';
    $rootScope.title = 'Blog';

    var vm = this;

    vm.sharePath = $window.location.href;

    $http.get(API.makeURL('blog/posts/' + $routeParams['postSlug']))
      .success(function(response){
        $rootScope.title = response['title'];
        $rootScope.metaDescription = response['meta_description'];
        vm.post = response;
      });
  }
})();