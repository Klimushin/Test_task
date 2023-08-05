from django.test import TransactionTestCase
import colorama

from db.db_query import ContactModel
from nimble.helper.for_export import export


class TestDBUpdate(TransactionTestCase):
    """
    Command - python manage.py test tests.test_db_update.TestDBUpdate --keepdb
    """
    fixtures = ['nimble.json']

    def setUp(self):
        colorama.init()
        return super().setUp()

    def test_export(self):
        print(colorama.Fore.CYAN + self._testMethodName)
        export()
        self.assertEqual(len(ContactModel.get_all()), 10, colorama.Fore.RED + "Failed")
        export()
        self.assertEqual(len(ContactModel.get_all()), 10, colorama.Fore.RED + "Failed")
        print(colorama.Fore.GREEN + "Passed!")
        print(colorama.Fore.WHITE)
