import customtkinter as ctk

class QuebecTax:
    def __init__(self):
        #Initialisation de l'écran d'affichage
        self.window= ctk.CTk()
        self.window.title('Quebec Tax Calculator')
        self.window.geometry('400x600')
        self.window.resizable(False,False)

        #Padding
        padding= {'padx':20, 'pady': 10}

        #Revenu total
        self.revenu_label = ctk.CTkLabel(self.window, text= 'Revenu Total:')
        self.revenu_label_grid= self.revenu_label.grid(row=0, column=0, **padding)
        self.revenu_entry= ctk.CTkEntry(self.window)
        self.revenu_entry_grid= self.revenu_entry.grid(row=0, column=1, **padding)
        #Revenu imposable
        self.revenu_imposable= ctk.CTkLabel(self.window, text= 'Revenu Imposable:')
        self.revenu_imposable_grid= self.revenu_imposable.grid(row=1, column=0, **padding)
        self.revenu_imposable_entry= ctk.CTkEntry(self.window)
        self.revenu_imposable_entry_grid = self.revenu_imposable_entry.grid(row=1, column=1, **padding)
        self.revenu_imposable_entry.insert(0,'- $17,183')

        # on the first $49,275 (14%)
        self.revenu_14 = ctk.CTkLabel(self.window, text='Entre $17,183 et $49,275:')
        self.revenu_14_grid = self.revenu_14.grid(row=2, column=0, **padding)
        self.revenu_14_entry = ctk.CTkEntry(self.window)
        self.revenu_14_entry_grid = self.revenu_14_entry.grid(row=2, column=1, **padding)
        self.revenu_14_entry.insert(0, '14%')

        #Entre $49,275 et $98,540 (19%)
        self.revenu_19 = ctk.CTkLabel(self.window, text='Entre $49,275 et $98,540:')
        self.revenu_19_grid = self.revenu_19.grid(row=3, column=0, **padding)
        self.revenu_19_entry = ctk.CTkEntry(self.window)
        self.revenu_19_entry_grid = self.revenu_19_entry.grid(row=3, column=1, **padding)
        self.revenu_19_entry.insert(0, '19%')

        # From $98,540  to $119,910 (24%)
        self.revenu_24 = ctk.CTkLabel(self.window, text='Entre $98,540 et $119,910:')
        self.revenu_24_grid = self.revenu_24.grid(row=4, column=0, **padding)
        self.revenu_24_entry = ctk.CTkEntry(self.window)
        self.revenu_24_entry_grid = self.revenu_24_entry.grid(row=4, column=1, **padding)
        self.revenu_24_entry.insert(0, '24%')

        # From $119,910 and up (25.75%)
        self.revenu_25 = ctk.CTkLabel(self.window, text='$119,910 et plus:')
        self.revenu_25_grid = self.revenu_25.grid(row=5, column=0, **padding)
        self.revenu_25_entry = ctk.CTkEntry(self.window)
        self.revenu_25_entry_grid = self.revenu_25_entry.grid(row=5, column=1, **padding)
        self.revenu_25_entry.insert(0, '25.75%')



        #Total Tax
        self.tax_total = ctk.CTkLabel(self.window, text='Taxe Totale:', text_color= 'red')
        self.tax_total_grid = self.tax_total.grid(row=6, column=0, **padding)
        self.tax_entry = ctk.CTkEntry(self.window)
        self.tax_entry_grid = self.tax_entry.grid(row=6, column=1, **padding)
        self.tax_entry.insert(0, '0')

        # Button
        self.button1 = ctk.CTkButton(self.window, text='Calculate', command=self.calculate_taxe)
        self.button1_grid = self.button1.grid(row=7, column=0, **padding)

        self.button2= ctk.CTkButton(self.window, text= 'Reset', command= self.reset)
        self.button2_grid = self.button2.grid(row=7, column=1, **padding)

    def reset(self):
        self.revenu_entry.delete(0, ctk.END)
        self.revenu_entry.insert(0, '')
        self.revenu_imposable_entry.delete(0, ctk.END)
        self.revenu_imposable_entry.insert(0, '')
        self.update_result(self.revenu_14_entry, '$0')
        self.update_result(self.revenu_19_entry, '$0')
        self.update_result(self.revenu_24_entry, '$0')
        self.update_result(self.revenu_25_entry, '$0')
        self.update_result(self.tax_entry, '$0')
    def run(self):
        self.window.mainloop()

    @staticmethod
    def update_result(entry,text):
        entry.delete(0,ctk.END)
        entry.insert(0,text)

    def calculate_taxe(self):
        try:
            money= float(self.revenu_entry.get())
            imposable = money - 17183
            if money < 0:
                raise ValueError
            elif money <= 17183:
                self.update_result(self.revenu_entry, '')
                self.update_result(self.revenu_imposable_entry,'$0')
                self.update_result(self.revenu_14_entry, '$0')
                self.update_result(self.revenu_19_entry, '$0')
                self.update_result(self.revenu_24_entry, '$0')
                self.update_result(self.revenu_25_entry, '$0')
                self.update_result(self.tax_entry, '$0')
            elif 17183 < money <= 49275:   #Entre $17,183 et $49,275
                self.update_result(self.revenu_imposable_entry, f'${imposable:,.2f}')
                self.update_result(self.revenu_14_entry, f'${(imposable*14)/100:,.2f}')
                self.update_result(self.revenu_19_entry, '$0')
                self.update_result(self.revenu_24_entry, '$0')
                self.update_result(self.revenu_25_entry, '$0')
                self.update_result(self.tax_entry, f'${(imposable*14)/100:,.2f}')

            elif 49275 < money <= 98540:           #Entre $49,275 et $98,540
                x= (32092 * 14) / 100
                y= (imposable-32092)*19/100
                self.update_result(self.revenu_imposable_entry, f'${imposable:,.2f}')
                self.update_result(self.revenu_14_entry, f'${x:,.2f}')
                self.update_result(self.revenu_19_entry, f'${y:,.2f}')
                self.update_result(self.revenu_24_entry, '$0')
                self.update_result(self.revenu_25_entry, '$0')
                self.update_result(self.tax_entry, f'${(x+y):,.2f}')
            elif 98540 < money <= 119910:           #Entre $98,540 et $119,910
                x = (32092 * 14) / 100
                y= (49265*19) / 100
                z= (imposable - (32092 + 49265)) * 24 / 100
                self.update_result(self.revenu_imposable_entry, f'${imposable:,.2f}')
                self.update_result(self.revenu_14_entry, f'${x:,.2f}')
                self.update_result(self.revenu_19_entry, f'${y:,.2f}')
                self.update_result(self.revenu_24_entry,f'${z:,.2f}')
                self.update_result(self.revenu_25_entry, '$0')
                self.update_result(self.tax_entry, f'${(x + y+ z):,.2f}')
            else:                                   #Supérieur à $119,910
                x = (32092 * 14) / 100
                y = (49265 * 19) / 100
                z = (21370 * 24) / 100
                f= ((imposable - (32092+49265+21370))* 25.75 )/100
                self.update_result(self.revenu_imposable_entry, f'${imposable:,.2f}')
                self.update_result(self.revenu_14_entry, f'${x:,.2f}')
                self.update_result(self.revenu_19_entry, f'${y:,.2f}')
                self.update_result(self.revenu_24_entry, f'${z:,.2f}')
                self.update_result(self.revenu_25_entry, f'${f:,.2f}')
                self.update_result(self.tax_entry, f'${(x + y + z + f):,.2f}')

        except ValueError:
            self.update_result(self.revenu_imposable_entry, '$0')
            self.update_result(self.revenu_14_entry, '$0')
            self.update_result(self.revenu_19_entry, '$0')
            self.update_result(self.revenu_24_entry, '$0')
            self.update_result(self.revenu_25_entry, '$0')
            self.update_result(self.tax_entry, 'Invalid Input')





if __name__ == '__main__':
    QC= QuebecTax()
    QC.run()