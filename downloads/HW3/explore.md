# Assignment 4 - Explore My Little Pony Dataset
## Antoine Malenfant - 261051198

Before starting the analysis, the dataset was added to the "downloads" folder of my EC2.

-	_How big is the dataset?_

**Commands used**: 
1. ls -lh clean_dialog.csv
2. wc -l clean_dialog.csv

The dataset is 4.7 MB, which was found by command 1. above. It has 36860 rows (including the header), found by command 2. 

-	_What’s the structure of the data? (i.e., what are the field and what are values in them)_

**Commands used**: 
1. head -n 1 clean_dialog.csv
2. head -n 6 clean_dialog.csv
3. tail -n 5 clean_dialog.csv
4. csvtool col 1-4 clean_dialog.csv

From the 1st command, we are able to obtain the column headers, which are: "title","writer","pony","dialog". We hence know that the dataset had 4 columns. Using commands 2 and 3, we are able to obtain 5 additional lines at the start and end of the datafile. From the final command, 4, we are able to inspect the value types. In "title", we can observe the title of the episode. In "writer", we observe the author of the episode. In "pony" we see which pony is talking, and in "dialog" we see the dialog that is being said by the "pony" character. Note that all values are strings. 


-	_How many episodes does it cover?_

**Commands used**: 
1. csvtool col 1 clean_dialog.csv | tail -n +2 | sort | uniq | wc -l

From command 1, we looked at the first column "title", 2nd column downwards, sorting the episodes and keeping a unique one of each. Finally, this list was counted. There is hence 197 unique episodes in the dataset. 

-	_During the exploration phase, find at least one aspect of the dataset that is unexpected – meaning that it seems like it could create issues for later analysis._

One issue that arose is that many dialog entries contain escaped quotes ("") within the text, which could cause parsing issues depending on the analysis tool used. 

Another issue is that there are multiple characters in a single field. For example, some entries have multiple characters in the "pony" field (e.g., "Apple Bloom and Scootaloo", "Narrator and Twilight Sparkle").

## Analyze Speaker Frequency. 

**Commands used**:
1. grep -c "Twilight Sparkle" clean_dialog.csv
2. grep -c "Rarity" clean_dialog.csv
3. grep -c "Pinkie Pie" clean_dialog.csv
4. grep -c "Rainbow Dash" clean_dialog.csv
5. grep -c "Fluttershy" clean_dialog.csv

**Find the total lines of dialog and percent per pony** 

nano percent_counter.py

{
import csv
filename = "clean_dialog.csv"
main_ponies = main_ponies = ["Twilight Sparkle", "Rarity", "Pinkie>
counts = {pony: 0 for pony in main_ponies}
total_lines = 0
with open(filename, newline='', encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        total_lines += 1
        pony_name = row["pony"]
        for pony in main_ponies:
            if pony in pony_name:
                counts[pony] += 1
with open("Line_percentages.csv", "w", newline='', encoding="utf-8>
    writer = csv.writer(out)
    writer.writerow(["pony_name", "total_line_count", "percent_all>
    for pony, cnt in counts.items():
        percent = (cnt / total_lines) * 100
        writer.writerow([pony, cnt, f"{percent:.4f}"])
}

python3 percent_counter.py