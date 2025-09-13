import re  # For simple pattern matching

# Simulated data (in a real app, this would come from a database)
orders = {
    "12345": {"status": "Shipped", "eta": "September 15, 2025"},
    "67890": {"status": "Delivered", "eta": "September 10, 2025"}
}

products = {
    "widget": "Our Widget is a high-quality gadget priced at $19.99. Features: Durable, portable.",
    "gadget": "The Gadget Pro is $49.99 with advanced features like Bluetooth connectivity."
}

def get_response(user_input):
    user_input = user_input.lower()
    
    # Order status check
    order_match = re.search(r'order\s*(status|track)?\s*(\d+)', user_input)
    if order_match:
        order_id = order_match.group(2)
        if order_id in orders:
            status = orders[order_id]["status"]
            eta = orders[order_id]["eta"]
            return f"Your order {order_id} is {status}. Estimated arrival: {eta}."
        else:
            return "Sorry, I couldn't find that order ID. Please check and try again."
    
    # Returns/refunds
    if "return" in user_input or "refund" in user_input:
        return "To process a return, please provide your order ID and reason. Our policy allows returns within 30 days."
    
    # Product info
    for product in products:
        if product in user_input:
            return products[product]
    
    # General help
    if "help" in user_input or "support" in user_input:
        return "How can I assist? Options: Order status, returns, product info."
    
    # Default fallback
    return "I'm sorry, I didn't understand that. Try asking about orders, returns, or products."

# Main loop for the bot
def run_bot():
    print("Welcome to Customer Service Bot! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Bot: Goodbye!")
            break
        response = get_response(user_input)
        print(f"Bot: {response}")

# Start the bot
if __name__ == "__main__":
    run_bot()