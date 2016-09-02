#IMPORT MODULES
import csv
from tkinter import *

#IMPORT ClASSES
from RoutePlan import Route
from AirportAtlas  import AirportAtlas
from PlaneList import PlaneList
from CurrencyRates import CurrencyList, CurrencyRateList

#CREATE OBJECTS
atlas = AirportAtlas()
planes = PlaneList()
currency = CurrencyList()
currencyRates = CurrencyRateList()


#####################GUI#################################

class ApplicationGui(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        root.geometry("800x500")
        root.title("Fuel-O-Tron 1.0")

        #GUI IMAGE HEADER AND ICON
        photo = PhotoImage(file='fuelotron.gif')
        root.iconbitmap('fuelicon.ico')
        label = Label(image=photo)
        label.image = photo
        label.grid(row=1, column=0, columnspan=4, sticky=W)

        #GUI WIDGETS (Entry boxes, buttons, text box)
        self.l = Label(root, text="         Airport of Origin")
        self.l.grid(row=3, column=0, sticky=W, pady=3 , padx=5)
        self.l2 = Label(root, text="                 ITINERARY")
        self.l2.grid(row=6, column=0, sticky=W)
        self.e2 = Entry(root)
        self.e2.grid(row=7, column=0, padx=20, pady=5, sticky=W)
        self.e2.insert(0, "e.g. 'AVO'")
        self.e3 = Entry(root)
        self.e3.grid(row=8, column=0, padx=20, pady=5, sticky=W)
        self.e3.insert(0, "e.g. 'JXN'")
        self.e4 = Entry(root)
        self.e4.grid(row=9, column=0, padx=20, pady=5, sticky=W)
        self.e4.insert(0, "e.g. 'BUU'")
        self.e5 = Entry(root)
        self.e5.grid(row=10, column=0, padx=20, pady=5, sticky=W)
        self.e5.insert(0, "e.g. 'JOT'")
        self.b2= Button(root, width=16, text="Write to CSV File...", command=self.exportManifest)
        self.b2.grid(row=15, column=0, sticky=W, pady=0, padx=20)
        self.b= Button(root, width=16, text="Calculate Route", command= self.routeCalculator, bg="#99c2ff")
        self.b.grid(row=18, column=0, sticky=W, pady=0, padx=20)
        self.e = Entry(root)
        self.e.grid(row=5, column=0,padx=20, pady=5, sticky=W)
        self.e.insert(0, "e.g. 'DUB'")
        self.l2 = Label(root, text="Aircraft")
        self.l2.grid(column=1,columnspan=1, row=3, padx=5, pady=5, sticky=E+W)
        self.listbox = Listbox(root, height=16)
        self.listbox.grid(rowspan=16, column=1,columnspan=1, row=4, padx=5, pady=5, sticky=E+W)
        self.listbox.insert(END, "A319")

        #LISTBOX
        for item in ["A320", "A321", "A330", "737", "747", "757", "767", "777", "BAE146", "DC8", "F50","MD11","A400M", "C212", "V22"]:
            self.listbox.insert(END, item)
        self.w = Text (root, width=65, height=18, wrap=WORD, font=("arial",8))
        self.w.grid(column=2, columnspan=1, row=4, rowspan=16, sticky=E)
        self.w.insert(END, "Flight information will be displayed here...")

##################CREATE MANIFEST CLASS AND CALCULATE ROUTE##############

    def routeCalculator(self):
        entry1 = self.e.get()
        entry2 = self.e2.get()
        entry3 = self.e3.get()
        entry4 = self.e4.get()
        entry5 = self.e5.get()
        try:
            manifest = Route(atlas.getAirport(self.e.get()).name, atlas.getAirport(self.e2.get()),
                       atlas.getAirport(self.e3.get()), atlas.getAirport(self.e4.get()),
                       atlas.getAirport(self.e5.get()), planes.getPlane(self.listbox.get(ACTIVE)),
                       currencyRates.getExchangeRate(currency.getCurrency(atlas.getAirport(self.e.get()).country).currency_code).to_euro,
                       currencyRates.getExchangeRate(currency.getCurrency(atlas.getAirport(self.e2.get()).country).currency_code).to_euro,
                       currencyRates.getExchangeRate(currency.getCurrency(atlas.getAirport(self.e3.get()).country).currency_code).to_euro,
                       currencyRates.getExchangeRate(currency.getCurrency(atlas.getAirport(self.e4.get()).country).currency_code).to_euro)
            itinerary = [entry1, entry2, entry3, entry4, entry5]
            x = manifest.routePlanner(itinerary, entry1, entry1, self.listbox.get(ACTIVE))

##################PRINT DATA TO INFORMATION DISPLAY IN GUI##############

            if len(x) > 1:
                self.w.delete(1.0, END)
                self.w.insert(1.0, cleanText(str(x[0])))
                self.w.insert(2.0, cleanText(str(x[1])))
                self.w.insert(3.0, cleanText(str(x[2])))
                self.w.insert(4.0, cleanText(str(x[3])))
                self.w.insert(5.0, cleanText(str(x[4])))
                self.w.insert(6.0, "\nTotal Distance: ")
                self.w.insert(9.0, str(round(x[5],2)) + " kilometers")
                self.w.insert(8.0, "\nTotal Fuel Purchased: ")
                self.w.insert(11.0, str(round(x[6],2)) + " litres")
                self.w.insert(10.0, "\n")
                self.w.insert(12.0, "\nTotal Cost: ")
                self.w.insert(15.0, str(round(x[7],2)) + " euros")
                self.w.insert(14.0, "\nCurrencies Utilised: ")
                self.w.insert(17.0, cleanText(str(x[8])))
            else:
                self.w.delete(1.0, END)
                self.w.insert(END, cleanText(str(x)))

        except:
            self.w.delete(1.0, END)
            self.w.insert(1.0, "ERROR: \n \nSome or all of the flight information you have entered is invalid. Please verify the data and try again.")


##################CSV WRITER##############
    def exportManifest(self):
        entry1 = self.e.get()
        entry2 = self.e2.get()
        entry3 = self.e3.get()
        entry4 = self.e4.get()
        entry5 = self.e5.get()
        manifest = Route(atlas.getAirport(self.e.get()).name, atlas.getAirport(self.e2.get()),
                   atlas.getAirport(self.e3.get()), atlas.getAirport(self.e4.get()),
                   atlas.getAirport(self.e5.get()), planes.getPlane(self.listbox.get(ACTIVE)),
                   currencyRates.getExchangeRate(currency.getCurrency(atlas.getAirport(self.e.get()).country).currency_code).to_euro,
                   currencyRates.getExchangeRate(currency.getCurrency(atlas.getAirport(self.e2.get()).country).currency_code).to_euro,
                   currencyRates.getExchangeRate(currency.getCurrency(atlas.getAirport(self.e3.get()).country).currency_code).to_euro,
                   currencyRates.getExchangeRate(currency.getCurrency(atlas.getAirport(self.e4.get()).country).currency_code).to_euro)
        itinerary = [entry1, entry2, entry3, entry4, entry5]
        x = manifest.routePlanner(itinerary, entry1, entry1, self.listbox.get(ACTIVE))
        self.exported_manifest = [x[9]]
        with open('empty_csv_file.csv', 'w') as f:
            self.writer = csv.writer(f)
            self.writer.writerows([self.exported_manifest],)

def cleanText(text):
        text = re.sub('[(){}<>"]', '', text)
        text = text.replace("'", "")
        text = text.replace(",", "")
        text = text.replace("[", "")
        text = text.replace("]", "")
        return text + "\n"

root = Tk()
app = ApplicationGui(root)
root.mainloop()
