from django.test import Client, TransactionTestCase
from django.urls import reverse
import colorama


class TestEndpoints(TransactionTestCase):
    """
    Command - python manage.py test tests.test_db.TestDB --keepdb
    """
    fixtures = ['nimble.json']

    def setUp(self):
        colorama.init()
        self.client = Client()
        return super().setUp()

    def test_search_contact(self):
        print(colorama.Fore.CYAN + "Full text search view")
        param_string = [
            {
                "query_params": {"string": "ken"}
            },
            {
                "query_params": {"string": "ken gray"}
            },
            {
                "query_params": {"string": "ke"}
            },
        ]
        cases = [
            {
                "data": [
                    {'id': 2, 'first_name': 'Ken', 'last_name': 'Underwood III',
                     'email': 'kenneth.underwood@yahoofinance.com'},
                    {'id': 4, 'first_name': 'Ken', 'last_name': 'Gray', 'email': 'kgray@cc-techgroup.com'}
                ],
                "status_code": 200
            },

            {
                "data": [
                    {'id': 4, 'first_name': 'Ken', 'last_name': 'Gray', 'email': 'kgray@cc-techgroup.com'}
                ],
                "status_code": 200
            },

            {
                "data": {'message': 'Contact not found'},
                "status_code": 404
            },
        ]
        for index, param in enumerate(param_string):
            response = self.client.get(reverse("search"), data=param.get("query_params"))
            self.assertEqual(response.json(), cases[index].get("data"), colorama.Fore.RED + "Failed")
            self.assertEqual(response.status_code, cases[index].get("status_code"), colorama.Fore.RED + "Failed")
        print(colorama.Fore.GREEN + "Passed!")
        print(colorama.Fore.WHITE)
