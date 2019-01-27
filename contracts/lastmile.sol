pragma experimental ABIEncoderV2;
contract lastmile{

    struct Passenger{
        string fname;
        string lname;
        uint age;
        string reference_id;
        string flight_no;
        string gender;
        uint checked_bags;
        string special_preferences;
        string class;

    }

    struct Booking{
        Passenger[] passengers;
        Flight flight;

    }

    struct Flight{
        string airline;
        string flight_number;
        string flight_date;
        uint departure_time;
        uint arrival_time;
        string departure_airport;
        string arrival_airport;
        string status;
        Flight_check flight_check;

    }

    struct Flight_check{
        bool hydraulics;
        bool wheels;
        bool landing_mechanism;
        bool nav_system;
    }


    event IssueTicket(Passenger _passenger, Flight _flight);
    mapping (address => Passenger) passengers;
    address[] public PassengersAccts;

    mapping (address => Flight) flights;
    address[] public FlightAccts;

    string[] public FlightRefs;
    function setPassenger (address _address, string _fname, string _lname, uint _age, string _reference_id, string _flight_no, string _gender,
                            uint _checked_bags, string _special_preferences, string _class)  public {
        var passenger = passengers[_address];

        passenger.fname = _fname;
        passenger.lname = _lname;
        passenger.age = _age;
        passenger.reference_id = _reference_id;
        passenger.flight_no = _flight_no;
        passenger.gender = _gender;
        passenger.checked_bags = _checked_bags;
        passenger.special_preferences = _special_preferences;
        passenger.class = _class;
        PassengersAccts.push(_address) -1;
        FlightRefs.push(_reference_id);

    }
        function getFlightRefs()  public returns(string[]) {
            return (FlightRefs);
        }

    function setFlight (address _address, string _airline, string _flight_number,string _flight_date, uint _departure_time,
                        uint _arrival_time, string _departure_airport, string _arrival_airport, string _status,
                        Flight_check _flight_check)  public {
        var flight = flights[_address];

        flight.airline = _airline;
        flight.flight_number = _flight_number;
        flight.flight_date = _flight_date;
        flight.departure_airport = _departure_airport;
        flight.arrival_airport = _arrival_airport;
        flight.departure_time = _departure_time;
        flight.arrival_time = _arrival_time;
        flight.status = _status;
        flight.flight_check = _flight_check;
        FlightAccts.push(_address) -1;
    }

        function getPassengers(address _address) view public  returns (string) {
            return (passengers[_address].reference_id);

        }

        function getFlights(address _address) view public  returns (string,string) {
            return (flights[_address].flight_number, flights[_address].flight_date);

        }

        function countFlights() view public returns (uint){
            return FlightAccts.length;
        }








}