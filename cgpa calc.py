class StudentGradeTracker:
    def __init__(self):
        self.grades = {}

    def add_grade(self, subject, grade):
        """Add a grade for a specific subject"""
        self.grades[subject] = grade

    def calculate_average(self):
        """Calculate the average grade"""
        if not self.grades:
            return 0
        return sum(self.grades.values()) / len(self.grades)

    def get_letter_grade(self, average):
        """Convert the average grade to a letter grade"""
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        else:
            return 'F'

    def get_gpa(self, average):
        """Convert the average grade to a GPA"""
        if average >= 90:
            return 4.0
        elif average >= 80:
            return 3.0
        elif average >= 70:
            return 2.0
        elif average >= 60:
            return 1.0
        else:
            return 0.0

    def display_summary(self):
        """Display the overall grade summary"""
        if not self.grades:
            print("No grades available.")
            return

        print("\nGrade Summary:")
        for subject, grade in self.grades.items():
            print(f"{subject}: {grade}")

        average = self.calculate_average()
        letter_grade = self.get_letter_grade(average)
        gpa = self.get_gpa(average)

        print(f"\nAverage Grade: {average:.2f}")
        print(f"Letter Grade: {letter_grade}")
        print(f"GPA: {gpa:.2f}")


def main():
    tracker = StudentGradeTracker()

    print("Welcome to the Student Grade Tracker")
    while True:
        subject = input("\nEnter the subject (or 'done' to finish): ")
        if subject.lower() == 'done':
            break
        try:
            grade = float(input(f"Enter the grade for {subject}: "))
            tracker.add_grade(subject, grade)
        except ValueError:
            print("Invalid input. Please enter a numeric grade.")

    tracker.display_summary()


if __name__ == "__main__":
    main()
