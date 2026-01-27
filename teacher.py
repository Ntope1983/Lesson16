import json


def next_id():
    try:
        with open("teachers.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []
    if not data:
        return 1000
    else:
        data_id = [data[i]['id'] for i in range(len(data))]
        return max(data_id) + 1


class Teacher:
    def __init__(self, first_name="", last_name="", id=next_id()):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name

    def from_dict(self, dictionary_teacher):
        self.id = dictionary_teacher['id']
        self.first_name = dictionary_teacher['first_name']
        self.last_name = dictionary_teacher['last_name']

    def to_dict(self):
        return {'id': self.id, 'first_name': self.first_name, 'last_name': self.last_name}

    def print(self):
        print (
            f"Teacher Information\n"
            f"-------------------\n"
            f"ID        : {self.id}\n"
            f"First Name: {self.first_name}\n"
            f"Last Name : {self.last_name}"
        )

test = Teacher()
test.print()
