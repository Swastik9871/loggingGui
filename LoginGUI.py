import customtkinter 

customtkinter.set_appearance_mode("dark")  # appearance is dark
customtkinter.set_default_color_theme("green")  # theme of app

root = customtkinter.CTk()
root.geometry("500x350")#size

def login(): # Some Random function
    print("Swastik")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Login System")
label.pack(pady=12, padx=10)#Label for GUI

entry_username = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
entry_username.pack(pady=12, padx=10)#Username input

entry_password = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
entry_password.pack(pady=12, padx=10)#Password input

button = customtkinter.CTkButton(master=frame, text="Login", command=login)
button.pack(pady=12, padx=10)#Loging button

checkBox = customtkinter.CTkCheckBox(master=frame, text="Remeber Me")
checkBox.pack(pady=12, padx=10)#Check box for Remeber me

root.mainloop()