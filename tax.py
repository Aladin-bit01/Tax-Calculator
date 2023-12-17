import customtkinter as ctk

class TaxCalculator:
    def __init__(self):
        #Initialize our Window
        self.window= ctk.CTk()
        self.window.title('Tax Calculator')
        self.window.geometry('280x200')
        self.window.resizable(False, False)
        #paddin in a dict cuase we need to use same values multiple times
        self.padding = {'padx':20 , 'pady':10}
        #Income_Label
        self.income_label = ctk.CTkLabel(self.window, text='Income:')
        self.income_label_grid = self.income_label.grid(row=0, column=0, **self.padding)
        #Income Entry
        self.income_box= ctk.CTkEntry(self.window)
        self.income_box_entry= self.income_box.grid(row=0, column=1, **self.padding)


        #Tax Rate Label
        self.tax_rate= ctk.CTkLabel(self.window, text='Percent: ')
        self.tax_rate_grid= self.tax_rate.grid(row=1, column=0, **self.padding)
        # Tax Rate Entry
        self.tax_rate_entry= ctk.CTkEntry(self.window)
        self.tax_rate_entry_grid= self.tax_rate_entry.grid(row=1, column=1, **self.padding)

        #Result Label
        self.result= ctk.CTkLabel(self.window, text= 'Tax:')
        self.result_grid= self.result.grid(row=2, column=0, **self.padding)

        #Result Entry
        self.result_entry= ctk.CTkEntry(self.window)
        self.result_entry.insert(0, '0')
        self.result_entry_grid= self.result_entry.grid(row=2 , column= 1, **self.padding)

        # Button
        self.button = ctk.CTkButton(self.window, text='Calculate', command=self.calculate_tax)
        self.button_grid = self.button.grid(row=3, column=1, **self.padding)

    #Method that permits to modify the default value by the calculated result
    def update_result(self,text):
        self.result_entry.delete(0,ctk.END)
        self.result_entry.insert(0, text)
    #Method that permits to calculate the tax
    def calculate_tax(self):
        try:
            income= float(self.income_box.get())
            rate= float(self.tax_rate_entry.get())
            self.update_result(f'${(income*rate)/100:,.2f}')
        except ValueError:
            self.update_result('Invalid Input')

#Method the permits to run the window
    def run(self):
        self.window.mainloop()



if __name__ == '__main__':
    app = TaxCalculator()
    app.run()
'''     
def buttono():
    print('Hello')

app = ctk.CTk()
app.title('tax_calculator')
app.geometry('400x250')
app.grid_columnconfigure(0, weight= 1)

button= ctk.CTkButton(app, text= 'Hello', command= buttono )
button.grid(row=0, column=0, padx=20, pady=20 , sticky='ew')

checkbox_1 = ctk.CTkCheckBox(app, text="checkbox 1")
checkbox_1.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="w")
app.mainloop()

'''