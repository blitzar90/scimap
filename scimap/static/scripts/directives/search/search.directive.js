angular.module('scimap').directive('search', ['', function() {
	return {
		name: 'search',
		// priority: 1,
		// terminal: true,
		scope: {
			onSelect : '&onSelect'
		}, // {} = isolate, true = child, false/undefined = no change
		controller: function($scope, $element, $attrs, $transclude) {
			console.log($scope);
		},
		// require: 'ngModel', // Array = multiple requires, ? = optional, ^ = check parent elements
		restrict: 'EA', // E = Element, A = Attribute, C = Class, M = Comment
		// template: '<div></div>',
		templateUrl: './search.directive.html',
		// replace: true,
		// transclude: true,
		// compile: function(tElement, tAttrs, function transclude(function(scope, cloneLinkingFn){ return function linking(scope, elm, attrs){}})),
		link: function($scope, iElm, iAttrs, controller) {
			console.log('link', $scope);		
		}
	};
}]);