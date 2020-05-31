import csv

with open("title.basics.tsv", "r") as titles:
    reader = csv.DictReader(titles, delimiter="\t")

    with open("show0.csv", "w") as shows:
        writer = csv.writer(shows)

        writer.writerow(["tconst", "primaryTitle", "startYear", "genres"])

        for row in reader:

            if row["startYear"] == "\\N":
                continue

            year = int(row["startYear"])
            if year < 1970:
                continue

            if row["titleType"] == "tvSeries" and row["isAdult"] == "0":
                writer.writerow(
                    [
                        row["tconst"],
                        row["primaryTitle"],
                        row["startYear"],
                        row["genres"],
                    ]
                )
