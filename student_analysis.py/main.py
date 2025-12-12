def student_analysis(marks):
    no_of=len(marks)
    avg_mark=sum(marks)/no_of
    high_mark=max(marks)
    low_mark=min(marks)


    
    tot_fail=0
    tot_pass=0

    grades = {"A":0, "B":0, "C":0, "D":0, "F":0}

    for m in marks:
        if m>= 40:
            tot_pass += 1
        else :
            tot_fail += 1

        if m >= 90:
            grades["A"] += 1
        elif m >= 75:
            grades["B"] += 1
        elif m >= 60:
            grades["C"] += 1
        elif m >= 40:
            grades["D"] += 1
        else:
            grades["F"] += 1
    pass_percentage = tot_pass*100/no_of
    fail_percentage = tot_fail*100/no_of

    return no_of,avg_mark, high_mark, low_mark, tot_pass, tot_fail, grades, pass_percentage, fail_percentage
def main():
    marks=list(map(int,input("enter marks:").split(',')))
    no_of, avg, high, low, passed, failed,grades,pass_percentage,fail_percentage = student_analysis(marks)
    print("total students:",no_of)
    print("average:", avg)
    print("highest:", high)
    print("lowest:", low)
    print("passed:", passed)
    print("failed:", failed)
    print("pass_percentage:",pass_percentage)
    print("Fail_percentage:",fail_percentage)
    

    print("\n grade distribution:")
    for grade, count in grades.items():
        print(grade, ":", count)
    
main()

            
    
    
    
