from django.http import HttpResponse

class StripeWH_Handler:
    """Handle Strip Webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """ 
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Webhook recevied: {event["type"]}',
            status=200)