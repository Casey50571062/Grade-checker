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
    return failed

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
        return failed

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
            return failed

failed = 0
print("\nTotal per english exam is 120 marks")
eng1 = int(input("Enter your first english paper mark: "))
eng2 = int(input("Enter your second english paper mark: "))
eng3 = int(input("Enter your third english paper mark: "))
failed += Carramel_Dansen_english(eng1,eng2,eng3)

print("\nTotal per maths exam is 100 marks")
mth1 = int(input("Enter your first math paper mark: "))
mth2 = int(input("Enter your second math paper mark: "))
mth3 = int(input("Enter your third math paper mark: "))
failed += Carramel_Dansen_math(mth1,mth2,mth3)

print("\nTotal per science exam is 150 marks")
sci1 = int(input("Enter your first science paper mark: "))
sci2 = int(input("Enter your second science paper mark: "))
sci3 = int(input("Enter your third science paper mark: "))
failed += Carramel_Dansen_science(sci1,sci2,sci3)

print(f"\nYou failed {failed} tests out of 9")
if failed>=3:
    print("You need to resit :3")