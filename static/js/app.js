var Agenda = angular.module('Agenda', ['ngMask']);

Agenda.config(function($interpolateProvider){
  $interpolateProvider.startSymbol('{[{');
  $interpolateProvider.endSymbol('}]}');
});



Agenda.controller('EventsListController', function EventsListController($scope, $http, $interval) {
    function load_table(){
        $http.get("/update_events/");
        var delayed_jobs = $http.get("/delayed_events/").success(
            function(data){
                $scope.delayed_jobs = data;
            }
        );
        var next_jobs = $http.get("/next_events/").success(
            function(data){
                $scope.next_jobs = data;
            }
        );
        var done_jobs = $http.get("/done_events/").success(
            function(data){
                $scope.done_jobs = data;
            }
        );
    };


    $interval(function(){$http.get("/update_events/")}, 60000);

    // add event
    $scope.add_event = function(event){
        $http.post(
            '/event/',
            {
                name: event.name,
                date: event.date,
                time: event.time
            }
        ).success(
            function(){
                load_table();
        });
    };

    // init table
    load_table();

    // button actions
    $scope.cancel_event = function(event_id){
        $http.post("/finish_event/" + event_id, {status: 104}).success(function(){
            load_table();
        });
    };
    $scope.confirm_event = function(event_id){
        $http.post("/finish_event/" + event_id, {status: 105}).success(function(){
            load_table();
        });
    };

});
