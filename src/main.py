from datetime import datetime

def reconcile_transactions(transactions, initial_balance):
    """
    Reconciles a batch of financial transactions, calculates the net balance,
    identifies discrepancies, and applies penalties for overdrafts.

    Args:
        transactions (list): A list of dictionaries with 'id', 'amount', 'timestamp', and 'type' keys.
                            'type' can be 'credit' or 'debit'.
        initial_balance (float): The starting balance for the account.

    Returns:
        dict: A report containing the final balance, discrepancies, and overdraft penalties.
    """
    if not isinstance(initial_balance, (int, float)) or initial_balance < 0:
        raise ValueError("Initial balance must be a non-negative number.")

    final_balance = initial_balance
    discrepancies = []
    overdraft_penalty = 35.0  # Fixed penalty for each overdraft
    overdraft_count = 0

    for transaction in transactions:
        # Validate transaction structure
        if "id" not in transaction or "amount" not in transaction or "timestamp" not in transaction or "type" not in transaction:
            discrepancies.append({**transaction, "reason": "Missing required fields"})
            continue

        # Validate amount
        amount = transaction["amount"]
        if not isinstance(amount, (int, float)) or amount <= 0:
            discrepancies.append({**transaction, "reason": "Invalid amount"})
            continue

        # Validate timestamp
        try:
            datetime.strptime(transaction["timestamp"], "%Y-%m-%dT%H:%M:%S")
        except ValueError:
            discrepancies.append({**transaction, "reason": "Invalid timestamp format"})
            continue

        # Process transaction
        transaction_type = transaction["type"]
        if transaction_type == "credit":
            final_balance += amount
        elif transaction_type == "debit":
            final_balance -= amount
            if final_balance < 0:
                overdraft_count += 1
                final_balance -= overdraft_penalty
        else:
            discrepancies.append({**transaction, "reason": "Invalid transaction type"})
            continue

    return {
        "final_balance": round(final_balance, 2),
        "discrepancies": discrepancies,
        "overdraft_count": overdraft_count,
        "total_penalties": round(overdraft_count * overdraft_penalty, 2),
    }



def process_text(input_text):
    if input_text:
        result = []
        for line in input_text.split('\n'):
            if line.startswith('#'):
                if len(line) > 5:
                    result.append(line.strip().upper())
                else:
                    result.append("SHORT_HEADER")
            else:
                if "TODO" in line:
                    result.append(f"TODO: {line.strip()}")
                else:
                    words = line.split()
                    if len(words) > 10:
                        result.append("LONG_LINE")
                    else:
                        result.append(' '.join(w[::-1] for w in words))
        return '\n'.join(result)
    else:
        return "EMPTY_INPUT"

def sorting_a_list(input_list):
    if isinstance(input_list, list):
        return sorted(input_list)
    else:
        raise ValueError("Input must be a list.")
    
def sort_and_process_list(data):
    if not isinstance(data, list):
        raise ValueError("Data must be a list.")

    # Sort the list
    sorted_data = sorted(data)

    # Extract times
    times = [datetime.strptime(item['timestamp'], "%Y-%m-%dT%H:%M:%S") for item in sorted_data if 'timestamp' in item]

    # Sort times as well (just in case, though list should already be sorted)
    times_sorted = sorted(times)

    # Process each item
    processed_data = []
    for item in sorted_data:
        if 'amount' in item and item['amount'] > 1000:
            item['amount'] = 1000
        processed_data.append(item)

    # Sort again by amount descending
    result = sorted(processed_data, key=lambda x: x.get('amount', 0), reverse=True)

    return result, times_sorted


def analyze_data(data):
    if not isinstance(data, list):
        raise ValueError("Data must be a list.")
    
    # Filter data with amounts greater than 500
    filtered_data = [entry for entry in data if entry.get('amount', 0) > 500]
    
    # Process timestamps: convert each to a datetime object
    processed_timestamps = [
        datetime.strptime(entry['timestamp'], "%Y-%m-%dT%H:%M:%S") 
        for entry in filtered_data if 'timestamp' in entry
    ]
    
    # Sort the filtered data by amount in ascending order
    sorted_filtered_data = sorted(filtered_data, key=lambda x: x.get('amount', 0))
    
    return sorted_filtered_data, processed_timestamps



