class MercadoPagoWebhookHandler:
    """
    Handle MercadoPago webhook events.
    """

    @staticmethod
    def process(payload):
        """
        Process MercadoPago webhook payload.
        """

        event_type = payload.get("type")

        return {
            "received": True,
            "event_type": event_type,
        }
