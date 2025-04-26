from django.core.management.base import BaseCommand
from kur.tcmb import fetch_data

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        fetch_data()