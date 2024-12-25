class SimpleOrderBot:
    def __init__(self):
        # Simulate order database
        self.orders = {
            "ORD123": {"status": "shipped", "tracking": "TRK789", "delivery_date": "Dec 26"},
            "ORD456": {"status": "processing", "tracking": None, "delivery_date": "Dec 28"},
            "ORD789": {"status": "delivered", "tracking": "TRK111", "delivery_date": "Dec 23"}
        }
        
        self.conversation_state = {}
    
    def chat(self, user_id: str, message: str) -> str:
        # Initialize or get user's conversation state
        state = self.conversation_state.get(user_id, {"stage": "greeting"})
        
        # Clean the input
        message = message.lower().strip()
        
        # Handle conversation based on current stage
        if state["stage"] == "greeting":
            if any(word in message for word in ["hi", "hello", "hey"]):
                state["stage"] = "ask_for_help"
                self.conversation_state[user_id] = state
                return "Namaskar, hajurlai order status ko barema bujhna ma madat garna sakchu. k tapailai order status ko barema bujhna man xa?"
            
            state["stage"] = "ask_for_help"
            self.conversation_state[user_id] = state
            return "Hello, ma kasari hajurlai madhat garna sakxu?"
            
        elif state["stage"] == "ask_for_help":
            if any(word in message for word in ["yes", "yeah", "sure", "okay", "track", "status", "order"]):
                state["stage"] = "get_order_number"
                self.conversation_state[user_id] = state
                return "Hajurle malai tapaiko order number dinuhola jun 'ORD' baata suru hunxa."
            elif any(word in message for word in ["no", "nai", "xaina"]):
                state["stage"] = "greeting"
                self.conversation_state[user_id] = state
                return "Hajurlai kehi awasyak parema vannu hola."
            else:
                return "k tapai order status bujhna chahanu hunxa? (yes/no) answer dinuhos."
        
        elif state["stage"] == "get_order_number":
            # Try to find an order number in the message
            order_number = None
            for word in message.upper().split():
                if word in self.orders:
                    order_number = word
                    break
            
            if order_number:
                order = self.orders[order_number]
                state["stage"] = "provide_more_info"
                state["current_order"] = order_number
                self.conversation_state[user_id] = state
                
                status_message = f"Your order {order_number} is {order['status']}. "
                if order["status"] == "shipped":
                    status_message += f"Tapaiko order deliver hudei xa hai ra tracking number raheko xa:  {order['tracking']} ani tapaiko saman  {order['delivery_date']}. samma aaune xa."
                elif order["status"] == "processing":
                    status_message += f"tapaiko order processing ma xa expected delivery date: {order['delivery_date']}. "
                elif order["status"] == "delivered":
                    status_message += "tapaiko order deliver vaisakyo confirmation chainxa?"
                
                status_message += "\nTapailai yo order ko bareema aru kehi bujhnu xa?"
                return status_message
            else:
                return "sorry maile hajurko order number vetauna sakina , kripaya sahi order number dinuhos ra ORD baata suru hunu paryo."
        
        elif state["stage"] == "provide_more_info":
            if any(word in message for word in ["no", "nope", "thanks", "thank"]):
                state["stage"] = "greeting"
                self.conversation_state[user_id] = state
                return "You're welcome! hajurlai aru kunei order ko barema bujhna man xa vane sodhu hola."
            
            elif any(word in message for word in ["yes", "yeah", "sure", "tracking"]):
                order = self.orders[state["current_order"]]
                if order["tracking"]:
                    return f"Hajurko order tracking number {order['tracking']}.Tapai yo number liyera tapaiko order track garna saknu hunecha."
                else:
                    return "Tapaiko order ajhai processing maa xa tesaile tracking number chaina. Kripaya order process huna dinuhola."
            
            else:
                return "Sorry, maile hajurko kura bujhina. Kripaya feri vannu hola."
        
        return "Hello, ma hajurko order track garna madhat garna sakxu. Ke hajur order status bujhna chananu hunxa?"

# Example usage
if __name__ == "__main__":
    # Initialize bot
    bot = SimpleOrderBot()
    
    # Example conversation
    user_id = "user123"
    while True:
        message = input("You: ")
        if message.lower() == "exit":
            print("Thank you for chatting with us. Have a great day.")
            break
        response = bot.chat(user_id, message)
        print("Bot:", response)
        print()
