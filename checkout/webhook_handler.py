from django.http import HttpResponse

class StripeWH_Handler:
    """Handle Stripe Webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """ 
        Handle a generic/unknown/unexpected webhook event
        """
        print(f'Unhandled event received: {event}')  # Print the full event data
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """ 
        Handle the payment_intent_succeeded webhook from Stripe
        """
        intent = event.data.object
        print(f'Payment intent succeeded: {intent}')  # Print the intent object
        print(f'Full event data: {event}')  # Print the full event data

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """ 
        Handle the payment_intent_failed webhook from Stripe
        """
        print(f'Payment intent failed: {event}')  # Print the full event data
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
