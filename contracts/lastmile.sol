pragma solidity ^0.5.0;

contract lastmile{

    struct Passenger{
        bytes32 fname;
        bytes32 lname;
        uint age;
        bytes32 gender;
        uint checked_bags;
        bytes32 special_preferences;
        bytes32 class;

    }

    struct Booking{
        Passenger[] passengers;
        Flight flight;

    }

    struct Flight{
        bytes32 airline;
        bytes32 flight_number;
        uint departure_time;
        uint arrival_time;
        bytes32 departure_airport;
        bytes32 arrival_airport;
        bytes32 status;
        Flight_check flight_check;

    }

    struct Flight_check{
        bool hydraulics;
        bool wheels;
        bool landing_mechanism;
        bool nav_system;
    }

    mapping (address => Passenger) passengers;
    address[] public PassengersAccts;

    mapping (address => Flight) flights;
    address[] public FlightAccts;


    function setPassenger (address _address, bytes32 _fname, bytes32 _lname, uint _age, bytes32 _gender,
                            uint _checked_bags, bytes32 _special_preferences, bytes32 _class) view public {
        var passenger = passengers[_address];

        passenger.fname = _fname;
        passenger.lname = _lname;
        passenger.age = _age;
        passenger.gender = _gender;
        passenger.checked_bags = _checked_bags;
        passenger.special_preferences = _special_preferences;
        passenger.class = _class;

    }

    function setFlight (address _address, bytes32 _airline, bytes32 _flight_number, uint _departure_time,
                        uint _arrival_time, bytes32 _departure_airport, bytes32 _arrival_airport, bytes32 _status,
                        Flight_check _flight_check) view public {
        var flight = flights[_address];

        flight.airline = _airline;
        flight.flight_number = _flight_number;
        flight.departure_airport = _departure_airport;
        flight.arrival_airport = _arrival_airport;
        flight.departure_time = _departure_time;
        flight.arrival_time = _arrival_time;
        flight.status = _status;
        flight.flight_check = _flight_check;
    }






}
