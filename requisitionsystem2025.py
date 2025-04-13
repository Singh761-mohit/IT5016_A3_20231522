class requisitionsystem:
    # Constructor method to initialize the object with attributes

    def __init__(self, DATE, STAFF_ID, STAFF_NAME, STATUS):
        self.DATE=DATE
        self.STAFF_ID=STAFF_ID
        self.staff_NAME=STAFF_NAME
        self.status=STATUS
        
    # Method to collect staff information and assign a requisition ID
    def staff_info(self, counter,):
        self.DATE=str(input("enter the date:"))
        self.STAFF_ID=input("enter the staff id:")
        self.STAFF_NAME=str(input("enter the staff name:"))
        self.counter=+1
        self.REQUISITION_ID=10000+counter
        
        # Print the collected staff info
        print("Printing staff information:")
        print("DATE:",self.DATE)
        print("STAFF ID:",self.STAFF_ID)
        print("STAFF NAME:",self.STAFF_NAME)
        print("REQUISITION ID:",self.REQUISITION_ID)

    # Method to enter details of requested items and calculate total price
    def requisitions_details(self):
        total = 0
        x=int(input("how many thing you want?"))
        for i in range(x):
            item_name=input("enter the name of your material :")
            price=int(input("enter the price for your material "))
            total += price
        print("TOTAL PRICE FOR MATERIALS IS :",total)
        return total

    # Method to decide approval based on total price
    def requisition_approval(self,):
        total=self.requisitions_details()
        status="Pending"
        approval_reference_number= None
        # Approve if total price is below 500
        if total<500: 
            status="approved" 
            approval_reference_number=f"{self.STAFF_ID} {str(self.REQUISITION_ID) [-3:]}"

        # Print approval result
        print("total",total)
        print("status", status)
        print("approval reference number ",approval_reference_number)
        return  status,total,approval_reference_number
   
    

    def display_requisitons(self):
        status,total,approval_reference_number=self.requisition_details()
        
        
        print("printing requisitions")          
        print("Date:",self.DATE)
        print("staff name:",self.STAFF_NAME)
        print("staff id:",self.STAFF_ID)
        print("requisition id:",self.REQUISITION_ID)
        print("total",total)
        print("status:",status)
        print("Approval number",approval_reference_number)
counter = 1      
requisition = requisitionsystem("","","","")


requisition.staff_info(counter)
requisition.display_requisitons()
               
  
        




            
