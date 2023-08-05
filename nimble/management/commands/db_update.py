from django.core.management import BaseCommand
from nimble.helper.for_export import export


class Command(BaseCommand):
    def handle(self, *args, **options):
        export()
