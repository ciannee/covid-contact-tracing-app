# Name: Pineda, Patricia Anne E.
# Section: BSCPE 1-5
# OOP Final Project: Covid Contact Tracing App with GUI

# import tkinter
import tkinter
# import ttk
from tkinter import ttk
# import tkinter message box
from tkinter import messagebox
# import os and openpyxl
import os
import openpyxl

# submit form command
def enter_data():
    accepted = accept_var.get()
    # user info
    if accepted == "Certified":
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()

        if first_name and last_name:
            gender = gender_combobox.get()
            age = age_entry.get()
            occupation = occupation_entry.get()

            # contact details
            address = residential_address_entry.get()
            number = mobile_number_entry.get()
            email = email_entry.get()

            # health information
            sore_throat = sore_throat_combobox.get()
            fever = fever_combobox.get()
            cough = cough_combobox.get()
            runny_nose = runny_nose_combobox.get()
            loss_of_smell = loss_of_smell_combobox.get()
            loss_of_taste = loss_of_taste_combobox.get()
            abdominal_pain = abdominal_pain_combobox.get()
            diarrhea = diarrhea_combobox.get()

            print("Submitted.")

            filepath = r'C:\Users\Mari\Desktop\OOP\git\covid-contact-tracing-app\data.xlsx'

            if not os.path.exists(filepath):
                workbook= openpyxl.Workbook()
                sheet = workbook.active
                heading = ["First Name", "Last Name", "Gender", "Age", "Occupation", "Residential Address", "Mobile Number", "Email Address", "Sore Throat", "Fever", "Cough", "Runny Nose", "Loss of Smell", "Loss of Taste", "Abdominal Pain", "Diarrhea"]
                sheet.append(heading)
                workbook.save(filepath)
            
            workbook = openpyxl.load_workbook(filepath)
            sheet = workbook.active
            sheet.append([first_name, last_name, gender, age, occupation, address, number, email, sore_throat, fever, cough, runny_nose, loss_of_smell, loss_of_taste, abdominal_pain, diarrhea])
            workbook.save(filepath)
        
        else:
             tkinter.messagebox.showwarning(title='Error', message ='First name and last name are required.')
    
    else:
        tkinter.messagebox.showwarning(title="Error", message="You have not certify the information.")



# create window
window = tkinter.Tk()
window.title("COVID-19 Health Declaration Form")

# create frame
frame = tkinter.Frame(window)
frame.pack()

# user info
user_information_frame = tkinter.LabelFrame(frame, text='Personal Information')
user_information_frame.grid(row=0, column=0, sticky='news', padx=20, pady=10)

# first name
first_name_label = tkinter.Label(user_information_frame, text='First Name')
first_name_label.grid(row=0, column=0)
first_name_entry = tkinter.Entry(user_information_frame)
first_name_entry.grid(row=1, column=0)

# last name
last_name_label = tkinter.Label(user_information_frame, text='Last Name')
last_name_label.grid(row=0, column=1)
last_name_entry = tkinter.Entry(user_information_frame)
last_name_entry.grid(row=1, column=1)

# gender
gender_label =tkinter.Label(user_information_frame, text='Gender')
gender_combobox = ttk.Combobox(user_information_frame, value=["Male", "Female", "Prefer not to say"])
gender_label.grid(row=0, column=2)
gender_combobox.grid(row=1, column=2)

# age
age_label = tkinter.Label(user_information_frame, text="Age")
age_label.grid(row=2, column=0)
age_entry = tkinter.Entry(user_information_frame)
age_entry.grid(row=3, column=0)

# occupation
occupation_label = tkinter.Label(user_information_frame, text='Occupation')
occupation_label.grid(row=2, column=1)
occupation_entry = tkinter.Entry(user_information_frame)
occupation_entry.grid(row=3, column=1)

# user information widget
for widget in user_information_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# contact details
contact_details_frame = tkinter.LabelFrame(frame, text = 'Contact Details')
contact_details_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

