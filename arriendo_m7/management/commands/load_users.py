import csv
from django.core.management.base import BaseCommand
from arriendo_m7.models import Comuna
from arriendo_m7.services import crear_user

# Se ejecuta usando python manage.py test_client

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        archivo = open('data/users.csv', 'r')
        reader = csv.reader(archivo, delimiter=';')
        next(reader) # Se salta la primera linea
        for fila in reader:
            crear_user(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], fila[6])
