# im using csv to store the submitted contacts so i can view them via my super safe admin route
import csv

class contactHandler:
    def __init__(self, filename): # we need to initialise the contact handler with a file name
        self.filename = filename

    def write_contact(self, row):
        # using open file and csv writer to save our contact variables above to a file from the form
        # you could also use a database but for this purpose i felt like there was no need
        with open(self.filename, 'a', newline='') as contactFile:
            writer = csv.writer(contactFile)
            writer.writerow(row)

    def read_contacts(self):
        # define our contact list
        contacts = []
        # read all the data from inside our contacts.csv and return the data
        try:
            with open(self.filename, newline='') as contactFile:
                reader = csv.reader(contactFile)
                contacts = [row for row in reader]
        except FileNotFoundError:
            print("Error with contacts file.") # ran into some errors so decide to add a little bit of error handling
        return contacts
