from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse

from authentication.models import BlockedIPAdresses

class BlockRequests(MiddlewareMixin):
    def process_request(self, request):
        ipadress = request.META.get('REMOTE_ADDR')
        validate_ip = BlockedIPAdresses.objects.filter(ip_adress=ipadress).exists()
        if validate_ip:
            return HttpResponse('You are blocked from this site')