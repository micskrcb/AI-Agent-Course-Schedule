class Course:
    def __init__(self, code, title, name, instructor, prerequisites, timings):
        """
        Initialize a course with its attributes.
        :param code: Unique code for the course
        :param title: Course title
        :param name: Course name
        :param instructor: Instructor's name
        :param prerequisites: List of prerequisite course codes
        :param timings: 2D list representing the schedule (5 days, 12 hours/day)
        """
        self.code = code
        self.title = title
        self.name = name
        self.instructor = instructor
        self.prerequisites = prerequisites
        self.timings = timings

    def __str__(self):
        # Convert timings into a readable format
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


# Function to check courses with timings as a subset of input timings
def find_courses_by_timings(courses, input_timings):
    matching_courses = []
    
    for course in courses:
        # Check if all the occupied slots of the course are in the input timings
        all_timings_match = True
        for day, day_schedule in enumerate(course.timings):
            for hour, occupied in enumerate(day_schedule):
                if occupied and not input_timings[day][hour]:
                    all_timings_match = False
                    break
            if not all_timings_match:
                break
        
        if all_timings_match:
            matching_courses.append(course)
    
    return matching_courses


# Creating more dummy courses for testing
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

timings4 = empty_timings()
timings4[0][2] = True  # Monday, 10 AM
timings4[2][5] = True  # Wednesday, 1 PM
timings4[4][6] = True  # Friday, 2 PM

course4 = Course(
    code="CS301",
    title="Advanced Algorithms",
    name="CS301",
    instructor="Dr. Alice Cooper",
    prerequisites=["CS201"],
    timings=timings4
)

timings5 = empty_timings()
timings5[1][1] = True  # Tuesday, 9 AM
timings5[3][3] = True  # Thursday, 11 AM

course5 = Course(
    code="CS401",
    title="Operating Systems",
    name="CS401",
    instructor="Dr. Sam Harris",
    prerequisites=["CS201"],
    timings=timings5
)

timings6 = empty_timings()
timings6[2][3] = True  # Wednesday, 11 AM
timings6[4][5] = True  # Friday, 1 PM

course6 = Course(
    code="CS501",
    title="Computer Networks",
    name="CS501",
    instructor="Dr. Steve Brown",
    prerequisites=["CS301"],
    timings=timings6
)

# Creating a list of all courses
courses = [course1, course2, course3, course4, course5, course6]

# Sample input timings to search (matching courses on Monday 10 AM, Wednesday 1 PM)
input_timings = empty_timings()
input_timings[0][2] = True  # Monday, 10 AM
input_timings[2][5] = True  # Wednesday, 1 PM

# Find courses with the matching timings
matching_courses = find_courses_by_timings(courses, input_timings)

# Print the matching courses
for course in matching_courses:
    print(course)
    print()