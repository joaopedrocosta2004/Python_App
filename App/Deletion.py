import tkinter as tk
import sqlite3

window = tk.Tk()
window.title("User Removal")
window.geometry("500x300")

def user_removal():
    # Get the entered email from the entry box
    user_email = email_entry.get()

    removal(user_email)

    # Clear the users fields
    email_entry.delete(0, "end")

def removal(user_email):
    
    # Connect to the SQLite database
    con = sqlite3.connect('../users.db')
    cur = con.cursor()

    cur = cur.execute("Select email from users")

    # Fetch all emails from the database
    all_emails_tuple = cur.fetchall()

    all_emails = [email[0] for email in all_emails_tuple]


    for index,email in enumerate(all_emails):
        if user_email == email:
            cur.execute("DELETE FROM users WHERE email=?", (email,))
            if cur.rowcount == 1:
                print(f"{email} foi removido.")
        if index == (len(all_emails) - 1) and user_email != email:
            print(f"Email {user_email} não encontrado.")
            con.close()
            return

    
    # Commit the changes and close the connection
    con.commit()
    con.close()

# Create labels and entry boxes for user input
label_email = tk.Label(window, text="Email:")
label_email.grid(row=0, column=0, padx=10, pady=10)

email_entry = tk.Entry(window, width=25)
email_entry.grid(row=0, column=1, padx=10, pady=10)

removal_button = tk.Button(text="Removal", command=user_removal)
removal_button.grid(row=1, column=0, padx=10, pady=10, ipadx=80)

window.mainloop()