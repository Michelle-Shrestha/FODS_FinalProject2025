#Necessary Libraries
import matplotlib.pyplot as plt 
import pandas as pd

# --------- Class Definitions ---------

class Student: #Base Class
    def __init__(self, student_id, name): #Constructor
        # Instance Variable
        self.id = student_id 
        self.name = name 
        self.role = "student" 


#-------------------------------- student menu ---------------------------------------

    #menu system for students
    def student_menu(self):

        #loop to keep the menu open
        while True: 
            print("\n---------------------------------------------")
            print(f"Welcome, {self.name} (Student)")
            print("1) View Profile")
            print("2) Update Profile")
            print("3) View Grades")
            print("4) View ECA")
            print("5) Change Password")
            print("6) Logout")
            print("---------------------------------------------")
            choice = input("Enter your choice: ")

            #have dynamic options for students
            #calls the methods of the class based on the choice of the student
            if choice == "1":
                self.view_profile()
            elif choice == "2":
                self.update_profile()
            elif choice == "3":
                self.view_grades()
            elif choice == "4":
                self.view_eca()
            elif choice == "5":
                self.change_password()
            elif choice == "6":
                print("Logging out...")
                break
            else:
                print("Invalid choice. Try again.")


#-------------------------------------------- view profile ---------------------------------------------

    def view_profile(self):
        try:

            with open("users.txt", "r") as file: 
                
                #condition to check whether there is profile or not
                found_profile = False 

                for line in file:
                    #using logical or so split the sentence 
                    #split the line into three parts using delimiter 
                    user_id, name, role = line.strip().split("|") 

                    #compares the user_id from the file with the currently logged_in users ID
                    if user_id == self.id: 
                        print("\n-------- Your Profile --------")
                        print(f"ID     : {user_id}")
                        print(f"Name   : {name}")
                        print(f"Role   : {role}")
                        print("----------------------------")

                         #if it matches,it means we've found their profile
                        found_profile = True  
                        break

            #if profile not found after the loop
            if not found_profile: 
                print("Profile not found.")

        #if file not found, print this message
        except FileNotFoundError:
            print("Error: File not found") 

        # if any other error occurs, print this message 
        except Exception as e:
            print(f"Error reading profile: {e}") 

#----------------------------------------- Update Profile----------------------------------------------------------------
    
    #for changing user name
    def update_profile(self): 
        try:

            #for new name
            updated_name = input("Enter your new name: ").strip()
            if not updated_name: #if nothing is written
                print("Name cannot be empty.")
                return

            #stores all lines from the file
            lines = [] 

            #to track the update status
            updated = False 

            with open("users.txt", "r") as file:

                for line in file:
                    #splits into 3 parts using delimiter
                    user_id, name, role = line.strip().split("|") 

                    #compares user_id from file with logged in id(seld.id)
                    if user_id == self.id: 

                        #adds the updated name into the line list
                        lines.append(f"{user_id}|{updated_name}|{role}\n")

                        #if update successful
                        updated = True

                        #update current session name too
                        self.name = updated_name  

                    else:

                        #if bot the logged user, just add the line as it is
                        lines.append(line) 

            with open("users.txt", "w") as file:

                #writes all the lines in the file
                file.writelines(lines) 

            if updated: 
                print("Name updated successfully!")

            else:
                print("User not found.")
        
        # if error found, print the message
        except FileNotFoundError:
            print ("Error: File not found") 

        except Exception as e:
            print("Error updating profile:", e)

#-------------------------------------------- View Grades -------------------------------------------------            

    def view_grades(self):

        #list of grades
        subjects = ["English", "Computer Fundamentals", "Programming", "Multimedia", "Database"]

        try:
            with open("grades.txt", "r") as file:

                #loops through each line in the file
                for line in file:

                    #strips spaces and newlines(.strip() and separate parts by logical or)
                    parts = line.strip().split("|")

                    #checks first line (user_id) matches logged in users ID
                    if parts[0] == self.id: 
                        
                        #if user_id matches
                        print("\n------ Your Grades ------")

                        #loops through the grades corresponding to the subjects in the list
                        for i in range(1, 6): 

                            #prints the respective grade from the file
                            print(f"{subjects[i-1]}: {parts[i]}") 

                        print("-------------------------")
                        return
                    
            #if users grade not found in the loop
            print("No grades found.") 
        
        #if error found, print the message
        except FileNotFoundError:
            print ("Error: File not found") 

        except Exception as e: 
            print("Error reading grades:", e)

