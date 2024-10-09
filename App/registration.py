import tkinter as tk
import sqlite3

window = tk.Tk()
window.title("User Registration")
window.geometry("250x500")

def user_registration():
    
    user_email = email_entry.get().strip()
    
    if verify_email(user_email):
        text_box.insert(tk.END, f"Email {user_email} já registrado!\n")
        return
    
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

def verify_email(user_email):

    con = sqlite3.connect('../users.db')
    cur = con.cursor()

    # Verify email exists
    cur.execute("SELECT email FROM users WHERE email=?", (user_email,))
    existing_email = cur.fetchone()

    con.close()  # Fechar a conexão

    return existing_email is not None  
            


# Create labels and entry boxes for user input
text_box = tk.Text(window, width=25, height=5)
text_box.grid(row=0, column=0, pady=10)

label_first_name = tk.Label(window, text="First Name:")
label_first_name.grid(row=1, column=0, padx=10, pady=10)

label_second_name = tk.Label(window, text="Second Name:")
label_second_name.grid(row=3, column=0, padx=10, pady=10)

label_email = tk.Label(window, text="Email:")
label_email.grid(row=5, column=0, padx=10, pady=10)

label_phone = tk.Label(window, text="Phone:")
label_phone.grid(row=7, column=0, padx=10, pady=10)

first_name_entry = tk.Entry(window, width=25)
first_name_entry.grid(row=2, column=0, padx=10, pady=10)

second_name_entry = tk.Entry(window, width=25)
second_name_entry.grid(row=4, column=0, padx=10, pady=10)

email_entry = tk.Entry(window, width=25)
email_entry.grid(row=6, column=0, padx=10, pady=10)

phone_entry = tk.Entry(window, width=25)
phone_entry.grid(row=8, column=0, padx=10, pady=10)

# Registration and export buttons
registration_button = tk.Button(text="Register", command=user_registration)
registration_button.grid(row=9, column=0, padx=10, pady=10, ipadx=80)

window.mainloop()
