class Facility:
  name = ""
  # list to maintain all Facilities
  facilities_list = []

  def __init__(self, name):
    self.name = name
    self.facilities_list.append(self)

  def list_facilities(self):
    d = print("The hospital facilities are:\n Ambulance\n Admissions\n Cantenn\n Emergency\n")
    print(d)
    print("\nBack to the previous menu\n")

  def add_facility(self):
    dname = input("\nEnter facility name:\n")
    d = print("The hospital facilities are: \nAmbulance \n Admissions\n Cantenn\n Emergency\n Covid Care\n")
    
    self.facilities_list.append(Facility(dname))
    print("\nBack to the previous menu\n")
    

  def writeListOfFacilities(self):
    d = print("The hosipital facilities are: \nAmbulance \n Admissions \n Cantenn \n Emergency\n")
    d.write("Facilities List:")
    for facility in self.facilities_list:
      if facility.name == self.name:
        self.facilities_list.remove(facility)
      else:
        d.write("\n" + facility.name)
    d.close()

  def facility_menu(self):
    while 1:
      print("Facility Menu")
      print("1 - Display Facilities list")
      print("2 - Add Facility")
      print("3 - Back to the Main Menu")
      choice = int(input("\nEnter your choice:\n"))
      if choice ==1:
        self.list_facilities()
      elif choice == 2:
        self.add_facility()
      elif choice == 3:
        Management.DisplayMenu()
      else:
        print("Invalid choice")
        self.facility_menu() 

class Management:
  def DisplayMenu():
    while 1:
      #Objects of the classes with dummy data
      fac = Facility('Ambulance')

      print("\nWelcome to Alberta Hospital (AH) Management System")
      print("Select from the following options, or select 0 to stop:")
      print("1. Doctors")
      print("2. Facilities")
      print("3. Laboratories")
      print("4. Patients")
      print("Enter your choice:")
      choice = int(input())
      
      if choice == 2:
        fac.facility_menu()
      elif choice == 0:
        exit(0)
      else:
        print("Invalid choice")
        continue
if __name__ == "__main__":
  Management.DisplayMenu()                
      
