import openpyxl
import pandas as pd

# Define the path to your file
file_path = 'libsys1.tt1'

# Initialize lists to store data
data = {
    "S.No.": [],
    "Accn No.": [],
    "Title": [],
    "Author": [],
    "Place": [],
    "Publisher": [],
    "Year": [],
    "Edition": []
}

# Read the file
with open(file_path, 'r') as file:
    lines = file.readlines()

# Parse the data
for line in lines:
    # Skip empty lines or lines that don't start with a digit
    if not line.strip() or not line[0].isdigit():
        continue

    # Split the line into fields
    fields = line.split()

    # Check if there are enough fields
    if len(fields) < 8:
        # If not, skip this line
        continue

    # Extract data from the line
    s_no = fields[0]
    accn_no = fields[1]
    title = ' '.join(fields[2:-6])  # Join remaining fields as title
    author = fields[-6] if len(fields) >= 7 else ""
    place = fields[-5]
    publisher = fields[-4]
    year = fields[-3]
    edition = fields[-2]

    # Append data to respective lists
    data["S.No."].append(s_no)
    data["Accn No."].append(accn_no)
    data["Title"].append(title)
    data["Author"].append(author)
    data["Place"].append(place)
    data["Publisher"].append(publisher)
    data["Year"].append(year)
    data["Edition"].append(edition)

# Create DataFrame
df = pd.DataFrame(data)

# Save DataFrame to Excel file using openpyxl
with pd.ExcelWriter('hhh.xlsx', engine='openpyxl') as writer:
    df.to_excel(writer, index=False)

print("Data saved to Excel successfully.")
