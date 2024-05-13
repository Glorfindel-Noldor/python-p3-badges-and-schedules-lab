def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    batch = []
    for name in names:
        batch.append(f"Hello, my name is {name}.")
    return batch;

def assign_rooms(names):
    rooms = []
    for index, name in enumerate(names):
        room_number = index + 1
        rooms.append(f"Hello, {name}! You'll be assigned to room {room_number}!")
    return rooms

def printer(names):
    name = batch_badge_creator(names)
    room = assign_rooms(names)
    for person in name + room:
        print(person)