# residential address
residential_address_label = tkinter.Label(contact_details_frame, text='Residential Address')
residential_address_label.grid(row=0, column=0)
residential_address_entry = tkinter.Entry(contact_details_frame)
residential_address_entry.grid(row=1, column=0)

# mobile number
mobile_number_label = tkinter.Label(contact_details_frame, text='Mobile Number')
mobile_number_label.grid(row=0, column=1)
mobile_number_entry = tkinter.Entry(contact_details_frame)
mobile_number_entry.grid(row=1, column=1)

# email
email_label = tkinter.Label(contact_details_frame, text='Email Address')
email_label.grid(row=0, column=2)
email_entry = tkinter.Entry(contact_details_frame)
email_entry.grid(row=1, column=2)

# contact details widget
for widget in contact_details_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)


# health info
health_info_frame = tkinter.LabelFrame(frame, text='Health Information Details')
health_info_frame.grid(row=2, column=0, sticky='news', padx=20, pady=10)

# sore throat
sore_throat_label = tkinter.Label(health_info_frame, text='Sore Throat')
sore_throat_combobox = ttk.Combobox(health_info_frame, value=['Yes', 'No'])
sore_throat_label.grid(row=0, column=0)
sore_throat_combobox.grid(row=2, column=0)

# fever
fever_label = tkinter.Label(health_info_frame, text='Fever')
fever_combobox = ttk.Combobox(health_info_frame, value=['Yes', 'No'])
fever_label.grid(row=0, column=1)
fever_combobox.grid(row=2, column=1)

# cough
cough_label = tkinter.Label(health_info_frame, text='Cough')
cough_combobox = ttk.Combobox(health_info_frame, value=['Yes', 'No'])
cough_label.grid(row=0, column=2)
cough_combobox.grid(row=2, column=2)

# runny nose
runny_nose_label = tkinter.Label(health_info_frame, text='Runny Nose')
runny_nose_combobox = ttk.Combobox(health_info_frame, value=['Yes', 'No'])
runny_nose_label.grid(row=3, column=0)
runny_nose_combobox.grid(row=4, column=0)

# loss of smell
loss_of_smell_label = tkinter.Label(health_info_frame, text='Loss of Smell')
loss_of_smell_combobox = ttk.Combobox(health_info_frame, value=['Yes', 'No'])
loss_of_smell_label.grid(row=3, column=1)
loss_of_smell_combobox.grid(row=4, column=1)

# loss of taste
loss_of_taste_label = tkinter.Label(health_info_frame, text='Loss of Taste')
loss_of_taste_combobox = ttk.Combobox(health_info_frame, value=['Yes', 'No'])
loss_of_taste_label.grid(row=3, column=2)
loss_of_taste_combobox.grid(row=4, column=2)

# abdominal pain
abdominal_pain_label = tkinter.Label(health_info_frame, text='Abdominal Pain')
abdominal_pain_combobox = ttk.Combobox(health_info_frame, value=['Yes', 'No'])
abdominal_pain_label.grid(row=5, column=0)
abdominal_pain_combobox.grid(row=6, column=0)

# diarrhea
diarrhea_label = tkinter.Label(health_info_frame, text='Diarrhea')
diarrhea_combobox = ttk.Combobox(health_info_frame, value=['Yes', 'No'])
diarrhea_label.grid(row=5, column=1)
diarrhea_combobox.grid(row=6, column=1)

# health info frame widget
for widget in health_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# accept terms
declaration_frame = tkinter.LabelFrame(frame, text='Declaration')
declaration_frame.grid(row=7, column=0, sticky='news', padx=20, pady=10)
accept_var = tkinter.StringVar(value='Not Certified')
declaration_check = tkinter.Checkbutton(declaration_frame, text='I hereby certify that the information given above are true, correct, and complete.', variable=accept_var, onvalue="Certified", offvalue="Not Certified")
declaration_check.grid(row=0, column=0)

# submit button
button = tkinter.Button(frame, text='Submit Form', command=enter_data)
button.grid(row=8, column=0, sticky='news', padx=20, pady=10)



window.mainloop()