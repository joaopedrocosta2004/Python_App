import tkinter as tk
import pandas as pd
import sqlite3
import subprocess

window = tk.Tk()
window.title("App")
window.geometry("450x500")

def show_users():

    text_box.delete("1.0", tk.END)
    # Connect to the SQLite database
    con = sqlite3.connect('../users.db')
    cur = con.cursor()

    cur = cur.execute("Select first_name, second_name, email from users")
    users_registered = cur.fetchall()

    if (len(users_registered) == 0):
        text_box.insert(tk.END, "No User is registered!!")

    # Close the connection
    con.close()

    # Display all users in the text box
    text_box.insert(tk.END, "Registered Users:\n\n")
    for user in users_registered:
        text_box.insert(tk.END, f"Nome: {user[0]} {user[1]} | Email: {user[2]}\n\n")
    return

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
    show_users()

def user_removal():
    subprocess.run(['python', 'Deletion.py']) 

def user_registration():
    subprocess.run(['python', 'Registration.py'])

text_box = tk.Text(window, width=50, height=15)
text_box.grid(row=0, column=0, pady=10)

users_button = tk.Button(text="Shows Users", command=show_users)
users_button.grid(row=1, column=0, padx=10, pady=10, ipadx=90)

export_button = tk.Button(text="Export to Excel", command=user_export)
export_button.grid(row=2, column=0, padx=10, pady=10, ipadx=90)

registration_button = tk.Button(text="Register", command=user_registration)
registration_button.grid(row=3, column=0, padx=10, pady=10, ipadx=90)

removal_button = tk.Button(text="Remove User", command=user_removal)
removal_button.grid(row=4, column=0, padx=10, pady=10, ipadx=90)


window.mainloop()