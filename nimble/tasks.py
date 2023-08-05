import requests
from Nimble_test_task.celery import app
from db.db_query import ContactModel

from Nimble_test_task.settings import API_URL, AUTH_TOKEN


@app.task
def check_contacts():

    contacts = ContactModel.get_all()

    headers = {"Authorization": f"Bearer {AUTH_TOKEN}"}
    params = (('record_type', 'person'), ('fields', 'first name,last name,email'))
    response_data = requests.get(API_URL, headers=headers, params=params).json()

    contacts_list = response_data.get('resources')
    for contact in contacts_list:
        data = contact.get('fields')
        first_name = data.get('first name') and data.get('first name')[0].get('value')
        last_name = data.get('last name') and data.get('last name')[0].get('value')
        email = data.get('email') and data.get('email')[0].get('value')
        contact_item = (first_name, last_name, email)
        if all(contact_item):
            if contact_item not in contacts:
                ContactModel.save_contact(contact_item)
