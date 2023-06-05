from django.core.management.base import BaseCommand
from excel_streaming.models import DummyData


class Command(BaseCommand):
    help = 'Generates dummy data for the DummyData model.'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='The number of dummy data records to generate.')

    def handle(self, *args, **options):
        count = options['count']
        dummy_data = [DummyData(data=f'Dato {i + 1}') for i in range(count)]
        DummyData.objects.bulk_create(dummy_data)
        self.stdout.write(self.style.SUCCESS(f'Successfully generated {count} dummy data records.'))
