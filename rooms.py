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

# print(rooms['data']['rooms'][0])


for room in rooms['data']['rooms']:
    # print(room)
    # print(room['room_number'])
    if room['room_number'] == "201":
        # print(room['id'])
        room_201_id = room['id']
        room_201_capacity = room['capacity']
        print(f'Room 201 id: {room_201_id}') #1
        print(f'Room 201 capacity: {room_201_capacity}') #50



# print(rooms['data']['events'][0])

for event in rooms['data']['events']:
    # print(event)

    if event['attendees'] < room_201_capacity:
        print('Over capacity!')
    else:
        print('They will all fit.')