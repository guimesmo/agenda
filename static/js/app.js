var Agenda = angular.module('Agenda', []);

Agenda.config(function($interpolateProvider){
  $interpolateProvider.startSymbol('{[{');
  $interpolateProvider.endSymbol('}]}');
});

Agenda.controller('EventsListController', function EventsListController($scope, $http) {
    var delayed_jobs = $http.get("http://localhost:8000/next_events/").success(
        function(data){
            $scope.delayed_jobs = data;
        }
    );
});
