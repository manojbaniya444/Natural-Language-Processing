import re
from datetime import datetime
from typing import Dict, List, Tuple, Optional

class EcommerceSupportBot:
    def __init__(self):
        self.order_status_db = {}  # Simulate order database
        self.product_catalog = {}  # Simulate product database
        self.user_context = {}     # Store conversation context
        
    def process_message(self, user_id: str, message: str) -> str:
        """
        Main entry point for processing user messages.
        Returns appropriate response based on intent detection and context.
        """
        # Clean and normalize input
        message = message.lower().strip()
        
        # Update or initialize user context
        if user_id not in self.user_context:
            self.user_context[user_id] = {
                'last_intent': None,
                'pending_info': None,
                'conversation_stage': 'greeting'
            }
        
        # Check for exit phrases
        if self._is_exit_phrase(message):
            self.user_context[user_id]['conversation_stage'] = 'ended'
            return "Thank you for chatting with us! Is there anything else I can help you with?"
        
        # Handle greeting
        if self._is_greeting(message):
            return self._handle_greeting()
        
        # Detect intent
        intent, entities = self._detect_intent(message)
        
        # Update context with current intent
        self.user_context[user_id]['last_intent'] = intent
        
        # Process based on intent
        response = self._process_intent(intent, entities, user_id)
        
        return response

    def _detect_intent(self, message: str) -> Tuple[str, Dict]:
        """
        Detects the intent of the user message and extracts relevant entities.
        Returns tuple of (intent, entities_dict)
        """
        # Define intent patterns
        intent_patterns = {
            'order_status': r'(?:order|track|package|delivery|shipping).*(?:status|where|when)',
            'return_request': r'(?:return|refund|send back|exchange)',
            'product_info': r'(?:product|item|price|availability|stock)',
            'payment_issue': r'(?:payment|charge|bill|invoice|credit card)',
            'technical_support': r'(?:website|login|account|password|error)',
            'shipping_info': r'(?:shipping|delivery|time|cost)',
            'complaint': r'(?:wrong|broken|damaged|not working|complaint)',
            'cancel_order': r'(?:cancel|stop|void).*(?:order|purchase)',
        }
        
        # Extract entities (e.g., order numbers, product IDs)
        entities = {
            'order_number': self._extract_order_number(message),
            'product_id': self._extract_product_id(message),
            'email': self._extract_email(message)
        }
        
        # Match patterns to determine intent
        for intent, pattern in intent_patterns.items():
            if re.search(pattern, message):
                return intent, entities
                
        return 'general_query', entities

    def _process_intent(self, intent: str, entities: Dict, user_id: str) -> str:
        """
        Processes the detected intent and returns appropriate response
        """
        intent_handlers = {
            'order_status': self._handle_order_status,
            'return_request': self._handle_return_request,
            'product_info': self._handle_product_info,
            'payment_issue': self._handle_payment_issue,
            'technical_support': self._handle_technical_support,
            'shipping_info': self._handle_shipping_info,
            'complaint': self._handle_complaint,
            'cancel_order': self._handle_cancel_order,
            'general_query': self._handle_general_query
        }
        
        handler = intent_handlers.get(intent, self._handle_general_query)
        return handler(entities, user_id)

    def _handle_order_status(self, entities: Dict, user_id: str) -> str:
        """
        Handles order status queries
        """
        order_number = entities.get('order_number')
        
        if not order_number:
            self.user_context[user_id]['pending_info'] = 'order_number'
            return "I'd be happy to help you check your order status. Could you please provide your order number?"
        
        # Simulate order status lookup
        status = self.order_status_db.get(order_number, {}).get('status')
        if status:
            return f"Your order #{order_number} is currently {status}. Is there anything else you'd like to know?"
        return "I couldn't find that order number in our system. Please verify the number and try again."

    def _handle_return_request(self, entities: Dict, user_id: str) -> str:
        """
        Handles return and refund requests
        """
        order_number = entities.get('order_number')
        
        if not order_number:
            self.user_context[user_id]['pending_info'] = 'order_number'
            return "I can help you with your return request. Could you please provide your order number?"
            
        return """Here's our return process:
1. Visit our returns portal at returns.example.com
2. Enter your order number and email
3. Select the items you want to return
4. Print the return shipping label
5. Drop off the package at any authorized shipping location

Would you like me to email you these instructions?"""

    def _handle_product_info(self, entities: Dict, user_id: str) -> str:
        """
        Handles product information queries
        """
        product_id = entities.get('product_id')
        
        if not product_id:
            return "I'd be happy to help you with product information. Could you please provide the product name or ID?"
            
        # Simulate product lookup
        product = self.product_catalog.get(product_id)
        if product:
            return f"Here are the details for {product['name']}: Price: ${product['price']}, Availability: {product['stock']} units in stock"
        return "I couldn't find that product in our catalog. Could you please verify the product ID?"

    def _extract_order_number(self, message: str) -> Optional[str]:
        """
        Extracts order number from message using regex
        """
        pattern = r'(?:order[:#\s]*)?([A-Z0-9]{6,12})'
        match = re.search(pattern, message.upper())
        return match.group(1) if match else None

    def _extract_product_id(self, message: str) -> Optional[str]:
        """
        Extracts product ID from message using regex
        """
        pattern = r'(?:product[:#\s]*)?([A-Z0-9]{4,10})'
        match = re.search(pattern, message.upper())
        return match.group(1) if match else None

    def _extract_email(self, message: str) -> Optional[str]:
        """
        Extracts email address from message using regex
        """
        pattern = r'[\w\.-]+@[\w\.-]+\.\w+'
        match = re.search(pattern, message)
        return match.group() if match else None

    def _is_greeting(self, message: str) -> bool:
        """
        Checks if the message is a greeting
        """
        greetings = {'hello', 'hi', 'hey', 'greetings', 'good morning', 'good afternoon', 'good evening'}
        return any(greeting in message for greeting in greetings)

    def _is_exit_phrase(self, message: str) -> bool:
        """
        Checks if the message is an exit phrase
        """
        exit_phrases = {'bye', 'goodbye', 'exit', 'quit', 'end', 'thanks', 'thank you'}
        return any(phrase in message for phrase in exit_phrases)

    def _handle_greeting(self) -> str:
        """
        Returns appropriate greeting based on time of day
        """
        hour = datetime.now().hour
        if 5 <= hour < 12:
            greeting = "Good morning"
        elif 12 <= hour < 17:
            greeting = "Good afternoon"
        else:
            greeting = "Good evening"
            
        return f"{greeting}! I'm your customer service assistant. How can I help you today?"

    def _handle_payment_issue(self, entities: Dict, user_id: str) -> str:
        """
        Handles payment-related issues
        """
        return """I understand you're having an issue with payment. For your security, please:
1. Check your payment method details are correct
2. Ensure sufficient funds are available
3. Try clearing your browser cache

If the issue persists, would you like me to connect you with our payments team?"""

    def _handle_technical_support(self, entities: Dict, user_id: str) -> str:
        """
        Handles technical support queries
        """
        return """Let's try these common solutions:
1. Clear your browser cache and cookies
2. Try using a different browser
3. Ensure your browser is up to date

If you're still experiencing issues, would you like me to connect you with our technical support team?"""

    def _handle_shipping_info(self, entities: Dict, user_id: str) -> str:
        """
        Handles shipping-related queries
        """
        return """Our standard shipping options are:
- Standard (5-7 business days): Free for orders over $50
- Express (2-3 business days): $12.99
- Next Day: $24.99

Would you like to know about international shipping options?"""

    def _handle_complaint(self, entities: Dict, user_id: str) -> str:
        """
        Handles customer complaints
        """
        return "I'm sorry to hear you're having an issue. To better assist you, could you please provide your order number and describe the problem in detail? This will help us resolve your concern as quickly as possible."

    def _handle_cancel_order(self, entities: Dict, user_id: str) -> str:
        """
        Handles order cancellation requests
        """
        order_number = entities.get('order_number')
        
        if not order_number:
            self.user_context[user_id]['pending_info'] = 'order_number'
            return "I can help you cancel your order. Could you please provide your order number?"
            
        # Simulate order status check
        order = self.order_status_db.get(order_number, {})
        if order.get('status') == 'shipped':
            return "I apologize, but this order has already been shipped and cannot be cancelled. Would you like information about our return process instead?"
        return f"I've initiated the cancellation for order #{order_number}. You should receive a confirmation email shortly. Is there anything else I can help you with?"

    def _handle_general_query(self, entities: Dict, user_id: str) -> str:
        """
        Handles general queries that don't match other intents
        """
        return "I'm not quite sure I understood your question. Could you please rephrase it? I can help you with order status, returns, product information, shipping, and technical support."