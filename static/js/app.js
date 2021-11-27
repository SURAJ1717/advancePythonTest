var app = angular.module('challengeApp', ['ngSanitize', 'ui.select']);

app.config(function ($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
});

app.controller('AppController', ['$scope', '$http', function ($scope, $http) {

    $scope.base_url = (window.location.hostname == '127.0.0.1') ? 'http://'+ window.location.hostname +':8000/' : 'https://'+ window.location.hostname +'/';
    $scope.processing = false;
    var vm = this;

    vm.books = [];
    vm.page_number = 1;
    vm.languages = [];

    $scope.postForm = function(API, Data, page_process=null){

        $scope.processing = true;

        var url = $scope.base_url + API;
        
        var requestData = new FormData();

        angular.forEach(Data, function (value, key) { requestData.append(key, value) });
        
        if(page_process){

            vm.page_number = (page_process == 'increase') ? vm.page_number+1 : vm.page_number-1;
        }

        requestData.append("page_number", vm.page_number);

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
                vm.books = response.data.page_obj
                vm.page_number = response.data.page_number
                
                $scope.processing = false;
            }, 

            function (error) {

                console.log(error);
                $scope.processing = false;
            }
        );
    }

    $scope.getLanguages = function(API){

        var url = $scope.base_url + API;
        
        $http({
            method : "POST",
            url : url,
            headers: {
                        'Content-Type': undefined,
                    },
            data: {},
        }).then(

            function (response) {
                
                console.log(response);
                vm.languages = response.data
            }, 

            function (error) {

                console.log(error);
            }
        );
    }

}]);

