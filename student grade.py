class StudentGradeManager:
    def __init__(self):
        self.grades = {}  # Dictionary to store subject grades

    def add_grade(self, subject, grade):
        """Add a grade for a specific subject."""
        if subject in self.grades:
            self.grades[subject].append(grade)
        else:
            self.grades[subject] = [grade]

    def edit_grade(self, subject, index, new_grade):
        """Edit a grade for a specific subject."""
        if subject in self.grades and 0 <= index < len(self.grades[subject]):
            self.grades[subject][index] = new_grade
        else:
            print("Invalid subject or index.")

    def delete_grade(self, subject, index):
        """Delete a grade for a specific subject."""
        if subject in self.grades and 0 <= index < len(self.grades[subject]):
            del self.grades[subject][index]
            if not self.grades[subject]:  # Remove subject if no grades left
                del self.grades[subject]
        else:
            print("Invalid subject or index.")

    def calculate_average_grade(self):
        """Calculate the average grade across all subjects."""
        if not self.grades:
            return None  # Return None if no grades recorded
        total_sum = sum(sum(grades) for grades in self.grades.values())
        total_count = sum(len(grades) for grades in self.grades.values())
        return total_sum / total_count

    def calculate_letter_grade(self, grade):
        """Calculate the letter grade based on the numeric grade."""
        if grade >= 90:
            return 'A'
        elif grade >= 80:
            return 'B'
        elif grade >= 70:
            return 'C'
        elif grade >= 60:
            return 'D'
        else:
            return 'F'

    def calculate_gpa(self):
        """Calculate the GPA (Grade Point Average) based on letter grades."""
        letter_grades = [self.calculate_letter_grade(grade) for grades in self.grades.values() for grade in grades]
        if not letter_grades:
            return None  # Return None if no grades recorded
        grade_points = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0}
        total_grade_points = sum(grade_points[grade] for grade in letter_grades)
        return total_grade_points / len(letter_grades)

    def display_grades(self):
        """Display all recorded grades."""
        if not self.grades:
            print("No grades recorded.")
            return
        for subject, grades in self.grades.items():
            print(f"{subject}: {', '.join(map(str, grades))}")

# Usage example:
if __name__ == "__main__":
    manager = StudentGradeManager()

    # Adding grades for different subjects
    manager.add_grade('Math', 85)
    manager.add_grade('Math', 78)
    manager.add_grade('English', 92)
    manager.add_grade('Science', 88)

    # Displaying all recorded grades
    print("Recorded Grades:")
    manager.display_grades()

    # Calculating and displaying average grade
    average_grade = manager.calculate_average_grade()
    if average_grade is not None:
        print(f"Average Grade: {average_grade:.2f}")

    # Calculating and displaying GPA
    gpa = manager.calculate_gpa()
    if gpa is not None:
        print(f"GPA: {gpa:.2f}")

    # Editing a grade
    manager.edit_grade('Math', 0, 90)
    print("\nAfter editing Math grade:")
    manager.display_grades()

    # Deleting a grade
    manager.delete_grade('Science', 0)
    print("\nAfter deleting Science grade:")
    manager.display_grades()
