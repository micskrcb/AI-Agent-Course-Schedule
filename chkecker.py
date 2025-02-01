import random

# Function to generate a 5x12 grid with True/False
def generate_student_schedule():
    return [[random.choice([True]) for _ in range(12)] for _ in range(5)]

# Generate the schedule for a dummy student
student_schedule = generate_student_schedule()
print("Student Schedule:")
for day in student_schedule:
    print(day)

class Course:
    def __init__(self, code, title, name, instructor, prerequisites, timings):
        self.code = code
        self.title = title
        self.name = name
        self.instructor = instructor
        self.prerequisites = prerequisites
        self.timings = timings

    def __str__(self):
        readable_timings = [
            f"Day {day + 1}: " +
            ", ".join([f"{8 + hour} AM" if hour < 4 else f"{hour - 4} PM"
                       for hour, occupied in enumerate(day_schedule) if occupied])
            for day, day_schedule in enumerate(self.timings)
        ]
        return f"Course Code: {self.code}\n" \
               f"Course Title: {self.title}\n" \
               f"Course Name: {self.name}\n" \
               f"Instructor: {self.instructor}\n" \
               f"Prerequisites: {', '.join(self.prerequisites) if self.prerequisites else 'None'}\n" \
               f"Timings:\n" + "\n".join(readable_timings)


# Helper function to create empty timings
def empty_timings():
    return [[False for _ in range(12)] for _ in range(5)]

# Creating dummy courses
timings1 = empty_timings()
timings1[0][2] = True  # Monday, 10 AM
timings1[2][5] = True  # Wednesday, 1 PM

course1 = Course(
    code="CS101",
    title="Introduction to Python",
    name="CS101",
    instructor="Dr. John Doe",
    prerequisites=[],
    timings=timings1
)

timings2 = empty_timings()
timings2[1][3] = True  # Tuesday, 11 AM
timings2[3][4] = True  # Thursday, 12 PM

course2 = Course(
    code="CS201",
    title="Data Structures",
    name="CS201",
    instructor="Dr. Jane Smith",
    prerequisites=["CS101"],
    timings=timings2
)

timings3 = empty_timings()
timings3[4][6] = True  # Friday, 2 PM

course3 = Course(
    code="AI301",
    title="Machine Learning Basics",
    name="AI301",
    instructor="Dr. Alan Turing",
    prerequisites=["CS201"],
    timings=timings3
)
completed_courses = ["Basic Mathematics", "Computer Literacy", "CS101"]
# Function to check courses matching free slots
def get_courses_matching_free_slots(student_schedule, courses,completed_courses):
    matching_courses = []

    for course in courses:
        timings = course.timings
        is_match = True

        # Compare each day's schedule
        for day_timing, day_free in zip(timings, student_schedule):
            for time, free_time in zip(day_timing, day_free):
                if time and not free_time:  # If course occupies a time student is not free
                    is_match = False
                    break

            if not is_match:
                break

        if is_match:
            if CheckPrereq(course,completed_courses):
                matching_courses.append(course)
    
        
        return matching_courses

def CheckPrereq(course, completed_courses):
    return all(prerequisite in completed_courses for prerequisite in course.prerequisites)

    
    


# Example usage
courses = [course1, course2, course3]
matching_courses = get_courses_matching_free_slots(student_schedule, courses,completed_courses)

# Print matching courses
print("\nMatching Courses:")
for course in matching_courses:
    print(course)
    print()

if not matching_courses:
    print("No matching courses found.")
