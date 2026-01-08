# student_grade.py
# Program to calculate student grade
import sys

def calculate_average(m1, m2, m3):
    return (m1+m2+m3)/3
def assign_grade(avg):    
    if avg >= 90:
        return "S"
    elif avg >= 80:
        return "A"
    elif avg >= 65:
        return "B"
    elif avg >= 50:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "F"

if __name__ == "__main__":
    import sys
    print("=== Student Grade Calculator ===")

    try:
        if len(sys.argv) == 7:
            # Case 1: Arguments passed (CLI / Jenkins)
            name = sys.argv[1]
            department = sys.argv[2]
            semester = sys.argv[3]
            m1 = float(sys.argv[4])
            m2 = float(sys.argv[5])
            m3 = float(sys.argv[6])
        else:
            # Case 2: Console input
            name = input("Enter Student Name: ")
            department = input("Enter Department: ")
            semester = input("Enter Semester: ")
            m1 = float(input("Enter Marks in Subject 1: "))
            m2 = float(input("Enter Marks in Subject 2: "))
            m3 = float(input("Enter Marks in Subject 3: "))

        print("\n=== Student Details ===")
        print(f" student Name: {name}")
        print(f"Department: {department}")
        print(f"Semester: {semester}")
        print(f"Marks: {m1}, {m2}, {m3}")
        
        average = calculate_average(m1, m2, m3)
        grade = assign_grade(average)
        
        print(f"\nAverage = {average:.2f}")
        print(f"Grade = {grade}")
        
    except ValueError:
        print("Invalid input! Please enter numeric values for marks.")