#-------------------------------------------- View ECA ------------------------------------------------------

    def view_eca(self):

        try:

            with open("eca.txt", "r") as file:

                for line in file:

                    #separates user_id and activities
                    user_id, activities = line.strip().split("|") 

                    #Checks user_id in the file with logged in user id
                    if user_id == self.id: 
                        print("\n------ Your ECA ------")
                        #prints the activities of the user
                        print(f"Activities: {activities}") 

                        print("----------------------")
                        return
                    
            #if user's ECA not found in the loop
            print("No ECA activities found.") 

        #if error found, print the message    
        except FileNotFoundError:
            print ("Error: File not found") 
        except Exception as e:
            print("Error reading ECA data:", e)

#------------------------------------------- Change Password --------------------------------------------------

    def change_password(self):

        try:

            with open("passwords.txt", "r") as file:

                #reads all lines in the file
                lines = file.readlines() 

            #to store modified data
            updated_lines = [] 

            #initializes the condition to check if password changed
            password_changed = False 

            #ask input and removes whitspace
            current_password = input("Enter your current password: ").strip() 
            new_password = input("Enter the new password: ").strip()
            confirm_password = input("Confirm the new password: ").strip()

            #if entered passwords do not match
            if new_password != confirm_password: 
                print("New password and confirm password do not match.")
                return

            for line in lines:

                #for each line in the file, splits user_id and password
                user_id, pwd = line.strip().split("|") 

                #if user_id matches logged in user id
                if user_id == self.id: 

                    #if entered current password is not correct
                    if pwd != current_password: 
                        print("Current password is incorrect.")
                        return
                    
                    #updates the password in the file if pwd is correct
                    updated_lines.append(f"{user_id}|{new_password}\n")

                    #sets condition to True if password changed
                    password_changed = True 

                else:

                    #if user_id does not match, adds the line as it is
                    updated_lines.append(line) 

            with open("passwords.txt", "w") as file:

                # writes the updated lines in the file
                file.writelines(updated_lines)

            if password_changed:
                print("Password updated successfully!")

            else:
                #if password not changed
                print("Password update failed.") 

        #if error found, print the message 
        except FileNotFoundError:
            print ("Error: File not found")
        except Exception as e:
            print("Error while changing password:", e)

#------------------------------------------------- Admin -------------------------------------------------------

#Admin class inherits from Student class
class Admin(Student): 

    #initializes admin_id and name
    def __init__(self, admin_id, name): 
        # calls the constructor of the parent class
        super().__init__(admin_id, name)  

        # sets the role of the admin as admin (in Student- student in Admin - admin)
        self.role = "admin" 

#--------------------------------------------- Admin Menu -------------------------------------------------------
   
   #menu system for Admins
    def admin_menu(self): 

        # print("Admin Menu")
        #loop to keep the menu running    
        while True: 

            print("\n================================================")
            print(f"Welcome, {self.name} (Admin)")
            print("1) Add Student")
            print("2) Delete Student")
            print("3) Edit Student Profile")
            print("4) Edit Student Grades")
            print("5) Edit Student ECA")
            print("6) Update Admin Username/Password")
            print("7) View Student Activities Analysis")
            print("8) Logout")
            print("================================================")
            choice = input("Enter your choice: ")


            #dynamic options for Admin
            #calls the methods of the class based on the choice of the admin
            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.delete_student()
            elif choice == "3":
                self.update_student_profile()
            elif choice == "4":
                self.update_student_grades()
            elif choice == "5":
                self.update_student_eca()
            elif choice == "6":
                self.update_admin_credentials()
            elif choice == "7":
                self.show_analytics()
            elif choice == "8":
                print("Logging out...")
                #breaks the loop and ends the menu
                break

            # if choice is not in the options
            else:
                print("Invalid choice. Try again.") 

