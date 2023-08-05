from django.http import JsonResponse
from db.db_query import ContactModel


def search_contact(request):
    search_params = request.GET.get('string')
    result = []
    if search_params:
        result_list = ContactModel.search(search_params)
        for item in result_list:
            contact_columns = ["id", "first_name", "last_name", "email", ]
            contact_item = dict(zip(contact_columns, item))
            result.append(contact_item)
    if result:
        return JsonResponse(result, safe=False)

    return JsonResponse(status=404, data={'message': 'Contact not found'})
