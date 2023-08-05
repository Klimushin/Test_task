from django.test import TransactionTestCase
import colorama

from db.db_query import ContactModel


class TestDB(TransactionTestCase):
    """
    Command - python manage.py test tests.test_db.TestDB --keepdb
    """
    fixtures = ['nimble.json']

    def setUp(self):
        colorama.init()
        return super().setUp()

    def test_get_all(self):
        print(colorama.Fore.CYAN + self._testMethodName)
        contacts = ContactModel.get_all()
        self.assertEqual(len(contacts), 5, colorama.Fore.RED + "Failed")
        print(colorama.Fore.GREEN + "Passed!")
        print(colorama.Fore.WHITE)

    def test_save_contact(self):
        print(colorama.Fore.CYAN + self._testMethodName)
        contacts = ContactModel.get_all()
        new_contact = "Janae", "Randolph", "janae@capitolfs.eu"
        ContactModel.save_contact(new_contact)
        self.assertEqual(len(ContactModel.get_all()), len(contacts) + 1, colorama.Fore.RED + "Failed")
        print(colorama.Fore.GREEN + "Passed!")
        print(colorama.Fore.WHITE)

    def test_search(self):
        print(colorama.Fore.CYAN + self._testMethodName)
        contacts = [
            (2, 'Ken', 'Underwood III', 'kenneth.underwood@yahoofinance.com'),
            (4, 'Ken', 'Gray', 'kgray@cc-techgroup.com'),
        ]
        ken_search = ContactModel.search('Ken')
        ken_gray_search = ContactModel.search('Ken Gray')
        self.assertEqual(ken_search, contacts, colorama.Fore.RED + "Failed")
        self.assertEqual(ken_gray_search, contacts[1:], colorama.Fore.RED + "Failed")
        print(colorama.Fore.GREEN + "Passed!")
        print(colorama.Fore.WHITE)
