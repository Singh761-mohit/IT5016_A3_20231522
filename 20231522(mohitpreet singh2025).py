def staff_info():
    DATE=str(input("enter the date:"))
    STAFF_ID=input("enter the staff id:")
    STAFF_NAME=str(input("enter the staff name:"))
    counter=+1
    REQUISITION_ID=10000+counter
    return DATE,STAFF_ID,STAFF_NAME,REQUISITION_ID
DATE,STAFF_ID,STAFF_NAME,REQUISITION_ID= staff_info()
print("Printing staff information:")
print("DATE:", DATE)
print("STAFF ID:",STAFF_ID)
print("STAFF NAME:",STAFF_NAME)
print("REQUISITION ID:",REQUISITION_ID)

def requisitions_total():
    staff_info()
    total = 0
    x=int(input("how many thing you want?"))
    for i in range(x):
        item_name=input("enter the name of your material :")
        price=int(input("enter the price for your material "))
        total += price
    print("TOTAL PRICE FOR MATERIALS IS :",total)
    return total
requisitions_total()

def  requisition_approval():
    total=requisitions_total()
    status="Pending"
    approval_reference_number= None

    if total<500: 
        status="approved" 
        approval_reference_number=f"{STAFF_ID} {str(REQUISITION_ID) [-3:]}"


    print("total",total)
    print("status", status)
    print("approval reference number ",approval_reference_number)
    return  status,total,approval_reference_number
requisition_approval()

def display_requisitons():
    
    status,total,approval_reference_number=requisition_approval()
    
    print("printing requisitions")          
    print("Date:",DATE)
    print("staff name:",STAFF_NAME)
    print("staff id:",STAFF_ID)
    print("requisition id:",REQUISITION_ID)
    print("total",total)
    print("status:",status)
    print("Approval number",approval_reference_number)
    
display_requisitons()

