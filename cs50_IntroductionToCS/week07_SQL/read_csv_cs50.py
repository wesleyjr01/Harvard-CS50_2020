import csv

counts = {}

# Open CSV file
with open(
    "CS50 2019 - Lecture 7 - Favorite TV Shows (Responses) - Form Responses 1.csv", "r"
) as file:

    # Create DictReader
    reader = csv.DictReader(file)

    # Iterate over CSV file, printing each title
    for row in reader:
        title = row["title"].lower()
        if title in counts:
            counts[title] += 1
        else:
            counts[title] = 1

for title, count in sorted(counts.items(), key=lambda item: item[1], reverse=True):
    print(f"title: {title}, count: {count}")
