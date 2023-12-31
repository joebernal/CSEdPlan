# while i < len(table_data) - 1:
#     if ":" in table_data[i].get_text() or "," in table_data[i].get_text():
#         if '.' in table_data[i+1].get_text():
#             current_table = clean_table_name(table_data[i+1].get_text())
#             print(table_data[i+1].get_text())
#             i += 2
#         else:
#             current_table = clean_table_name(table_data[i].get_text())
#             print(table_data[i].get_text())
#             i += 1
#     elif '.' in table_data[i].get_text():
#         current_table = clean_table_name(table_data[i].get_text())
#         print(table_data[i].get_text())
#         i += 1
#     else:
#         print(table_data[i].get_text())
#         print(table_data[i+1].get_text())
#         print(table_data[i+2].get_text())
#         i += 3

'''
# Loop through each table and add a column named "selected" with a default value of 0
for table_name in major_tables:
    cursor.execute(f"ALTER TABLE {table_name} ADD COLUMN selected INTEGER DEFAULT 0;")

for table_name in ge_tables:
    cursor.execute(f"ALTER TABLE {table_name} ADD COLUMN selected INTEGER DEFAULT 0;")
'''