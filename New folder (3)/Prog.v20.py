# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
summary = []
histoList = [0 for i in range(4)]
passcredits = 0
defercredits = 0
failcredits = 0
multiInput = False
def outcome(passcredits, defercredits, failcredits):
    status = ""
    if passcredits == 120:
        print()
        print('Progress')
        status = "Progress"
    elif passcredits == 100:
        print()
        print('Progress (module trailer)')
        status = "Progress (module trailer)"
    elif failcredits >= 80:
        print()
        print('Exclude')
        status = "Exclude"
    elif (passcredits <= 80) and (failcredits <= 60):
        print()
        print('Module Retriver')
        status = "Module Retriver"
    appendString = status + " - " + str(passcredits) + ", " + str(defercredits) + ", " + str(failcredits)
    summary.append(appendString)
    

def validate(multiInput):
    global passcredits, defercredits, failcredits
    while True:
        try:
            passcredits = int(input('Enter your pass credits: '))
        except ValueError:
            print("Integer required")
        else:
            if passcredits in (0, 20, 40, 60, 80, 100, 120):
                break
            else:
                print('Out Of Range')
    while True:
        try:
            defercredits = int(input('Enter your defer credits: '))
        except ValueError:
            print("Integer required")
        else:
            if defercredits in (0, 20, 40, 60, 80, 100, 120):
                break
            else:
                print('Out Of Range')
    while True:
        try:
            failcredits = int(input('Enter your fail credits: '))
        except ValueError:
            print("Integer required")
        else:
            if failcredits in (0, 20, 40, 60, 80, 100, 120):
                break
            else:
                print('Out Of Range')
    totalcredits = passcredits + defercredits + failcredits
    if totalcredits == 120:
        outcome(passcredits, defercredits, failcredits)
        if multiInput:
            histogram(passcredits, failcredits)
            multioutcome()
    else:
        print('Total Incorrect')
        print()
        print('Re-running the program...........')
        print()
        validate(multiInput)


def teacherSummary():
    global summary
    summary = []
    histoList = [0 for i in range(4)]
    validate(True)
    print()
    print('List Outcomes')#part 3
    print('- '*30)
    for i in summary:
        print(i)

def multioutcome():
    print()
    print('Would you like to enter another set of data?')
    b = str(input('Enter "y" for yes or "q" to quit and view results: '))
    b = b.lower()
    if b == 'q':
        print('- '*30)
        global totaloutcomes
        totaloutcomes = histoList[0] + histoList[1] + histoList[2] + histoList[3]
        print("what kind of histogram do you want to print (Horizontal ('h') or Vertical ('v')?")
        print()
        choosehistro()
    elif b == 'y':
        print()
        validate(True)
    else:
        print()
        print('Enter a valid option')
        multioutcome()

def choosehistro():
    choice = str(input("'h' or 'v'? "))
    choice = choice.lower()
    if choice == 'h':
        print()
        histoprint(totaloutcomes)
    elif choice == 'v':
        print()
        v_histogram(totaloutcomes)
    else:
        print("try again, program accepts only 'h' or 'v'\n")
        choosehistro()

#progress = 0, trailer = 1, retriever = 2, exclude = 3

def histogram(passcredits, failcredits):
    global histoList
    if passcredits == 120:
        histoList[0] += 1
    elif passcredits == 100:
        histoList[1] += 1
    elif passcredits <= 80 and failcredits <= 60:
        histoList[2] += 1
    elif failcredits >= 80:
        histoList[3] += 1

def histoprint(totaloutcomes):
    global histoList
    print('Horizontal Histogram')
    print('- '*30)
    print()
    print('Progress ', histoList[0], '  : ', histoList[0] * '*')
    print('Trailer ', histoList[1], '  : ', histoList[1] * '*')
    print('Retriver ', histoList[2], '  : ', histoList[2] * '*')
    print('Exclude ', histoList[3], '  : ', histoList[3] * '*')
    print()
    print(totaloutcomes,' outcomes in total.')

def v_histogram(totaloutcomes):#part 2
    global histoList
    print()
    print('Vertical Histogram')
    print('- '*30)
    print()
    print('Progress Trailer Retriever Excluded')
    rowCount = 0
    for a in histoList:
        if a > rowCount:
            rowCount = a  #counts the number of rows by finding the count with the max value
    for x in range(rowCount):
        print('    ', end='')
        for i in range(4):
            if histoList[i] > 0:
                print(f"{'*':9}", end='')
                histoList[i] -=1
            else:
                print(f"{' ':9}", end='')
        print()
    print(totaloutcomes,' outcomes in total')

def textfile():#part 4
    print()
    print('credits saved into a file')
    print('- '*30)
    print()
    f = open('progression.txt','w')
    for i in summary:
        f.write(i)
        f.write('\n')
    f.close()
    
def readlist():#part 4
    print()
    print('reading file')
    print('- '*30)
    f = open('progression.txt','r')
    for line in f:
        print(line)

def main():
    print('Main Menu')
    print()
    print('1 : to run single student progression prediction')
    print('2 : to run multiple student progression prediction (Staff)')
    print('3 : to save to file and read from file (staff)')
    print('4 : to exit')
    print()
    try:
        choice = int(input("Enter Choice: "))
        if choice == 1:
            validate(False)
        elif choice == 2:
            print()
            teacherSummary()
        elif choice == 3:
            print()
            textfile()
            readlist()
        elif choice == 4:
            quit()
        else:
            print("Incorrect Input")
    except ValueError:
        print("Enter a integer in range of options (1 - 4)")
    print()
    print('- '*30)
    main()

main()      
