from django.core.handlers.base import logger
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from collections import defaultdict
from ..views import ContactByUser

class CustomMiddleware(object):
    def __init__(self, get_response):
        """
        One-time configuration and initialisation.
        """
        self.get_response = get_response

    def __call__(self, request):
        """
        Code to be executed for each request before the view (and later
        middleware) are called.
        """
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        """
        Called just before Django calls the view.
        """
        if request.user.is_authenticated:
            if isinstance(view_func, ContactByUser):
                print('Yes')
                return None
        # return redirect('login')
        # print(view_func)
        # print(view_args)
        # print(view_kwargs)
        # return None
    #
    # def process_exception(self, request, exception):
    #     """
    #     Called when a view raises an exception.
    #     """
    #     print('process_exception')
    #     return None
    #
    # def process_template_response(self, request, response):
    #     """
    #     Called just after the view has finished executing.
    #     """
    #     print('process_template_response')
    #     return response

class CountRequestsMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        self.data_request = defaultdict(list)
        self.count_requests = 0
        self.count_exceptions = 0

    def __call__(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            self.data_request[request.user.username].append(1)
        self.count_requests += 1
        logger.info(f"Handled {request.user.username} {sum(self.data_request[request.user.username])} requests so far")
        return self.get_response(request)

    def process_exception(self, request, exception):
        self.count_exceptions += 1
        logger.error(f"Encountered {self.count_exceptions} exceptions so far")