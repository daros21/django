
from django_redis import get_redis_connection


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)
        print("\n moj middleware \n")
        con = get_redis_connection()


        con.incr("klucz z middleware")



        # Code to be executed for each request/response after
        # the view is called.

        return response