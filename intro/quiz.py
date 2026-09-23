class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course



def quiz1():
    q1 = "what is ALU?"
    ans1 = "arithmetic logic unit"
    userInput1 = input(f"{q1}: ").lower()

    if ans1 == userInput1:
        return True
    else:
        return False
    
def quiz2():
    q2 = "what is ROM?"
    ans2 = "read only memory"
    userInput2 = input(f"{q2}: ").lower()

    if ans2 == userInput2:
        return True
    else:
        return False
    
def quiz3():
    q3 = "what is OS?"
    ans3 = "operating system"
    userInput3 = input(f"{q3}: ").lower()

    if ans3 == userInput3:
        return True
    else:
        return False
    



if __name__ == '__main__':
    # quiz()
    # q1 = quiz()

    # score = 0

    # if quiz1():
    #     score += 1
    #     print("Correct")        
    # else:
    #     print("Bagsak")

    # if quiz2():
    #     score += 1
    #     print("Correct")
    # else:
    #     print("Bagsak")

    # if quiz3():
    #     score += 1
    #     print("Correct")
    # else:
    #     print("Bagsak")

    # print(f"SCORE: {score}")

    # print("SCORE: ", score)

    # stdnt1 = Student("ash", "DIT")
    # print(stdnt1.name)
    # print(stdnt1.course)
    
    # new_students = [
    #     ["ash", "DIT"],
    #     ["ley", "DIT"],
    #     ["jay", "DIT"]
    # ]

    # for stud in(new_students):
    #     # stud[0]
    #     s = Student(stud[0], stud[1])
    #     print(s)
    #     print(s.name)

    add_students = True
    student_objs = []
    while add_students:
        courses = ["DIT", "HMT", "RM"]
        name = input("Name: ")
        print(f"[0] DIT\n[1] HMT\n[2] RM")
        course_num = int(input())
        crs = courses[course_num]

        s = Student(name, crs)
        student_objs.append(s)

        add = input("TYPE EXIT TO STOP: ").lower()

        # print(s)
        if add == "exit":
            add_students = False
            # break
        # course = input()

    for obj in student_objs:
        print(obj)
        print(f"Name: {obj.name}")
        print(f"Course: {obj.course}")
        input()

