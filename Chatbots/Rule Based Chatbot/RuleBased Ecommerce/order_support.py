class ShoppingBot:
    def __init__(self):
        # Simulate product catalog
        self.products = {
            "laptops": {
                "macbook": {"name": "MacBook Pro", "price": 1299.99, "stock": 10},
                "dell": {"name": "Dell XPS", "price": 999.99, "stock": 15},
                "hp": {"name": "HP Spectre", "price": 1099.99, "stock": 8}
            },
            "phones": {
                "iphone": {"name": "iPhone 15", "price": 999.99, "stock": 20},
                "samsung": {"name": "Samsung S24", "price": 899.99, "stock": 25},
                "pixel": {"name": "Google Pixel 8", "price": 799.99, "stock": 12}
            },
            "headphones": {
                "airpods": {"name": "AirPods Pro", "price": 249.99, "stock": 30},
                "sony": {"name": "Sony WH-1000XM5", "price": 399.99, "stock": 18},
                "bose": {"name": "Bose QC45", "price": 329.99, "stock": 15}
            }
        }
        
        # Shopping cart
        self.carts = {}
        
        # Conversation state
        self.conversation_state = {}
    
    def chat(self, user_id: str, message: str) -> str:
        # Initialize or get user's state and cart
        state = self.conversation_state.get(user_id, {"stage": "greeting"})
        if user_id not in self.carts:
            self.carts[user_id] = {}
            
        message = message.lower().strip()
        
        # Handle exit commands
        if message in ["quit", "exit", "bye"]:
            self.conversation_state[user_id] = {"stage": "greeting"}
            return "Thanks for shopping with us! Have a great day!"
        
        # Handle cart viewing from any stage
        if "cart" in message:
            return self._show_cart(user_id)
        
        # Handle checkout from any stage
        if "checkout" in message:
            return self._handle_checkout(user_id)
        
        # Main conversation flow
        if state["stage"] == "greeting":
            return self._handle_greeting(user_id)
            
        elif state["stage"] == "category_selection":
            return self._handle_category_selection(user_id, message)
            
        elif state["stage"] == "product_selection":
            return self._handle_product_selection(user_id, message)
            
        elif state["stage"] == "quantity_selection":
            return self._handle_quantity_selection(user_id, message)
            
        elif state["stage"] == "confirmation":
            return self._handle_confirmation(user_id, message)
        
        return "I'm not sure what you'd like to do. Would you like to browse our products?"

    def _handle_greeting(self, user_id: str) -> str:
        categories = ", ".join(self.products.keys())
        self.conversation_state[user_id] = {"stage": "category_selection"}
        return f"Welcome to our store! What type of product are you looking for? We have: {categories}"

    def _handle_category_selection(self, user_id: str, message: str) -> str:
        category = next((cat for cat in self.products.keys() if cat in message), None)
        if category:
            self.conversation_state[user_id] = {
                "stage": "product_selection",
                "category": category
            }
            products_list = []
            for key, product in self.products[category].items():
                products_list.append(f"{product['name']}: ${product['price']}")
            products_str = "\n- ".join(products_list)
            return f"Great! Here are our {category}:\n- {products_str}\n\nWhich one interests you?"
        
        categories = ", ".join(self.products.keys())
        return f"Please choose from these categories: {categories}"

    def _handle_product_selection(self, user_id: str, message: str) -> str:
        category = self.conversation_state[user_id]["category"]
        product = None
        
        # Find product based on name or key
        for key, prod in self.products[category].items():
            if key in message.lower() or prod["name"].lower() in message.lower():
                product = prod
                product_key = key
                break
        
        if product:
            if product["stock"] > 0:
                self.conversation_state[user_id].update({
                    "stage": "quantity_selection",
                    "product": product_key
                })
                return f"How many {product['name']} would you like? (Available: {product['stock']})"
            else:
                return f"Sorry, {product['name']} is currently out of stock. Would you like to look at something else?"
        
        products_list = ", ".join([p["name"] for p in self.products[category].values()])
        return f"Please choose from these products: {products_list}"

    def _handle_quantity_selection(self, user_id: str, message: str) -> str:
        try:
            quantity = int(message)
            category = self.conversation_state[user_id]["category"]
            product_key = self.conversation_state[user_id]["product"]
            product = self.products[category][product_key]
            
            if quantity <= 0:
                return "Please enter a positive number."
            
            if quantity > product["stock"]:
                return f"Sorry, we only have {product['stock']} units available. Please enter a smaller quantity."
            
            self.conversation_state[user_id].update({
                "stage": "confirmation",
                "quantity": quantity
            })
            
            total = quantity * product["price"]
            return f"Would you like to add {quantity} {product['name']}(s) to your cart for ${total:.2f}? (yes/no)"
            
        except ValueError:
            return "Please enter a valid number."

    def _handle_confirmation(self, user_id: str, message: str) -> str:
        if message.lower() in ["yes", "y", "sure", "okay"]:
            category = self.conversation_state[user_id]["category"]
            product_key = self.conversation_state[user_id]["product"]
            quantity = self.conversation_state[user_id]["quantity"]
            
            # Add to cart
            if product_key in self.carts[user_id]:
                self.carts[user_id][product_key] += quantity
            else:
                self.carts[user_id][product_key] = quantity
            
            # Reset state
            self.conversation_state[user_id] = {"stage": "category_selection"}
            
            return f"Added to cart! Would you like to browse more products? You can also say 'cart' to view your cart or 'checkout' to complete your purchase."
        
        elif message.lower() in ["no", "n", "nope"]:
            self.conversation_state[user_id] = {"stage": "category_selection"}
            return "No problem! Would you like to look at something else?"
        
        return "Please say 'yes' or 'no'."

    def _show_cart(self, user_id: str) -> str:
        if not self.carts[user_id]:
            return "Your cart is empty. Would you like to browse our products?"
        
        cart_items = []
        total = 0
        
        for product_key, quantity in self.carts[user_id].items():
            for category in self.products.values():
                if product_key in category:
                    product = category[product_key]
                    item_total = quantity * product["price"]
                    total += item_total
                    cart_items.append(f"{product['name']} x{quantity}: ${item_total:.2f}")
        
        cart_str = "\n- ".join(cart_items)
        return f"Your cart:\n- {cart_str}\n\nTotal: ${total:.2f}\n\nSay 'checkout' to complete your purchase or continue shopping!"

    def _handle_checkout(self, user_id: str) -> str:
        if not self.carts[user_id]:
            return "Your cart is empty. Would you like to browse our products?"
        
        # Simulate checkout process
        total = sum(
            self.products[cat][prod]["price"] * qty
            for prod, qty in self.carts[user_id].items()
            for cat in self.products
            if prod in self.products[cat]
        )
        
        # Clear cart and reset state
        self.carts[user_id] = {}
        self.conversation_state[user_id] = {"stage": "greeting"}
        
        return f"Thank you for your order! Total payment: ${total:.2f}\nYour order will be processed shortly.\n\nWould you like to browse more products?"

# Example usage
if __name__ == "__main__":
    bot = ShoppingBot()
    
    # Example conversation
    user_id = "user123"
    conversation = [
        "hi",
        "laptops",
        "macbook",
        "2",
        "yes",
        "cart",
        "checkout"
    ]
    
    print("Example shopping conversation:")
    for message in conversation:
        print(f"\nUser: {message}")
        response = bot.chat(user_id, message)
        print(f"Bot: {response}")