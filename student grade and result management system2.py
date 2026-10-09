students = []

while True:
    print("\n===== STUDENT RESULT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student")
    print("4. Update Student Marks")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        roll = input("Enter Roll Number: ")

        # Check for duplicate roll numbers
        if any(s["roll"] == roll for s in students):
            print("Roll number already exists!")
            continue

        name = input("Enter Student Name: ")

        marks = []

        for i in range(5):
            while True:
                try:
                    mark = float(input(f"Enter marks for Subject {i + 1}: "))

                    if 0 <= mark <= 100:
                        marks.append(mark)
                        break
                    else:
                        print("Marks must be between 0 and 100.")

                except ValueError:
                    print("Please enter a valid number.")

        total = sum(marks)
        percentage = total / 5

        if percentage >= 90:
            grade = "A"
        elif percentage >= 75:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        elif percentage >= 40:
            grade = "D"
        else:
            grade = "F"