"""[Onsite Day1] Drop Drop"""
def main():
    """print [Onsite Day1] Drop Drop"""
    grade_semeter1 = float(input())
    if grade_semeter1 < 1.00:
        print("I'm so sad.")
    elif grade_semeter1 < 2.00:
        grade_semeter2 = 4 - grade_semeter1
        print("%.2f"%grade_semeter2)
    else:
        print("I'm so happy.")
main()
