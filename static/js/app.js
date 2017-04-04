var Agenda = angular.module('Agenda', ['ngMask', '720kb.datepicker']);

Agenda.config(function($interpolateProvider, $httpProvider){
  $interpolateProvider.startSymbol('{[{');
  $interpolateProvider.endSymbol('}]}');
  $httpProvider.defaults.xsrfCookieName = 'csrftoken';
  $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
});



Agenda.controller('EventsListController', function EventsListController($scope, $http, $interval) {
    function load_table(){
        $http.get("/update_events/");
        var delayed_jobs = $http.get("/events/?status=delayed").success(
            function(data){
                $scope.delayed_jobs = data;
            }
        );
        var next_jobs = $http.get("/events/?status=next").success(
            function(data){
                $scope.next_jobs = data;
            }
        );
        var done_jobs = $http.get("/events/?status=done").success(
            function(data){
                $scope.done_jobs = data;
            }
        );
    };


    $interval(function(){$http.get("/update_events/")}, 60000);

    // add event
    $scope.add_event = function(event){
        $http.post(
            '/events/',
            {
                name: event.name,
                date: event.date,
                time: event.time
            }
        ).success(
            function(){
                load_table();
              }
        );
    };

    // init table
    load_table();

    // button actions
    $scope.cancel_event = function(event_id){
        $http.delete("/events/" + event_id).success(function(){
            load_table();

        });
    };
    $scope.confirm_event = function(event_id){
        $http.patch("/events/" + event_id, {status: 105}).success(function(){
            load_table();
        });
    };

});
