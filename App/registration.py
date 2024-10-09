import tkinter as tk
import sqlite3
import pandas as pd
import subprocess

window = tk.Tk()
window.title("User Registration")
window.geometry("500x400")

def user_registration():
    con = sqlite3.connect('../users.db')
    cur = con.cursor()

    # Insert user data into the database
    cur.execute("INSERT INTO users VALUES (:first_name, :second_name, :email, :phone)", {
        'first_name': first_name_entry.get(),
        'second_name': second_name_entry.get(),
        'email': email_entry.get(),
        'phone': phone_entry.get()
    })

    # Commit the changes and close the connection
    con.commit()
    con.close()
    
    # Clear the user input fields
    first_name_entry.delete(0, "end")
    second_name_entry.delete(0, "end")
    email_entry.delete(0, "end")
    phone_entry.delete(0, "end")

def user_export():
    con = sqlite3.connect('../users.db')

    cur = con.cursor()

    # Fetch all user data from the database
    cur.execute("SELECT *, oid FROM users")
    users_registered = cur.fetchall()

    # Create a DataFrame from the fetched data
    users_registered_df = pd.DataFrame(users_registered, columns=['First Name', 'Second Name', 'Email', 'Phone', 'id'])
    users_registered_df.to_excel('../users_registered.xlsx', index=False)

    # Close the connection
    con.close()

def user_removal():
    subprocess.run(['python', 'Deletion.py'])   

# Create labels and entry boxes for user input
label_first_name = tk.Label(window, text="First Name:")
label_first_name.grid(row=0, column=0, padx=10, pady=10)

label_second_name = tk.Label(window, text="Second Name:")
label_second_name.grid(row=1, column=0, padx=10, pady=10)

label_email = tk.Label(window, text="Email:")
label_email.grid(row=2, column=0, padx=10, pady=10)

label_phone = tk.Label(window, text="Phone:")
label_phone.grid(row=3, column=0, padx=10, pady=10)

first_name_entry = tk.Entry(window, width=25)
first_name_entry.grid(row=0, column=1, padx=10, pady=10)

second_name_entry = tk.Entry(window, width=25)
second_name_entry.grid(row=1, column=1, padx=10, pady=10)

email_entry = tk.Entry(window, width=25)
email_entry.grid(row=2, column=1, padx=10, pady=10)

phone_entry = tk.Entry(window, width=25)
phone_entry.grid(row=3, column=1, padx=10, pady=10)

# Registration and export buttons
registration_button = tk.Button(text="Register", command=user_registration)
registration_button.grid(row=4, column=0, padx=10, pady=10, ipadx=80)

export_button = tk.Button(text="Export to Excel", command=user_export)
export_button.grid(row=5, column=0, padx=10, pady=10, ipadx=80)

removal_button = tk.Button(text="Remove User", command=user_removal)
removal_button.grid(row=6, column=0, padx=10, pady=10, ipadx=80)

window.mainloop()
