import sqlite3

def add_major_course(course_name, course_description, course_units, course_prereqs, selected=0):
    with sqlite3.connect('prereqtest.db') as conn:
        conn.execute(
            """
            INSERT INTO major_courses (course_name, course_description, course_units, course_prereqs, selected)
            VALUES (?, ?, ?, ?, ?);
            """,
            (course_name, course_description, course_units, course_prereqs, selected)
        )
        conn.commit()
        conn.close()

#add_major_course("MATH 175", "Pre-Calculus", 6, "Prerequisite(s): MATH 150 or MATH 151 or direct placement based on multiple measures.")
#add_major_course("CS 111", "Introduction to Programming Concepts and Design", 4, "Strongly recommended: ENGL 101.")