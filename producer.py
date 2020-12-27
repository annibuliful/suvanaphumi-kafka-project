import faust
import random
import datetime
# class prototype
class Location(faust.Record):
    location_name: str
    location_zone: str
    # next location by location
    next_left: str
    next_right: str
    next_top: str
    next_bottom: str

class MoveEvent(faust.Record):
    location_src: str
    location_dest: str
    date_time: str
    

def generate_locations():
    # list location
    list_locations = []

    list_locations.append(
        Location(
            location_name = "Train",
            location_zone = "parking",
            next_right = "parking",
            next_left = None,
            next_top = None,
            next_bottom = "Garage"
        )
    )
    list_locations.append(
        Location(
            location_name = "G5",
            location_zone = "concourse G",
            next_right = "Parking Short Term 1",
            next_left = None,
            next_top = "Train",
            next_bottom = "G4"
        )
    )

    list_locations.append(
        Location(
            location_name = "G4",
            location_zone = "concourse G",
            next_right = "Parking Short Term 1",
            next_left = None,
            next_top = "G5",
            next_bottom = "G3"
        )
    )

    list_locations.append(
        Location(
            location_name = "G3",
            location_zone = "concourse G",
            next_right = "Parking Short Term 1",
            next_top = "G4",
            next_bottom = "G2",
            next_left = None
        )
    )

    list_locations.append(
        Location(
            location_name = "G2",
            location_zone = "concourse G",
            next_right = "International 1",
            next_left = None,
            next_top = "G3",
            next_bottom = "G1"
        )
    )

    list_locations.append(
        Location(
            location_name = "G1",
            location_zone = "concourse G",
            next_right = "International 1",
            next_left = None,
            next_top = "G2",
            next_bottom = "Information 1"
        )
    )

    list_locations.append(
        Location(
            location_name = "Information 1",
            location_zone = "Intersaction 1",
            next_right = "Security 1",
            next_left = "F2",
            next_top = "G1",
            next_bottom = "E2"
        )
    )

    list_locations.append(
        Location(
            location_name = "F2",
            location_zone = "concourse F",
            next_right = "Information 1",
            next_left = "F4",
            next_top = None,
            next_bottom = None
        )
    )

    list_locations.append(
        Location(
            location_name = "F4",
            location_zone = "concourse F",
            next_right = "F2",
            next_left = "Information 1",
            next_top = None,
            next_bottom = None
        )
    )

    list_locations.append(
        Location(
            location_name = "F6",
            location_zone = "concourse F",
            next_right = "F4",
            next_left = None,
            next_bottom = None,
            next_top = None
        )
    )

    list_locations.append(
        Location(
            location_name = "Security 1",
            location_zone = "Main Terminal",
            next_left = "Information 1",
            next_right = "Baggage Claim 1",
            next_top = "Ticketing 1",
            next_bottom = None
        )
    )

    list_locations.append(
        Location(
            location_name = "Baggage Claim 1",
            location_zone = "Main Terminal",
            next_left = "Security 1",
            next_right = "Security 2",
            next_top = "Ticketing 1",
            next_bottom = None
        )
    )

    list_locations.append(
        Location(
            location_name = "Security 2",
            location_zone = "Main Termimnal",
            next_left = "Baggage Claim 1",
            next_top = "Taxi Rank",
            next_right = "Baggage Claim 2",
            next_bottom = None
        )
    )

    list_locations.append(
        Location(
            location_name = "Baggage Claim 2",
            location_zone = "Main Termimnal",
            next_left = "Security 2",
            next_top = "Taxi Rank",
            next_right = "Security 3",
            next_bottom = None
        )
    )

    list_locations.append(
        Location(
            location_name = "Security 3",
            location_zone = "Main Termimnal",
            next_left = "Baggage Claim 2",
            next_top = "Ticketing 2",
            next_right = "Information 2",
            next_bottom = None
        )
    )

    list_locations.append(
        Location(
            location_name = "Information 2",
            location_zone = "Intersaction 1",
            next_left = "Security 3",
            next_top = "Bus 2",
            next_right = "B1",
            next_bottom = None
        )
    )

    list_locations.append(
        Location(
            location_name = "B1",
            location_zone = "Concourse B",
            next_left = "Information 2",
            next_top = "A1",
            next_right = "B3",
            next_bottom = "C1"
        )
    )

    list_locations.append(
        Location(
            location_name = "B3",
            location_zone = "Concourse B",
            next_left = "B1",
            next_top = "A1",
            next_right = "B5",
            next_bottom = "C1"
        )
    )

    list_locations.append(
        Location(
            location_name = "B5",
            location_zone = "Concourse B",
            next_left = "B3",
            next_top = "A1",
            next_right = None,
            next_bottom = "C1"
        )
    ) 

    list_locations.append(
        Location(
            location_name = "Taxi Rank",
            location_zone = "Main Terminal",
            next_left = "Car Rental",
            next_top = "Garage",
            next_right = "Bus 1",
            next_bottom = "Baggage Claim 2"
        )
    )

    list_locations.append(
        Location(
            location_name = "A1",
            location_zone = "Concourse A",
            next_left = "Information 2",
            next_top = "A2",
            next_right = None,
            next_bottom = "B1"
        )
    )

    list_locations.append(
        Location(
            location_name = "A2",
            location_zone = "Concourse A",
            next_left = "Bus 2",
            next_top = "A3",
            next_right = None,
            next_bottom = "A1"
        )
    )

    list_locations.append(
        Location(
            location_name = "A3",
            location_zone = "Concourse A",
            next_left = "Parking 4",
            next_top = "A4",
            next_right = None,
            next_bottom = "A2"
        )
    )

    list_locations.append(
        Location(
            location_name = "A4",
            location_zone = "Concourse A",
            next_left = "Parking 4",
            next_top = "A5",
            next_right = None,
            next_bottom = "A3"
        )
    )

    list_locations.append(
        Location(
            location_name = "A5",
            location_zone = "Concourse A",
            next_left = "Parking 4",
            next_top = "A6",
            next_right = None,
            next_bottom = "A4"
        )
    )

    list_locations.append(
        Location(
            location_name = "A6",
            location_zone = "Concourse A",
            next_left = "Parking 1",
            next_top = None,
            next_right = None,
            next_bottom = "A5"
        )
    )

    list_locations.append(
        Location(
            location_name = "F6",
            location_zone = "Concourse F",
            next_left = None,
            next_top = None,
            next_right = "F4",
            next_bottom = "F5"
        )
    )

    list_locations.append(
        Location(
            location_name = "F4",
            location_zone = "Concourse F",
            next_left = "F6",
            next_top = None,
            next_right = "F2",
            next_bottom = "F3"
        )
    )

    list_locations.append(
        Location(
            location_name = "F2",
            location_zone = "Concourse F",
            next_left = "F4",
            next_top = "G1",
            next_right = "Information 1",
            next_bottom = "F1"
        )
    )

    list_locations.append(
        Location(
            location_name = "E2",
            location_zone = "Concourse E",
            next_left = "F1",
            next_top = "Information 1",
            next_right = "E1",
            next_bottom = "E4"
        )
    )

    list_locations.append(
        Location(
            location_name = "E4",
            location_zone = "Concourse E",
            next_left = None,
            next_top = "E2",
            next_right = "E3",
            next_bottom = "E5"
        )
    )

    list_locations.append(
        Location(
            location_name = "E6",
            location_zone = "Concourse E",
            next_left = None,
            next_top = "E4",
            next_right = "E5",
            next_bottom = "E8"
        )
    )

    list_locations.append(
        Location(
            location_name = "E8",
            location_zone = "Concourse E",
            next_left = None,
            next_top = "E6",
            next_right = "E7",
            next_bottom = "E10"
        )
    )

    list_locations.append(
        Location(
            location_name = "E10",
            location_zone = "Concourse E",
            next_left = None,
            next_top = "E8",
            next_right = "E9",
            next_bottom = None
        )
    )

    list_locations.append(
        Location(
            location_name = "C2",
            location_zone = "Concourse C",
            next_left = "D1",
            next_top = "Information 2",
            next_right = "C1",
            next_bottom = "C4"
        )
    )

    list_locations.append(
        Location(
            location_name = "C4",
            location_zone = "Concourse C",
            next_left = "D1",
            next_top = "C2",
            next_right = "C3",
            next_bottom = "C6"
        )
    )

    list_locations.append(
        Location(
            location_name = "C6",
            location_zone = "Concourse C",
            next_left = None,
            next_top = "C4",
            next_right = "C5",
            next_bottom = "C8"
        )
    )

    list_locations.append(
        Location(
            location_name = "C8",
            location_zone = "Concourse C",
            next_left = None,
            next_top = "C6",
            next_right = "C7",
            next_bottom = "C10"
        )
    )

    list_locations.append(
        Location(
            location_name = "C10",
            location_zone = "Concourse C",
            next_left = None,
            next_top = "C8",
            next_right = "C9",
            next_bottom = None
        )
    )

    return list_locations

