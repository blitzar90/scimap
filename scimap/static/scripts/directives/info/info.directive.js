angular.module('scimap').directive('info', [function() {
	// Runs during compile
	return {
		name: 'info',
		// priority: 1,
		// terminal: true,
		scope: {
			element : '=',
			selectElement : '&',
			hoverElement : '&'
		}, // {} = isolate, true = child, false/undefined = no change
		controller: function($scope, $element, $attrs, $transclude) {
			console.log('info directive', $scope);

			$scope.selectElementBinding = (element) => {
				$scope.selectElement()(element);
			}

			$scope.hoverElementBinding = (element) => {
				$scope.hoverElement()(element);
			}
		},
		// require: 'ngModel', // Array = multiple requires, ? = optional, ^ = check parent elements
		restrict: 'EA', // E = Element, A = Attribute, C = Class, M = Comment
		// template: '',
		templateUrl: 'static/scripts/directives/info/info.directive.html',
		// replace: true,
		// transclude: true,
		// compile: function(tElement, tAttrs, function transclude(function(scope, cloneLinkingFn){ return function linking(scope, elm, attrs){}})),
		link: function($scope, iElm, iAttrs, controller) {
		}
	};
}]);