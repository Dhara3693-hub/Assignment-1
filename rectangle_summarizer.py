# %%
import csv

area_list=[]

with open('rectangles_data.csv', newline="") as f:
    reader = csv.reader(f)
    next(reader)

    for row in reader:
        width = float(row[1])
        length = float(row[2])

        area = width * length
        area_list.append(area)

# Calculate summary statistics
total_count = len(area_list)
total_area = sum(area_list)
average_area = total_area / total_count if total_count > 0 else 0
maximum_area = max(area_list) if area_list else 0
minimum_area = min(area_list) if area_list else 0

# Print summary statistics
summary = {
    'Total_Count': total_count,
    'Total_Area': total_area,
    'Average_Area': average_area,
    'Maximum_Area': maximum_area,
    'Minimum_Area': minimum_area
}

for key, value in summary.items():
    print(f"{key}: {value}")

# Write summary to CSV
with open("summary.csv", 'w', newline="") as f:
    writer = csv.writer(f)
    writer.writerow(summary.keys())
    writer.writerow(summary.values())