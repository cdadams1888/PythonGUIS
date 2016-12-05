# Create a Python tkinter GUI for calculating mileage in miles per gallon after a road trip.
# Your GUI should enable a user to enter the gallons used and the miles driven after the drive.
# Design and layout are up to you.
# Clicking a button should display the mileage in mpg right in the GUI, not in a new popup window.
import tkinter
class MileConverterGUI:
    def __init__(self):
        self.main_window     = tkinter.Tk()
        self.top_frame       = tkinter.Frame()
        self.next_frame      = tkinter.Frame()
        self.mid_frame       = tkinter.Frame()
        self.bottom_frame    = tkinter.Frame()

        self.prompt_label  = tkinter.Label(self.top_frame, text='Enter the miles driven:')
        self.miles_entry   = tkinter.Entry(self.top_frame, width=20)
        self.prompt_label.pack(side='left')
        self.miles_entry.pack(side='left')

        self.another_label   = tkinter.Label(self.next_frame, text='Enter the gallons held by the car:')
        self.gallon_entry    = tkinter.Entry(self.next_frame, width=20)
        self.another_label.pack(side='left')
        self.gallon_entry.pack(side='left')

        self.descr_label  = tkinter.Label(self.mid_frame, text='Your MPG is: ')
        self.value        = tkinter.StringVar()
        self.miles_label  = tkinter.Label(self.mid_frame, textvariable = self.value)
        self.descr_label.pack(side='left')
        self.miles_label.pack(side='left')

        self.calc_button = tkinter.Button(self.bottom_frame, text="Convert", command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)

        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.top_frame.pack()
        self.next_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()
        tkinter.mainloop()

    def convert(self):
        miles   = float(self.miles_entry.get())
        gallons = float(self.gallon_entry.get())
        mpg     = miles / gallons
        self.value.set(mpg)

mpg_conv = MileConverterGUI()
