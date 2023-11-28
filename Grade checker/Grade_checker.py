eng = {}
mth = {}
sci = {}
totalFail=0

def Carramel_Dansen_english(A,B,C):
    failed = 0
    if A >= 104:
            print("Passed english test 1 :3")
    else:
            print("Failed english test 1 :(")
            failed+=1
    if B >= 84:
            print("Passed english test 2 :3")
    else:
            print("Failed english test 2 :(")
            failed+=1
    if C >= 64:
            print("Passed english test 3 :3")
    else:
            print("Failed english test 3 :(")
            failed+=1
    Total = A+B+C
    Avg = Total // 3
    print(f"Your total was {Total}/360")
    print(f"Your average was {Avg}/120")
    return failed, Avg, Total

def Carramel_Dansen_math(A,B,C):
        failed = 0
        if A >= 78:
            print("Passed math test 1 :3")
        else:
            print("Failed math test 1 :(")
            failed+=1
        if B >= 64:
            print("Passed math test 2 :3")
        else:
            print("Failed math test 2 :(")
            failed+=1
        if C >= 56:
            print("Passed math test 3 :3")
        else:
            print("Failed math test 3 :(")
            failed+=1
        Total = A+B+C
        Avg = Total // 3
        print(f"Your total was {Total}/300")
        print(f"Your average was {Avg}/100")
        return failed, Avg, Total

def Carramel_Dansen_science(A,B,C):
            failed = 0
            if A >= 128:
                print("Passed science test 1 :3")
            else:
                print("Failed science test 1 :(")
                failed+=1
            if B >= 113:
                print("Passed science test 2 :3")
            else:
                print("Failed science test 2 :(")
                failed+=1
            if C >= 96:
                print("Passed science test 3 :3")
            else:
                print("Failed science test 3 :(")
                failed+=1
            Total = A+B+C
            Avg = Total // 3
            print(f"Your total was {Total}/450")
            print(f"Your average was {Avg}/150")
            return failed, Avg, Total

def inputGrade(subject):
    eng = {}
    mth = {}
    sci = {}
    if subject == "english":
        for x in range(3):
            while True:
                try:
                    eng[x] = int(input(f"Enter your first {x+1} english paper mark: "))
                    if eng[x]<0 or eng[x]>120:
                        print("There is no such thing as a negative mark")
                    else:
                        break
                except ValueError:
                    print("Invalid Number")
        return eng
    if subject == "math":
        for x in range(3):
            while True:
                try:
                    mth[x] = int(input(f"Enter your first {x+1} math paper mark: "))
                    if mth[x]<0 or mth[x]>100:
                        print("There is no such thing as a negative mark")
                    else:
                        break
                except ValueError:
                    print("Invalid Number")
        return mth
    if subject == "science":
        for x in range(3):
            while True:
                try:
                    sci[x] = int(input(f"Enter your {x+1} science paper mark: "))
                    if sci[x]<0 or sci[x]>150:
                        print("There is no such thing as a negative mark")
                    else:
                        break
                except ValueError:
                    print("Invalid Number")
        return sci

failed = 0  
MthAverage = 0
MthTotal= 0
print("\nTotal per math exam is 100 marks")
mth = inputGrade("math")
failed, MthAverage, MthTotal = Carramel_Dansen_math(mth[0], mth[1], mth[2])
totalFail+=failed

EngAvg = 0
EngTotal=0
print("\nTotal per english exam is 120 marks")
eng = inputGrade("english")
failed, EngAvg, EngTotal = Carramel_Dansen_english(eng[0],eng[1],eng[2],)
totalFail+=failed

SciAverage=0
SciTotal=0
print("\nTotal per science exam is 150 marks")
sci = inputGrade("science")
failed, SciAverage, SciTotal = Carramel_Dansen_science(sci[0],sci[1],sci[2])
totalFail+=failed

print(f"\nYou failed {totalFail} tests out of 9")
if totalFail>=3:
    print("You need to resit :3")
print(">:3")