password=input('Enter Spell: ').capitalize()

if password!='Alohomora':
        print('Try Again👿')
else:    
        class MagicalContact:
            def __init__(self, name, email, phone_no):
                self.__name = name
                self.__email = email
                self.__phone_no = phone_no

            def get_name(self):
                return self.__name

            def get_email(self):
                return self.__email

            def get_phone_number(self):
                 return self.__phone_no

            def set_email(self, email):
                self.__email = email

            def set_phone_number(self, phone_no):
                self.__phone_no = phone_no

            def describe(self):
                return (f"Name: {self.__name}, Email: {self.__email}, Phone Number: {self.__phone_no}")
        class WizardOrWitch(MagicalContact):
            def __init__(self, name, email, phone_no, house):
                super().__init__(name, email, phone_no)
                self.__house = house
                wand = {
                            'Gryffindor': ['Holly', 'Phoenix feather', '11 inches'],
                            'Slytherin': ['Yew', 'Dragon heartstring', '13 inches'],
                            'Ravenclaw': ['Walnut', 'Raven feather', '10 inches'],
                            'Hufflepuff': ['Cedar', 'Unicorn hair', '12 inches']
                        }
                self.__wand = {
                            'wood': wand[house][0],
                            'core': wand[house][1],
                            'length': wand[house][2]
        }
               


          
            def get_wand(self):
                return f"{self.__wand['wood']}, {self.__wand['core']}, {self.__wand['length']}"
          
            def get_house(self):
                return self.__house
            def describe(self):
                return f"{super().describe()} Wand: {self.get_wand()}, House: {self.__house}"
        class MagicalCreature(MagicalContact):
            
            def __init__(self, name, email, phone_no, species, tame):
                super().__init__(name, email, phone_no)
                self.__species = species
                self.__tame = tame
            def get_species(self):
                return self.__species
            def is_tame(self):
                return self.__tame

            def describe(self):
                return f"{super().describe()}, Species: {self.__species}, Tamed? (yes/no): {self.__tame}"
        class MagicalContactBook:
            def __init__(self):
                self.__contacts = []

            def add_contact(self, contact):
                self.__contacts.append(contact)

            def list_contacts(self):
                if self.__contacts:
                    for contact in self.__contacts:
                        print(contact.describe())
                else:
                    print("The contact book is empty.")

            def find_contact(self, name):
                for contact in self.__contacts:
                    if contact.get_name().lower() == name.lower():
                        return contact
                return None
                
              
        owner=input('Name?: ').capitalize()
        
        if owner!='Hermione':
            print('Wrong')
        else:
            contactbook=MagicalContactBook()
            while True:
                print(f'⭐Welcome {owner}!⭐')
                print("1. Add Wizard/Witch🧙")
                print("2. Add Creature👽")
                print("3. List Contacts")
                print("4. Find Contacts")
                print("5. Quit")
                choice=int(input(f'enter a number from(1-6),{owner}: '))
                if choice== 1:
                    name=input('Name: ')
                    email=input('Email: ')
                    phone_no=int(input('Number: +'))
                    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
                    house = input("Enter House(Gryffindor, Slytherin, Ravenclaw, or Hufflepuff): ").capitalize()
                    if house not in houses:
                        raise ValueError("Invalid house provided.")
                    else:
                        contact=WizardOrWitch(name, email, phone_no, house)
                        contactbook.add_contact(contact)
                        print(f'the contact {name} with the number {phone_no} and the email {email} and the house {house} has been added!')
              
                elif choice == 2:
                    name = input("Name: ")
                    email = input("Email: ")
                    phone_no = input("Number: +")
                    species = input("Species: ")
                    tame = input("Is the creature tame (yes/no)? ").strip().lower()
                    if tame == 'yes':
                        tame_state = 'yes'
                    elif tame == 'no':
                        tame_state = 'no'
                    else:
                        print('Invalid Choice, the answer has to be (yes/no)')
                        continue
                    contact = MagicalCreature(name, email, phone_no, species, tame_state)
                    contactbook.add_contact(contact)

                    print(f'the contact {name} with the number {phone_no} and the species {species} and it is {tame_state} has been added!')
                elif choice== 3:
                    contactbook.list_contacts()
                elif choice == 4:
                    name = input('Name: ')
                    contact = contactbook.find_contact(name)
                    if contact:
                        print(f'The contact with the name {name} has been found 😊')
                        print(contact.describe())
                    else:
                        print(f'The contact with the name {name} has not been found 😟')

                elif choice== 5:
                    print('Bye😈')
                    break
                else:
                    print('INVALID CHOICE👿')


                

              
                    
         

            


        
        




 



        
        
        
    
    
        
    
    
             

        
