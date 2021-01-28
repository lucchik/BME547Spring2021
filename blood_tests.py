def interface():
    print("Blood Test Analysis")
    while True:
        print("Options")
        print("1 - HDL")
        print("9 - Quit")
        choice = input("Enter an option: ")
        if choice == "9":
            return
        elif (choice == "1"):
            HDL_driver()

def get_HDL_input():
    inputHDL = input("Enter an HDL value: ")
    return int(inputHDL)

def analyze_HDL(data):
    analysis = "Low"
    if (data >= 60):
        analysis = "Normal"
    elif (40 <= data < 60):
        analysis = "Borderline Low"
    return analysis

def output_HDL(HDL, analysis):
    print("The HDL entered was {}".format(HDL))
    print("The level is {}".format(analysis))
    
def HDL_driver():
    #Get Data
    data = get_HDL_input()
    #Analyze Data
    analysis = analyze_HDL(data)
    #Output Data
    output_HDL(data,analysis)

interface()
