import json

import teacher


class Teachers:
    def __init__(self):
        self.teachers = []  # initialize once

        try:
            with open("teachers.json", "r", encoding="utf-8") as f:
                data_dicts = json.load(f)
                # convert each dict to Teacher object
                self.teachers = [
                    teacher.Teacher(dic['id'], dic['first_name'], dic['last_name'])
                    for dic in data_dicts
                ]
        except (FileNotFoundError, json.JSONDecodeError):
            # file missing or invalid JSON → keep self.teachers as empty list
            pass

    def save_teachers_data(self):
        # Convert Teacher objects to dictionaries
        records = [record.to_dict() for record in self.teachers]

        # Save to JSON (auto-creates file if missing)
        with open("teachers.json", "w", encoding="utf-8") as f:
            json.dump(records, f, indent=2)

    def create_teacher(self, first_name, last_name):
        self.teachers.append(teacher.Teacher(first_name, last_name))


data_teachers = Teachers()
data_teachers.create_teacher("Dope","Dope")
data_teachers.save_teachers_data()