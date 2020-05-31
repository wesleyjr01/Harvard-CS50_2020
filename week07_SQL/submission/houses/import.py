import sys
import csv
import cs50

# Create database
db = cs50.SQL("sqlite:///students.db")

if len(sys.argv) != 2:
    print("we need argv=2")
    sys.exit()
else:
    with open(sys.argv[1], "r") as csvfile:
        students_csv = csv.DictReader(csvfile)
        for student in students_csv:
            array_name = student["name"].split()
            if len(array_name) == 2:
                first_name = array_name[0]
                last_name = array_name[1]
                house = student["house"]
                birth = student["birth"]
                db.execute(
                    "INSERT INTO students (first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)",
                    first_name,
                    None,
                    last_name,
                    house,
                    birth,
                )
            elif len(array_name) == 3:
                first_name = array_name[0]
                middle_name = array_name[1]
                last_name = array_name[2]
                house = student["house"]
                birth = student["birth"]
                db.execute(
                    "INSERT INTO students (first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)",
                    first_name,
                    middle_name,
                    last_name,
                    house,
                    birth,
                )
