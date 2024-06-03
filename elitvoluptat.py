from collections import namedtuple
from datetime import datetime

# Define a Transaction namedtuple for better structure
Transaction = namedtuple('Transaction', 'amount currency sender recipient timestamp')

def create_transaction(amount, currency, sender, recipient, timestamp):
    # Convert timestamp to a human-readable format
    timestamp = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
    # Create a Transaction object
    return Transaction(amount, currency, sender, recipient, timestamp)

# Example usage
tx = create_transaction(100, "USD", "Alice", "Bob", 1598918400)
print(tx)