list_locs = generate_locations()

def get_next_location(current_location):
    """
    0 = next_left
    1 = next_right
    2 = next_top
    3 = next_bottom
    """
    result_next = ""
    next_lo_rand = random.randrange(0,4)
    if next_lo_rand == 0:
        result_next = current_location.next_left
    elif next_lo_rand == 1:
        result_next = current_location.next_right
    elif next_lo_rand == 2:
        result_next = current_location.next_top
    else:
        result_next = current_location.next_bottom
    return result_next

def get_loc_info(list_locs,current_loc =""):
    if current_loc == None:
        return current_loc

    result = None
    for loc in list_locs:
        if(loc.location_name == current_loc):
            result = loc
    
    return result

def random_first_loc():
    list_spawn = ["G5","A6", "Parking 1", "Train","B5"]
    return random.choice(list_spawn)

app = faust.App('producer-app', broker='kafka://localhost')
location_topic = app.topic('location', value_type=Location)
move_topic = app.topic('move-event', value_type=MoveEvent)
# print(get_next_location(list_locs[0]))

@app.agent(move_topic)
async def move_event(move_events):
    async for move in move_events:
        # location_src location_dest date_time
        print(f' from {move.location_src} -> {move.location_dest}: time = {move.date_time}')

@app.timer(interval=1.0)
async def move_event_sender(app):
    current = get_loc_info(list_locs,random_first_loc())
    while current != None:

        new_loc = get_next_location(current)
        new_loc = get_loc_info(list_locs,new_loc)
        if new_loc == None:
            return

        new_event = MoveEvent(
            location_src = current.location_name,
            location_dest = new_loc.location_name,
            date_time = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        )

        await move_event.send(value=new_event)
        current = new_loc

if __name__ == '__main__':
    app.main()