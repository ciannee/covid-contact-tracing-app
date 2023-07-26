# Name: Pineda, Patricia Anne E.
# Section: BSCPE 1-5
# OOP Final Project: Covid Contact Tracing App with GUI

# import tkinter
import tkinter
# import ttk
from tkinter import ttk

# create window
window = tkinter.Tk()
window.title("COVID-19 Health Declaration Form")

# create frame
frame = tkinter.Frame(window)
frame.pack()

# user info
user_information_frame = tkinter.LabelFrame(frame, text='Personal Information')
user_information_frame.grid(row=0, column=0, padx=20, pady=10)

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
loss_of_taste_label = tkinter.Label(health_info_frame, text='Loss of Smell')
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

# accept terms

window.mainloop()