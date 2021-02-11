def create_database_entry(name,id_no,age):
    new_patient = [name,id_no,age,[]]
    return new_patient


def main():
    db = list()
    db.append(create_database_entry("Ann Ables",1,30))
    db.append(create_database_entry("Boy Boyles",2,31))
    db.append(create_database_entry("Chris Chou",3,32))
    names = [i[0] for i in db]
    #print_directory(db)
    #find_patient(2,db)
    print(db)
    add_test_result(2,db,"HDL",65)
    print(db)
    add_test_result(2,db,"LDL",80)
    print(db)

def add_test_result(id_no,db,test_name,test_result):
    for patient in db:
        if patient[1] == id_no:
            patient[3].append((test_name,test_result))
    print(db)
    

def find_patient(id_no, db):
    for patient in db:
        if (patient[1] == id_no):
            print("------------------------------------")
            print("Name: {}, id: {}, age: {}\n".format(patient[0],patient[1],patient[2]))
            #print("Patient is in {}".format(other_data[i]))
            print("------------------------------------")
            break
        
def print_directory(db):
    #enumerate returns counter and item
    other_data = ["Room 2","Room 3","Room 4","Room 5"]
    for i,patient in enumerate(db):
        print("Name: {}, id: {}, age: {}".format(patient[0],patient[1],patient[2]))
        print("Patient is in {}".format(other_data[i]))

if __name__=="__main__":
    main()
    
    
    
    
