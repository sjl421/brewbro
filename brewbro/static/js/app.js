var app = angular.module("BrewBro", ["ngRoute", "recipe"]);

app.config(function($routeProvider, $interpolateProvider){
	$routeProvider
		.when("/recipe/:recipeId", {
			templateUrl: "/static/partials/recipe-detail.html",
			controller: "RecipeCtrl"
		});

    $interpolateProvider.startSymbol('{[').endSymbol(']}');
});