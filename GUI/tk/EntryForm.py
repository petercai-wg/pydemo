
import tkinter
from tkinter import messagebox
from tkinter import ttk


class EntryForm(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.create_widget()

    def create_widget(self):

        self.title("Data Entry Form")

        frame = ttk.Frame(self)
        frame.pack()

        user_info_frame = ttk.LabelFrame(frame, text="User Information")
        user_info_frame.grid(row=0, column=0, padx=20, pady=10, columnspan=3)

        first_name_label = ttk.Label(user_info_frame, text="First Name")
        first_name_label.grid(row=0, column=0)
        last_name_label = ttk.Label(user_info_frame, text="Last Name")
        last_name_label.grid(row=0, column=1)

        self.first_name_entry = ttk.Entry(user_info_frame)
        self.last_name_entry = ttk.Entry(user_info_frame)

        self.first_name_entry.grid(row=1, column=0)
        self.last_name_entry.grid(row=1, column=1)

        title_label = ttk.Label(user_info_frame, text="Title")
        self.title_combobox = ttk.Combobox(
            user_info_frame, values=["Mr.", "Mrs.", "Ms.", "Dr."])
        self.title_combobox.set("select a title")
        self.title_combobox["state"] = 'readonly'

        self.title_combobox.bind("<<ComboboxSelected>>",lambda event: print(f"Combo selected  {self.title_combobox.get()}") )
        title_label.grid(row=0, column=2)
        self.title_combobox.grid(row=1, column=2)

        # Accept terms
        terms_frame = ttk.LabelFrame(frame, text="Terms & Conditions")
        terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10, columnspan=3)

        self.accept_var = tkinter.StringVar()
        terms_check = ttk.Checkbutton(terms_frame, text="I accept the terms and conditions.",
                                      variable=self.accept_var, onvalue="Accepted", offvalue="Not Accepted")
        terms_check.grid(row=0, column=0)

        self.contact_var = tkinter.StringVar()
        contact_check = ttk.Checkbutton(terms_frame, text="I agree you can contact me",
                                      variable=self.contact_var, onvalue="Yes", offvalue="No")
        contact_check.grid(row=1, column=0)

        users = [ 'Anne', 'Bea', 'Chris', 'Bob', 'Helen' ]   

        check_frame = ttk.LabelFrame(frame, text="Mutltiple checkbox")
        check_frame.grid(row=3, column=0 )
        self.checkbox_values = []
        for _ in range(len(users)):
            self.checkbox_values.append(tkinter.StringVar(value= "No"))     
        
        for index in range(len(users)):   
            checkbox = ttk.Checkbutton(check_frame, text=users[index], variable= self.checkbox_values[index],onvalue=str(users[index]), offvalue="No",)
                                    # command=lambda x = index: print(f"checked {x} " ))
            checkbox.pack()
        ## radio choice
        radio_frame = ttk.LabelFrame(frame, text="Radio selection")
        radio_frame.grid(row=3, column=1 )
        
        self.radio_value = tkinter.StringVar()
        self.radio_value2 = tkinter.StringVar()
        
        for index in range(0, 3):   
            radio = ttk.Radiobutton(radio_frame, text=users[index], variable= self.radio_value, value=users[index])
            radio.pack()

        for index in range(3, 5):   
            radio = ttk.Radiobutton(radio_frame, text=users[index], variable= self.radio_value2, value=users[index])
            radio.pack()

        ## ListBox
        list_frame = ttk.LabelFrame(frame, text="List selection")
        list_frame.grid(row=3, column=2 )
        # self.listbox_values = []
        list_value = tkinter.StringVar(value = users)
        self.listbox = tkinter.Listbox(list_frame, listvariable=list_value, height= 3, selectmode= "extended")
        self.listbox.bind("<<ListboxSelect>>", lambda event: print(self.listbox.curselection()))
        self.listbox.pack()

        # Button
        button = ttk.Button(frame, text="Enter data",
                            command=self.enter_data)
        button.grid(row=7, column=0, sticky="news", padx=20, pady=10, columnspan=3)

    def enter_data(self):
        accepted = self.accept_var.get()

        if accepted == "Accepted":
            # User info
            firstname = self.first_name_entry.get()
            lastname = self.last_name_entry.get()
            title = self.title_combobox.get()

            print(f"{title}  First name: {firstname}, Last name: {lastname}")
            selected_items = []
            for value in self.checkbox_values:
                if value.get() != "No":
                    selected_items.append(value.get())
            print(f"Selected items: {selected_items}")

            print(f"Selected choices: {self.radio_value.get()}")
            print(f"Selected list: {self.listbox.curselection()}")
            print("------------------------------------------")
        else:
            messagebox.showwarning(
                title="Error", message="You have not accepted the terms")


if __name__ == "__main__":
    window = EntryForm()
    window.mainloop()
