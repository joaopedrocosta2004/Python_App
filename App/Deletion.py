import tkinter as tk
import sqlite3

window = tk.Tk()
window.title("User Removal")
window.geometry("250x260")

def user_removal():
    # Get the entered email from the entry box
    user_email = email_entry.get()

    removal(user_email)

    # Clear the users fields
    email_entry.delete(0, "end")

def removal(user_email):
    
    text_box.delete("1.0", tk.END)

    # Connect to the SQLite database
    con = sqlite3.connect('../users.db')
    cur = con.cursor()

    cur = cur.execute("Select email from users")

    # Fetch all emails from the database
    all_emails_tuple = cur.fetchall()
    if (len(all_emails_tuple) == 0):
        text_box.insert(tk.END, "No User is registered!!")

    all_emails = [email[0] for email in all_emails_tuple]


    found = False  # Flag to check if the email was found

    for email in all_emails:
        if user_email == email:
            cur.execute("DELETE FROM users WHERE email=?", (email,))
            if cur.rowcount == 1:
                text_box.insert(tk.END, f"{email} foi removido.")
                found = True  # Set the flag to True if email is found and deleted
                break  # Exit the loop since we've found and deleted the email

    # After the loop, check if the email was not found
    if not found:
        text_box.insert(tk.END, f"Email {user_email} não encontrado.")

    
    # Commit the changes and close the connection
    con.commit()
    con.close()

# Create labels and entry boxes for user input
label_email = tk.Label(window, text="Email:")
label_email.grid(row=2, column=0, padx=10, pady=10)

email_entry = tk.Entry(window, width=25)
email_entry.grid(row=3, column=0, padx=10, pady=10)

text_box = tk.Text(window, width=25, height=5)
text_box.grid(row=0, column=0, pady=10)

removal_button = tk.Button(text="Remove", command=user_removal)
removal_button.grid(row=4, column=0, padx=10, pady=10, ipadx=80)

window.mainloop()