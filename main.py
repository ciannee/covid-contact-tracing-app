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

# last name
# gender
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