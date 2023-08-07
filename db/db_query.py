from django.db import connection


class ContactModel:

    @staticmethod
    def __query(query_string, fetching=False):
        with connection.cursor() as cursor:
            try:
                cursor.execute(query_string)
                connection.commit()
                if fetching:
                    rows = cursor.fetchall()
                    return rows
                # connection.commit()
            except Exception as e:
                print(e)
                connection.rollback()
                return
            return

    @classmethod
    def get_all(cls):
        all_contacts_query = f"""SELECT first_name, last_name, email FROM {'nimble_contact'}"""
        return cls.__query(all_contacts_query, fetching=True)

    @classmethod
    def save_contact(cls, contact):
        write_to_db = f"""INSERT INTO nimble_contact (first_name, last_name, email) VALUES {contact}"""
        return cls.__query(write_to_db)

    @classmethod
    def search(cls, search_string):
        search_query = f"""
                SELECT * FROM nimble_contact
                WHERE to_tsvector(first_name) || to_tsvector(last_name) || to_tsvector(email)
                @@ plainto_tsquery('{search_string}')
                """
        return cls.__query(search_query, fetching=True)

