class TradingAlert:
    def __init__(self, alert_keywords=None):
        """
        Initialize the TradingAlert with a list of alert keywords.
        """
        if alert_keywords is None:
            alert_keywords = [
                "volume breakout", "neckline", "bullrun", "reversal",
                "support", "resistance", "trendline", "pattern"
            ]
        self.alert_keywords = alert_keywords

    def detect_alert(self, message):
        """
        Check if a message contains any of the alert keywords.
        
        Parameters:
        message (str): The message to be checked.
        
        Returns:
        bool: True if an alert keyword is found, False otherwise.
        """
        message_lower = message.lower()
        for keyword in self.alert_keywords:
            if keyword in message_lower:
                return True
        return False

    def scan_messages(self, messages):
        """
        Scan a list of messages and identify those that contain trading alerts.
        
        Parameters:
        messages (list of str): The messages to be scanned.
        
        Returns:
        list of tuple: A list of tuples with index and message that contain alerts.
        """
        alert_messages = []
        for idx, message in enumerate(messages):
            if self.detect_alert(message):
                alert_messages.append((idx, message))
        return alert_messages


# Example usage
if __name__ == "__main__":
    # Sample messages
    messages = [
        "❗️New users are restricted until they ➡️ CLICK HERE and pass the captcha or be kicked.",
        "I think the real crypto bullrun maybe starting now. See what happens over the next month or 2.",
        "If we breakout of this pattern, it requires a significant volume surge.",
        "Kraken allowed PayPal ser",
        "Do you see wyckoff on chart?",
        "The neckline held and we may see a reversal soon."
    ]

    # Create an instance of TradingAlert
    alert_detector = TradingAlert()

    # Scan messages for trading alerts
    alert_messages = alert_detector.scan_messages(messages)

    # Output detected trading alerts
    for idx, alert_message in alert_messages:
        print(f"Trading alert detected in message {idx}: {alert_message}")
