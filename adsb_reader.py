import datetime

class Plane:
    def __init__(self, icao):
        self.icao = icao
        self.message_type = None
        self.transmission_type = None
        self.session_id = None
        self.aircraft_id = None
        self.flight_id = None
        self.datetime_message_generated = None
        self.datetime_message_logged = None
        self.call_sign = None
        self.altitude = None
        self.ground_speed = None
        self.track = None
        self.latitude = None
        self.longitude = None
        self.vertical_rate = None
        self.squawk = None
        self.alert = None
        self.emergency = None
        self.spi = None
        self.is_on_ground = None

    def update(self, fields):
        self.message_type = fields[0]
        self.transmission_type = fields[1]
        self.session_id = fields[2]
        self.aircraft_id = fields[3]
        self.flight_id = fields[4]

        date_generated = fields[6]
        time_generated = fields[7]
        if date_generated and time_generated:
            self.datetime_message_generated = datetime.datetime.strptime(f"{date_generated} {time_generated}", "%Y/%m/%d %H:%M:%S.%f")
        
        date_logged = fields[8]
        time_logged = fields[9]
        if date_logged and time_logged:
            self.datetime_message_logged = datetime.datetime.strptime(f"{date_logged} {time_logged}", "%Y/%m/%d %H:%M:%S.%f")
        
        self.call_sign = fields[10] if fields[10] else self.call_sign
        self.altitude = fields[11] if fields[11] else self.altitude
        self.ground_speed = fields[12] if fields[12] else self.ground_speed
        self.track = fields[13] if fields[13] else self.track
        self.latitude = fields[14] if fields[14] else self.latitude
        self.longitude = fields[15] if fields[15] else self.longitude
        self.vertical_rate = fields[16] if fields[16] else self.vertical_rate
        self.squawk = fields[17] if fields[17] else self.squawk
        self.alert = fields[18] if fields[18] else self.alert
        self.emergency = fields[19] if fields[19] else self.emergency
        self.spi = fields[20] if fields[20] else self.spi
        self.is_on_ground = fields[21] if fields[21] else self.is_on_ground

class ADSBParser:
    def __init__(self):
        self.planes = {}

    def parse_message(self, message):
        fields = message.strip().split(',')
        icao = fields[4]
        if icao not in self.planes:
            self.planes[icao] = Plane(icao)
        self.planes[icao].update(fields)

    def parse_data(self, data):
        for message in data:
            self.parse_message(message)

    def get_planes(self):
        return self.planes

# Example usage
data = [
    "MSG,7,1,1,C00E6C,1,2024/01/29,09:33:43.665,2024/01/29,09:33:43.665,,32000,,,,,,,,,,",
    "MSG,7,1,1,A4794E,1,2024/01/29,09:33:43.665,2024/01/29,09:33:43.665,,33000,,,,,,,,,,",
    "MSG,3,1,1,A87196,1,2024/01/29,09:33:43.665,2024/01/29,09:33:43.665,,34100,,,39.99428,-84.06557,,,0,,0,0",
    "MSG,3,1,1,AA739D,1,2024/01/29,09:33:43.665,2024/01/29,09:33:43.665,,24225,,,40.01211,-83.31401,,,0,,0,0",
    "MSG,4,1,1,AAB8CD,1,2024/01/29,09:33:43.665,2024/01/29,09:33:43.665,,,442,264,,,64,,,,,0",
    "MSG,8,1,1,AC2567,1,2024/01/29,09:33:43.665,2024/01/29,09:33:43.665,,,,,,,,,,,,0",
    "MSG,5,1,1,AA739D,1,2024/01/29,09:33:43.665,2024/01/29,09:33:43.665,,24225,,,,,,,0,,0,",
    "MSG,8,1,1,AC2567,1,2024/01/29,09:33:43.665,2024/01/29,09:33:43.665,,,,,,,,,,,,0",
    "MSG,8,1,1,AC2567,1,2024/01/29,09:33:43.665,2024/01/29,09:33:43.665,,,,,,,,,,,,0",
    "MSG,8,1,1,A406C9,1,2024/01/29,09:33:43.665,2024/01/29,09:33:43.665,,,,,,,,,,,,0",
    "MSG,3,1,1,A8B926,1,2024/01/29,09:33:43.665,2024/01/29,09:33:43.665,,33950,,,37.49277,-84.89118,,,0,,0,0",
    "MSG,5,1,1,A4F6FE,1,2024/01/29,09:33:43.665,2024/01/29,09:33:43.665,,23000,,,,,,,0,,0,",
    "MSG,5,1,1,A3A9DE,1,2024/01/29,09:33:43.665,2024/01/29,09:33:43.665,,43025,,,,,,,0,,0,",
    "MSG,5,1,1,A6AABA,1,2024/01/29,09:33:43.665,2024/01/29,09:33:43.665,,34000,,,,,,,0,,0,",
    "MSG,3,1,1,A28928,1,2024/01/29,09:33:43.665,2024/01/29,09:33:43.665,,32000,,,41.09454,-83.79626,,,0,,0,0",
    "MSG,8,1,1,AC90F3,1,2024/01/29,09:33:43.665,2024/01/29,09:33:43.665,,,,,,,,,,,,0",
    "MSG,8,1,1,AAEC9C,1,2024/01/29,09:33:43.665,2024/01/29,09:33:43.665,,,,,,,,,,,,0",
    "MSG,7,1,1,ADA092,1,2024/01/29,09:33:43.665,2024/01/29,09:33:43.665,,7700,,,,,,,,,,",
    "MSG,8,1,1,A28928,1,2024/01/29,09:33:43.665,2024/01/29,09:33:43.665,,,,,,,,,,,,0",
    "MSG,8,1,1,AB56EE,1,2024/01/29,09:33:43.665,2024/01/29,09:33:43.665,,,,,,,,,,,,0",
    "MSG,8,1,1,A92EA0,1,2024/01/29,09:33:43.665,2024/01/29,09:33:43.665,,,,,,,,,,,,0"
]

parser = ADSBParser()
parser.parse_data(data)

planes = parser.get_planes()

for icao, plane in planes.items():
    print(f"ICAO: {icao}, Altitude: {plane.altitude}, Latitude: {plane.latitude}, Longitude: {plane.longitude}, Time Logged: {plane.datetime_message_logged}, Time Generated: {plane.datetime_message_generated}")
