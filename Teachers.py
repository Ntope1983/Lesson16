import json

import teacher


def get_valid_input(last_number):
    while True:
        try:
            value = int(input(f"Enter a number (1 to {last_number}): "))
            if 1 <= value <= last_number:
                return value
            else:
                print(f"Number must be between 1 and {last_number}.")
        except ValueError:
            print("Invalid input. Please enter an integer.")


def get_name(prompt):
    while True:
        name = input(f"Enter {prompt}: ").strip()
        if not name:
            print(f"{prompt} must not be empty.")
        elif not name.isalpha():
            print(f"{prompt} must contain only letters.")
        else:
            return name


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
        same_name_teachers = [teacher for ter in self.teachers if
                              ter.first_name == first_name and ter.last_name == last_name]
        if not same_name_teachers:
            new_teacher = teacher.Teacher(None, first_name, last_name)
            self.teachers.append(new_teacher)
            return new_teacher
        else:
            print(f"there is a Teacher with first name {first_name} and lastname {last_name}")
            return None

    def read_teacher(self, teacher_id):
        for ter in self.teachers:
            if ter.id == teacher_id:
                return ter
        return None

    def update_teacher(self, teacher_id):
        update_teacher = self.read_teacher(teacher_id)
        if update_teacher:
            print("--------------------------------")
            print("Choose the field you want to update:")
            menu = ["1: Name", "2: Surname", "3: Both"]
            for option in menu:
                print(option, end="  ")
            choice = get_valid_input(3)
            if choice == 1:
                update_teacher.first_name = get_name("Name")
                return True
            elif choice == 2:
                update_teacher.last_name = get_name("Surname")
                return True
            else:
                update_teacher.first_name = get_name("Name")
                update_teacher.last_name = get_name("Surname")
                return True
        else:
            return False

    def delete_teacher(self, teacher_id):
        for ter in self.teachers:
            if ter.id == teacher_id:
                self.teachers.remove(ter)
        return None


data_teachers = Teachers()
data_teachers.delete_teacher(1006)
data_teachers.save_teachers_data()
