from django.core.management.base import BaseCommand
from django.core.management.utils import get_random_secret_key


class Command(BaseCommand):
    help = 'Generate a secure Django secret key for production'

    def handle(self, *args, **options):
        secret_key = get_random_secret_key()
        self.stdout.write(
            self.style.SUCCESS(f'Generated secret key: {secret_key}')
        )
        self.stdout.write(
            self.style.WARNING(
                'Add this to your .env file as SECRET_KEY=your-generated-key'
            )
        )
