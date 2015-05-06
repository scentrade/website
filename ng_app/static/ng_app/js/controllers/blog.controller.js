(function(){
  'use strict';

  angular.module('scentrade.controllers')
    .controller('BlogController', BlogController);

  BlogController.$inject = ['$scope', '$rootScope', '$http', 'API'];

  function BlogController($scope, $rootScope, $http, API){
    $rootScope.bodyClass = 'blog';
    $rootScope.title = 'Blog';

    var vm = this;
    vm.filterBy = ''; // select ng-model, default to empty
    vm.filterPosts = filterPosts;
    vm.fetchPosts = fetchPosts;
    // fetch posts first time
    vm.fetchPosts();

    // -----------------------------------------------------------------------------

    $http.get(API.makeURL('blog/categories'))
      .success(function(response, status){
        vm.categories = response.results;
      });

    function fetchPosts(filterBy){
      var url = API.makeURL('blog/posts');
      if( filterBy ) url += '?category__slug=' + filterBy;
      $http.get(url)
        .success(function(response, status){
          vm.posts = response.results;
        });
    }

    function filterPosts(){
      vm.fetchPosts(vm.filterBy);
    }
  }
})();