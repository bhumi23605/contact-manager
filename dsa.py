import os
import csv

csv_file = "contacts.csv"
FIELDS = ["Name", "Phone1", "Phone2", "Email", "WhatsApp", "LinkedIn", "Instagram"]

if not os.path.exists(csv_file):
    with open(csv_file, 'w', newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()

def add_contact(contact_data):
    with open(csv_file, 'a', newline="", encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writerow(contact_data)

def view_contact():
    contacts = []
    with open(csv_file, 'r', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            contacts.append(row)
    return contacts

def search_contact(query):
    results = []
    with open(csv_file, "r", encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Check if query appears in ANY field (case-insensitive)
            if any(query.lower() in str(value).lower() for value in row.values()):
                results.append(row)
    return results


def update_contact(name, new_data):
    rows = []
    updated = False
    with open(csv_file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["Name"].lower() == name.lower():
                rows.append(new_data)
                updated = True
            else:
                rows.append(row)
    if updated:
        with open(csv_file, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDS)
            writer.writeheader()
            writer.writerows(rows)
        return True
    return False

def delete_contact(name):
    rows = []
    deleted = False
    with open(csv_file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['Name'].lower() != name.lower():
                rows.append(row)
            else:
                deleted = True
    if deleted:
        with open(csv_file, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDS)
            writer.writeheader()
            writer.writerows(rows)
    return deleted
            
                
                
        
         

                
