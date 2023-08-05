import csv

from db.db_query import ContactModel


def export():
    try:
        with open('Contacts.csv') as file:
            reader = csv.reader(file)
            db_contacts = ContactModel.get_all()
            next(reader)
            for row in reader:
                contact = tuple(row)
                if contact not in db_contacts:
                    ContactModel.save_contact(contact)

    except Exception as e:
        print(e)
