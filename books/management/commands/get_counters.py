from django.core.management.base import BaseCommand
from django_redis import get_redis_connection


class Command(BaseCommand):
    help = "Pobiera liczniki"

    def handle(self, *args, **opitons):
        con = get_redis_connection()
        keys = con.keys()
        print("liczniki: ")
        for k in keys:
            print (k.decode(), " : ", con.get(k).decode())