#-------------------------------------------- Add Students -------------------------------------------------------

    def add_student(self):

        try:

            #get the new student details from user
            new_id = input("Enter new student ID: ").strip() 
            new_name = input("Enter student name: ").strip()
            new_password = input("Enter student password: ").strip()

            #Check if student already exists
            with open("users.txt", "r") as file:
                for line in file:

                    # "_" are the placeholders of the variable which are not much in use
                    # user_id, name, password
                    user_id, _, _ = line.strip().split("|") 

                    #if user id is alread in the file and is same as new id
                    if user_id == new_id: 
                        print("Error: Student ID already exists.")
                        return

            # open file in append mode to add new student in the file
            with open("users.txt", "a") as file: 

                #write new student details to file (users.txt)
                file.write(f"{new_id}|{new_name}|student\n") 

            #Add to passwords.txt
            with open("passwords.txt", "a") as file:

                # write new student password to file (passwords.txt)
                file.write(f"{new_id}|{new_password}\n") 

            # Add to grades.txt with empty default grades
            with open("grades.txt", "a") as file:

                #write new student grades to file (grades.txt), it set the new student grades to 0
                file.write(f"{new_id}|0|0|0|0|0\n") 

            # Add to eca.txt with empty entry
            with open("eca.txt", "a") as file:

                #write new student eca entry to file (eca.txt)
                file.write(f"{new_id}|\n") 

            print("Student added successfully!")


        #if error found, print the message 
        except FileNotFoundError:
            print("Error: File not found.")
        except Exception as e: 
            print("Error adding student:", e)

#------------------------------------------ Delete Student ---------------------------------------------------------

    def delete_student(self):

        #get student id from user which is to be deleted
        target_id = input("Enter student ID to delete: ").strip() 

        #condition to check if student is found
        found = False

    #---------------------- Filter out the student from all files -----------------------------------------------
        
        # helper function to filter out student id from file
        #Handles the delete process of studen id from the files (at a time)
        def filter_out(filename): 

            #nonlocal keyword is used to access outer function variable
            #it allows the function to modify the outer function variable (but not the global variable)
            nonlocal found 

            try:


                with open(filename, "r") as f: 
                    # read all lines from file
                    lines = f.readlines() 

                #overwrites its content
                with open(filename, "w") as f: 

                    for line in lines:

                        #if line does not start with target id
                        if not line.startswith(target_id + "|"): 

                            #write line back to the file
                            f.write(line) 

                        else:

                            #if line starts with target ID it skips writing the line and deletes that line
                            found = True 
            except:

                # if file not accessable 
                print(f"Could not access {filename}") 

        #searches the targetted student id in all the files
        for file in ["users.txt", "passwords.txt", "grades.txt", "eca.txt"]: 

            #filter out (deletes) student id from each file
            filter_out(file) 

        #conditional expression to print student deleted or student id not found
        print("Student deleted." if found else "Student ID not found.") 


#------------------------------------------ Update Student Profile ------------------------------------------------

    #allows updating the student names based on Student ID
    def update_student_profile(self):

        #get student id and new name from user which is to be updated
        target_id = input("Enter student ID to update: ").strip() 
        new_name = input("Enter new name: ").strip() 

        #condition to check if student is updated
        updated = False 

        try:
            with open("users.txt", "r") as file: 

                #read all lines from file and stores in list variable lines
                lines = file.readlines() 

            #reopens the .txt & overwrites its content
            with open("users.txt", "w") as file: 
                for line in lines:

                    #removes whitespace and splits the line into three variables using delimiter
                    user_id, name, role = line.strip().split("|") 

                    #if user id matches with target id and role is student
                    if user_id == target_id and role == "student":

                        #updates the name in the file replacing old name 
                        file.write(f"{user_id}|{new_name}|{role}\n") 

                        #sets true if updated successfully
                        updated = True 

                    else:

                        #writes the original line back to the file
                        file.write(line) 

            #uses conditional expression to check if updated or not
            print("Name updated." if updated else "Student not found.") 

        #if error found, print the message 
        except FileNotFoundError:
            print("Error File not found.") 
        except Exception as e:
            print("Error updating profile:", e)

