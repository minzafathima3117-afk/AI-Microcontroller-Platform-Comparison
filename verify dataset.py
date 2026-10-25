
import csv
import os

FILE_NAME = "Python dataset - Sheet1.csv"

if not os.path.exists(FILE_NAME):
    print("CSV file not found!")
    print("Check the filename and folder.")
else:
    with open(FILE_NAME, "r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    print("DATASET VERIFICATION REPORT")
    print("===========================")
    print("Total platforms:", len(rows))
    print()
    
# Check expected clock speeds
expected_speeds = {
    "Arduino Uno R3": 16,
    "ESP32": 240,
    "STM32 Blue Pill": 72,
    "Raspberry Pi Pico": 133
}

print("CLOCK SPEED VERIFICATION")
print("------------------------")

for row in rows:
    platform = row.get("Platform", "").strip()
    speed = row.get("Clock Speed", "").strip()
print("DEBUG - Platform:", platform)
print("DEBUG - Clock Speed:", repr(speed))
print()

if platform in expected_speeds:
        if str(expected_speeds[platform]) in speed:
            print(platform, "- Clock speed value found:", speed)
        else:
            print(platform, "- Please verify clock speed:", speed)

print()



missing_count = 0
    # Check for duplicate platforms
platform_names = [row.get("Platform", "").strip() for row in rows]
if len(platform_names) == len(set(platform_names)):
    print("No duplicate platforms found!")
else:
    print("Warning: Duplicate platforms found!")

print()

for row in rows:
        platform = row.get("Platform", "Unknown")
        print("Platform:", platform)

        for column, value in row.items():
            if value is None or value.strip() == "":
                print("  Missing information:", column)
                missing_count += 1

        print()

print("===========================")
if missing_count == 0:
        print("Great! No missing values found.")
else:
        print("Total missing values:", missing_count)

print("Verification completed!")

