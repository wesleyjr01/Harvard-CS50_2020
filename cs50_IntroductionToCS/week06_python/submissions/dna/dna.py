import re
import sys
import csv


def fullstring(s):
    new = ""
    for x in s:
        new += x
    return new


def find_maxval(s):
    sums = [len(i) for i in s]
    return max(sums) + 1


new_dict = {}
STRS = ["AGATC", "AATG", "TATC"]
with open(sys.argv[2], "r") as genomefile:
    text = genomefile.read()
    # print(text)
    for base in STRS:
        start_idx = [m.start() for m in re.finditer(base, text)]
        end_idx = [m.end() for m in re.finditer(base, text)]
        boolmask_vector = ["0"] + [
            "1" if start_idx[i] - start_idx[i - 1] == len(base) else "0"
            for i in range(1, len(start_idx))
        ]
        boolmask = fullstring(boolmask_vector).split("0")
        # print(boolmask)
        maxval = find_maxval(boolmask)
        new_dict[base] = maxval
# print(f"new genome: {new_dict}")
with open(sys.argv[1], "r") as csvfile:
    dna_map = csv.DictReader(csvfile)
    for row in dna_map:
        match_counter = 0
        for base in STRS:
            if int(row[base]) == int(new_dict[base]):
                match_counter += 1
        # print(match_counter)
        if match_counter == len(STRS):
            print(row["name"])
            sys.exit()
    print("No match")