#---------------------------------------- Update Student Grades -----------------------------------------------------     

    #allows updating the student grades based on Student ID
    def update_student_grades(self):

        #get student id and new grade from user which is to be updated
        target_id = input("Enter student ID: ").strip() 

        #subjecta for which grade is to be updated
        subjects = ["English", "Computer Fundamentals", "Programming", "Multimedia", "Database"] 

        #list to store the subjects and their corresponding grades
        new_grades = [] 

        #iterates over each subject 
        for subject in subjects: 
            while True:
                try:

                    #prompts user to enter marks for each subject
                    mark = int(input(f"Enter marks for {subject}: ")) 

                    #checks if marks are valid (between 0 and 100)
                    if 0 <= mark <= 100: 
                        # appends the marks to the list
                        new_grades.append(mark) 

                        #breaks the loop if all subjects' marks are entered
                        break 

                    else:
                        print("Enter a value between 0 and 100.")
                
                except:
                    print("Invalid input.")

        #condition to check if student is updated
        updated = False 
        try:

            #to access its contents
            with open("grades.txt", "r") as file: 

                #read all lines from file and stores in list variable lines
                lines = file.readlines() 

            #reopens the .txt & overwrites its content
            with open("grades.txt", "w") as file: 

                #iterates over each line in the list
                for line in lines:

                    # if line starts with target id followed by delimiter
                    if line.startswith(target_id + "|"): 

                        #converts into strring and joins the using delimiter
                        file.write(f"{target_id}|" + "|".join(map(str, new_grades)) + "\n")

                        #sets true if updated successfully 
                        updated = True 

                    else:

                        #writes the original line back to the file
                        file.write(line) 

            #uses conditional expression to check if updated or not
            print("Grades updated." if updated else "Student not found.") 

        #if error found, print the message 
        except FileNotFoundError:
            print("Error File not found.") 

        #catches any exceptions that may occur
        except Exception as e: 
            print("Error updating grades:", e)

 #----------------------------------------------------- Update Student ECA --------------------------------------------------           

    def update_student_eca(self):

        #get student id and new eca activities from user and removes whitespace which is to be updated
        target_id = input("Enter student ID: ").strip() 
        new_activities = input("Enter updated ECA activities (comma separated): ").strip() 

        #condition to check if student is updated
        updated = False 

        try:

            #to access its contents
            with open("eca.txt", "r") as file: 

                #read all lines from file and stores in list variable lines
                lines = file.readlines() 

            #reopens the .txt and overwrites its content
            with open("eca.txt", "w") as file: 

                for line in lines:

                    #if line starts with target id followed by delimiter
                    if line.startswith(target_id + "|"): 

                        #writes the updated eca activities in the targeted id
                        file.write(f"{target_id}|{new_activities}\n") 

                        #sets true if updated successfully
                        updated = True 

                    else:

                        #writes the original line back to the file
                        file.write(line) 

            #uses conditional expression to check if updated or not
            print("ECA updated." if updated else "Student not found.") 

        #if error found, print the message 
        except FileNotFoundError:
            print("Error File not found.")
        except Exception as e:
            print("Error updating ECA:", e)

