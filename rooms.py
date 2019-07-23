rooms = { 'data': { 'rooms': 
    [ { 'id': 1, 'room_number': "201", 'capacity': 50}, { 'id': 2, 'room_number': "301", 'capacity': 200 }, { 'id': 3, 'room_number': "1B", 'capacity': 100}
    ],
    'events': [
      { 'id': 1, 'room_id': 2, 'start_time': 18, 'end_time': 20, 'attendees': 75 },
      { 'id': 2, 'room_id': 1, 'start_time': 10, 'end_time': 18, 'attendees': 25 },
      { 'id': 3, 'room_id': 2, 'start_time': 10, 'end_time': 18, 'attendees': 20 },
      { 'id': 4, 'room_id': 3, 'start_time': 18, 'end_time': 21, 'attendees': 56 },
    ]
  }
}


room_num = '201'

for room in rooms['data']['rooms']:
    # print(room)
    if room['room_number'] == room_num:
        room_id = room['id']
        room_capacity = room['capacity']
        print(f'Room {room_num} id: {room_id}') #1
        print(f'Room {room_num} capacity: {room_capacity}') #50



for event in rooms['data']['events']:
  # print(event)

  if event['id'] == room_id:
      # print(event)
      print(f"The event #{event['id']} in {room_num} will have {event['attendees']} people.")
      # id room_id, start_time, end_time, attendees
      if event['attendees'] < room_capacity:
          print('The room is over capacity!')
      else:
          print('Everyone will fit in the room.')