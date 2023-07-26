# Name: Pineda, Patricia Anne E.
# Section: BSCPE 1-5
# OOP Final Project: Covid Contact Tracing App with GUI

# import tkinter
import tkinter

# create window
window = tkinter.Tk()
window.title("COVID-19 Health Declaration Form")

# create frame
frame = tkinter.Frame(window)
frame.pack

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
# occupation
# contact details
# address
# number
# email
# health info
# sore throat
# fever
# cough
# runny nose
# loss of smell
# loss of taste
# abdominal pain
# diarrhea
# accept terms

window.mainloop