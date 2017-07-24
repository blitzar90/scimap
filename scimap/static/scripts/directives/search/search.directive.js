angular.module('scimap').directive('search', ['$http', function($http) {
	return {
		name: 'search',
		scope: {
			onSelect : '&'
		},
		controller: function($scope, $element, $attrs, $transclude) {

			$scope.types = {
				node : 'Теорема',
				route : 'Доказательство'
			}

			console.log($scope.onSelect);
			console.log($scope.onSelect());
			$scope.suggestions = [];

			$scope.onSelectBinding = (item, model) => {
				$scope.onSelect()(item, model);
			}

			$scope.getType = (type) => {
				return $scope.types[type];
			}

			$scope.refreshSuggestions = (searchWord) => {

				if (!searchWord) return;

				console.log('refreshSuggestions');
				return $http.get('/api/search?q=' + searchWord).then(data => {
					console.log(data);
					$scope.suggestions = data.data;
				}, error => {
					console.log(error);
				});
			}
		},
		restrict: 'EA', // E = Element, A = Attribute, C = Class, M = Comment
		templateUrl: 'static/scripts/directives/search/search.directive.html',
		link: function($scope, iElm, iAttrs, controller) {
			console.log('link', $scope);
		}
	};
}]);