#------------------------------------------------------ User Admin Credentials --------------------------------------------------------------------            

    #method to update admin credentials
    def update_admin_credentials(self):

        # get new admin credentials from user
        new_id = input("Enter new admin ID: ").strip() 
        new_name = input("Enter new admin name: ").strip()
        new_password = input("Enter new password: ").strip()
        
        #get current admin id
        #stores existing ID in the variable old_id  before changing it
        old_id = self.id  

        
        # Update users.txt
        try:

            #to access its contents
            with open("users.txt", "r") as file: 

                #read all lines from file and stores in list variable lines
                lines = file.readlines() 

            #reopens the .txt and overwrites its content
            with open("users.txt", "w") as file: 
              
              for line in lines:

                #splits the line into parts using delimiter
                parts = line.strip().split("|") 

                #if line does not contain 3 parts (id,name,role)
                if len(parts) != 3: 

                    #Write it back unchanged
                    file.write(line)  

                    #Skip to the next line
                    continue  
                
                #to ensure that the only the records of admin is updated
                #extracts from the current records (parts): user id, name, and role
                user_id, name, role = parts  

                #if current admin id matches with old id and role is admin
                if user_id == old_id and role == "admin": 

                    #updates the admin credentials
                    file.write(f"{new_id}|{new_name}|admin\n")  

                    #updates attributes of the admin object with new values
                    self.id = new_id  
                    self.name = new_name 

                else:
                  
                  #Write it back unchanged if record doesnot match
                  file.write(line) 
        
        #if error found, print the message 
        except FileNotFoundError:
            print("Error File not found.") 
        except Exception as e:
          print("Error updating user file:", e)

        #Update passwords.txt
        try:

            with open("passwords.txt", "r") as file:

                #read all lines from file and stores in list variable lines
                lines = file.readlines() 

            #reopens the .txt and overwrites its content
            with open("passwords.txt", "w") as file: 
                for line in lines:
                  
                  #splits the line into parts using delimiter
                  user_id, pwd = line.strip().split("|") 

                #Write it back unchanged if record doesnot match
                  if user_id != old_id: 
                      file.write(line)  

                #if current admin id matches with old id
                  else:
                      
                      #updates the admin password
                      file.write(f"{new_id}|{new_password}\n")  
                    
            #prints success message
            print("Admin credentials updated.") 
        
        #if error found, print the message 
        except FileNotFoundError:
            print("Error File not found.") 
        except Exception as e:
            print("Error updating password file:", e)

#---------------------------------------------- Show Students Activity Analytics ------------------------------------------       
    
    def show_analytics(self):
        try:

            #reads grades.txt file into a pandas dataframe
            df_grades = pd.read_csv("grades.txt", sep="|", header=None) 

            #assigns column names to the dataframe
            df_grades.columns = ["ID", "English", "CompFund", "Programming", "Multimedia", "Database"] 

            #sets ID as index of the dataframe
            df_grades.set_index("ID", inplace=True) 
            
            #reads eca file into a pandas dataframe
            df_eca = pd.read_csv("eca.txt", sep="|", header=None, names=["ID", "Activities"]) 
            df_eca.set_index("ID", inplace=True) 

            # 1. Grade Trend (Average per subject)
            #calculates average of each subject
            subject_avg = df_grades.mean() 

            #plots a bar chart of average grades per subject
            subject_avg.plot(kind='bar', title="Average Grades per Subject", ylabel="Marks", xlabel="Subjects") 
            plt.tight_layout() #ensures labels fit within the figure area
            plt.show() #displays the plot

            # 2. ECA Impact
            #calculates average of each student
            df_grades["Average"] = df_grades.mean(axis=1) 

            #fillna() method replaces the missing value in df or series
            #counts the number of activities each student has done 
            #x is the string of activities
            df_eca["ECA_Count"] = df_eca["Activities"].fillna("").apply(lambda x: len(x.split(",")) if x else 0) 

            #combines the two dataframes on ID and fills missing values with 0
            df_combined = df_grades.join(df_eca, how='left').fillna(0) 

            #plots a scatter plot of ECA count vs average grade
            plt.scatter(df_combined["ECA_Count"], df_combined["Average"], color='green') 

            plt.title("ECA Participation vs Academic Performance") #sets title of the plot
            plt.xlabel("Number of ECAs") # ets x-axis label
            plt.ylabel("Average Grade") #sets y-axis label
            plt.grid(True) #displays grid lines
            plt.tight_layout() #ensures labels fit within the figure area
            plt.show()

            # 3. Performance Alerts (Below threshold)
            #sets the threshold for performance alert
            threshold = 40 

            #identifies students with average grade below threshold
            alerts = df_combined[df_combined["Average"] < threshold] 

            #if there are students with average grade below threshold
            if not alerts.empty: 
                print("\n Students Below Performance Threshold (Avg < 40):") 

                #prints student IDs with average grade below threshold
                for student_id in alerts.index: 

                    #.loc is a powerful method to access rows and columns by labels or a boolean array
                    #prints student ID and average grade
                    print(f"- {student_id}: Avg = {alerts.loc[student_id, 'Average']:.2f}") 

            else:
                #prints message if all students are above threshold
                print("\n All students are above the performance threshold.") 

        #if error found, print the message 
        except FileNotFoundError: 
            print("Missing 'grades.txt' or 'eca.txt'. Please ensure files exist.") 
        except Exception as e:
            print("Analytics Error:", e)



