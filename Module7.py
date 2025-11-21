#Module 7
#Key-Value Pairs: Room Number
RoomNum = {
    "CSC101": "3004",
    "CSC102": "4501",
    "CSC103": "6755",
    "NET110": "1244",
    "COM241": "1411",
}
#Key-Value Pairs: Instructors
Instructors = {
    "CSC101": "Haynes",
    "CSC102": "Alvarado",
    "CSC103": "Rich",
    "NET110": "Burke",
    "COM241": "Lee",
}
#Key-Value Pairs: Meeting Times
MtgTime = {
    "CSC101": "8:00 a.m.",
    "CSC102": "9:00 a.m.",
    "CSC103": "10:00 a.m.",
    "NET110": "11:00 a.m.",
    "COM241": "1:00 p.m.",
}

course = "none"
for course in RoomNum:
    course = input("Please enter your course number:\n")
    while course not in RoomNum:
        course = input("That course was not found. \nPlease Enter your course number:")
    print("\nRoom Number:",RoomNum[course], "\nInstructor ",Instructors[course], "\nMeeting at", MtgTime[course])
    break




