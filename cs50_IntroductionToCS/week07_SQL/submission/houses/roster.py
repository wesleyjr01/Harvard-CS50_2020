import sys
import cs50

# Create database
db = cs50.SQL("sqlite:///students.db")

if len(sys.argv) != 2:
    print("we need argv=2")
    sys.exit()
else:
    query = f'SELECT * FROM students WHERE house = "{str(sys.argv[1])}"  ORDER BY last ASC, first ASC;'
    return_dict = db.execute(query)
    for element in return_dict:
        if element["middle"]:
            print(
                f"{element['first']} {element['middle']} {element['last']}, born in {element['birth']}"
            )
        else:
            print(f"{element['first']} {element['last']}, born in {element['birth']}")