# ------------------------------------------------ Utility Functions --------------------------------------------------
# extra function
#checks file exists or not in these two function
                                  #----------------load users --------------------------
def load_users(): 

    #dictionary to store users
    users = {} 
    try:

        #opens the file in read mode
        with open("users.txt", "r") as file: 
            for line in file:

                #splits the line into parts using delimiter
                user_id, name, role = line.strip().split("|") 

                #stores user id (key) and its details (value) in dictionary
                users[user_id] = {"name": name, "role": role} 
   
    except FileNotFoundError:
        print("Error: 'users.txt' not found.")

    #returns the dictionary of users
    return users 

                                    #-------------- load passwords ------------------------

def load_passwords():

    #dictionary to store passwords
    passwords = {} 

    try:

        with open("passwords.txt", "r") as file:
            for line in file:

                #splits the line into parts using delimiter
                user_id, password = line.strip().split("|") 

                #stores user id (key) and its password (value) in dictionary
                passwords[user_id] = password 

    #if error found, print the message 
    except FileNotFoundError:
        print("Error: 'passwords.txt' not found.")
    return passwords #returns the dictionary of passwords

# -------------------------------------------------------- Logi Screen  ------------------------------------------

#Login and Menu Interface
def login_screen(): # function to display login screen

    # declares global variables to access
    global users 
    global passwords

    #calls function from their respective files
    #dict containing info
    users = load_users() 
    passwords = load_passwords()

    #Display login screen
    print("\n=====================================================")
    print("\tWelcome to Student Profile Management System")
    print("=====================================================\n")
    print("1) Student Login")
    print("2) Admin Login")
    print("3) Exit")
    choice = input("\nPlease select an option (1-3): ")

    #if user selects student login
    if choice == "1": 
        role = "student"
    elif choice == "2":
        role = "admin"
    elif choice == "3":
        print("Exiting the program. Goodbye!")
        exit()
    else:
        print("Invalid choice. Returning to main menu.\n")
        return

    #prompts user to enter the id and password
    user_id = input("\nEnter your ID: ").strip() 
    password = input("Enter your password: ").strip()

    #Checks the role + ID match
    if user_id in users and users[user_id]["role"] == role:

        #Check password match
        #checks if user id and password match
        if user_id in passwords and passwords[user_id] == password: 

            #if matches prints welcome message
            print(f"\nLogin successful! Welcome {users[user_id]['name']}\n") 

            #if user is student
            if role == "student": 

                #creates student object
                student = Student(user_id, users[user_id]["name"])
                #calls student menu function
                student.student_menu() 

            else:
                 # if user is admin
                 #creates admin object
                admin = Admin(user_id, users[user_id]["name"]) 
                #calls admin menu function
                admin.admin_menu() 

        else:
            #if password is incorrect prints message
            print("Incorrect password. Please try again.\n")

    else:
        #if user id or role is incorrect prints message
        print("ID not found or role mismatch.\n") 


# ------------------------------------------ Main Program Loop -------------------------------------------------

#main function
def main(): 
    while True: 

        #call login_screen function to get into the program
        login_screen() 


# ------------------------------------------ REntry Point of the Program ----------------------------------------------------

#This is the entry point of the program
# it is the special biuld-in variable
if __name__ == "__main__": 
     #call main function to start the program
    main()