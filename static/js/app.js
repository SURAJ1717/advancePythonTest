var app = angular.module('challengeApp', ['ngSanitize', 'ui.select']);

app.config(function ($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
});

app.controller('AppController', ['$scope', '$http', function ($scope, $http) {

    console.log(window.location.hostname);
    if(window.location.hostname == '127.0.0.1'){

        $scope.base_url = 'http://'+ window.location.hostname +':8000/';
    }else{
    
        $scope.base_url = 'https://'+ window.location.hostname +'/';
    }

    $scope.processing = false;
    var vm = this;

    vm.books = [];

    $scope.postForm = function(API, Data){

        $scope.processing = true;

        var url = $scope.base_url + API;
        
        var requestData = new FormData();

        angular.forEach(Data, function (value, key) { requestData.append(key, value) });
        
        $http({
            method : "POST",
            url : url,
            headers: {
                        'Content-Type': undefined,
                    },
            data: requestData,
        }).then(

            function (response) {
                
                console.log(response);
                $scope.processing = false;
            }, 

            function (error) {

                console.log(error);
                $scope.processing = false;
            }
        );
    }
}]);

