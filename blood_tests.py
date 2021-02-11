def interface():
    print("Blood Test Analysis")
    while True:
        print("Options")
        print("1 - HDL")
        print("2 - LDL")
        print("9 - Quit")
        choice = input("Enter an option: ")
        if (choice == "9"):
            return
        elif (choice == "1"):
            HDL_driver()
        elif (choice == "2"):
            LDL_driver()

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


def output_LDL(LDL, analysis):
    print("The LDL entered was {}".format(LDL))
    print("The level is {}".format(analysis))
    
def get_LDL_input():
    inputLDL = input("Enter an LDL value: ")
    return int(inputLDL)

def analyze_LDL(data):
    analysis = ""
    if (data < 130):
        analysis = "Normal"
    elif (130 <= data <= 159):
        analysis = "Borderline High"
    elif (160 <= data <= 189):
        analyis = "High"
    elif (data > 190):
        analysis = "Very High"
    return analysis

def LDL_driver():
    #Get Data
    data = get_LDL_input()
    #Analyze Data
    analysis = analyze_LDL(data)
    #Output Data
    output_LDL(data, analysis)

if __name__=="__main__":
    interface()
