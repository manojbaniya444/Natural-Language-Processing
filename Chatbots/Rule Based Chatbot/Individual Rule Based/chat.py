# Import the chatbot class
from app import EcommerceSupportBot

# Initialize the bot
bot = EcommerceSupportBot()

# # Simulate a product database (you would typically connect to your real database)
# bot.product_catalog = {
#     'PROD123': {
#         'name': 'Wireless Headphones',
#         'price': 99.99,
#         'stock': 50
#     },
#     'PROD456': {
#         'name': 'Smart Watch',
#         'price': 199.99,
#         'stock': 25
#     }
# }

# # Simulate an order database (you would typically connect to your real database)
# bot.order_status_db = {
#     'ORD123456': {
#         'status': 'shipped',
#         'user_id': 'user123',
#         'items': ['PROD123'],
#         'tracking': 'TRK789012'
#     },

# from ecommerce_support_bot import EcommerceSupportBot

# Initialize the bot
# bot = EcommerceSupportBot()

# Simulate a product database (you would typically connect to your real database)
bot.product_catalog = {
    'PROD123': {
        'name': 'Wireless Headphones',
        'price': 99.99,
        'stock': 50
    },
    'PROD456': {
        'name': 'Smart Watch',
        'price': 199.99,
        'stock': 25
    }
}

# Simulate an order database (you would typically connect to your real database)
bot.order_status_db = {
    'order1': {
        'status': 'shipped',
        'user_id': 'user123',
        'items': ['PROD123'],
        'tracking': 'TRK789012'
    },
    'order2': {
        'status': 'processing',
        'user_id': 'user123',
        'items': ['PROD456']
    }
}


user_id = "user123"
message = "mero order ko status ke ho order1"
response = bot.process_message(user_id, message)
print(response)
