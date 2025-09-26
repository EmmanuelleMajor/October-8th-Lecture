import csv
filename = "clean_dialog.csv"
main_ponies = main_ponies = ["Twilight Sparkle", "Rarity", "Pinkie Pie", "Rainbow Dash", "Fluttershy"]
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
with open("Line_percentages.csv", "w", newline='', encoding="utf-8") as out:
    writer = csv.writer(out)
    writer.writerow(["pony_name", "total_line_count", "percent_all_lines"])
    for pony, cnt in counts.items():
        percent = (cnt / total_lines) * 100
        writer.writerow([pony, cnt, f"{percent:.4f}"])
