# Import necessary libraries
import requests
from bs4 import BeautifulSoup
import sqlite3

# Retrieve webpage HTML and parse using BeautifulSoup
webpage = requests.get("http://catalog.citruscollege.edu/disciplines/computer-science/computer-science-adt/#requirementstext")
soup = BeautifulSoup(webpage.content, "html.parser")

# Find all table cells in the parsed HTML
table_data = soup.find_all("td")

# Connect to database
conn = sqlite3.connect('major.db')

# Create SQL table
conn.execute('''CREATE TABLE major_courses
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             course_name TEXT NOT NULL,
             course_description TEXT NOT NULL,
             course_units TEXT NOT NULL);''')

# Loop through the table data and insert rows into the SQL table
i = 0
while i < len(table_data)-2:
    if "or" not in table_data[i].get_text():
        # If there is no "or" in the class name, add the name, description, and units to a new row
        course_name = table_data[i].get_text().replace('\xa0', " ")
        course_description = table_data[i+1].get_text().replace('\xa0', " ")
        course_units = table_data[i+2].get_text()
        conn.execute(f"INSERT INTO major_courses (course_name, course_description, course_units) \
                      VALUES ('{course_name}', '{course_description}', '{course_units}');")
        i += 3
    else:
        # If there is an "or" in the class name, add the name, description, and units to a new row
        # using the previous class's units
        course_name = table_data[i].get_text().replace('\xa0', " ")
        course_description = table_data[i+1].get_text()
        course_units = table_data[i-1].get_text()
        conn.execute(f"INSERT INTO major_courses (course_name, course_description, course_units) \
                      VALUES ('{course_name}', '{course_description}', '{course_units}');")
        i += 2

# Save changes and close connection
conn.commit()
conn.close()
