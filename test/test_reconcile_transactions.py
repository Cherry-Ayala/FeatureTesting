# test_reconcile_transactions.py
# Instructions: 
# To run these tests, you need to have Python installed. This script uses the built-in `unittest` module.
# Run the tests by executing the command: python -m unittest test_reconcile_transactions.py

import unittest
from datetime import datetime
from main import reconcile_transactions

class TestReconcileTransactions(unittest.TestCase):

    # Happy Paths
    def test_reconcile_typical_transactions(self):
        transactions = [
            {"id": 1, "amount": 100.0, "timestamp": "2023-10-01T10:20:30", "type": "credit"},
            {"id": 2, "amount": 50.0, "timestamp": "2023-10-02T11:20:30", "type": "debit"},
            {"id": 3, "amount": 20.0, "timestamp": "2023-10-03T12:20:30", "type": "debit"}
        ]
        initial_balance = 150.0
        report = reconcile_transactions(transactions, initial_balance)
        self.assertEqual(report['final_balance'], 180.0)
        self.assertEqual(report['discrepancies'], [])
        self.assertEqual(report['overdraft_count'], 0)
        self.assertEqual(report['total_penalties'], 0.0)

    def test_reconcile_transactions_with_overdraft(self):
        transactions = [
            {"id": 1, "amount": 50.0, "timestamp": "2023-10-01T10:20:30", "type": "debit"},
            {"id": 2, "amount": 100.0, "timestamp": "2023-10-02T11:20:30", "type": "debit"}
        ]
        initial_balance = 80.0
        report = reconcile_transactions(transactions, initial_balance)
        self.assertEqual(report['final_balance'], -40.0)
        self.assertEqual(report['discrepancies'], [])
        self.assertEqual(report['overdraft_count'], 1)
        self.assertEqual(report['total_penalties'], 35.0)

    # Edge Cases
    def test_no_transactions(self):
        transactions = []
        initial_balance = 100.0
        report = reconcile_transactions(transactions, initial_balance)
        self.assertEqual(report['final_balance'], 100.0)
        self.assertEqual(report['discrepancies'], [])
        self.assertEqual(report['overdraft_count'], 0)
        self.assertEqual(report['total_penalties'], 0.0)

    def test_invalid_initial_balance(self):
        transactions = [{"id": 1, "amount": 50.0, "timestamp": "2023-10-01T10:20:30", "type": "debit"}]
        with self.assertRaises(ValueError):
            reconcile_transactions(transactions, -100.0)

    def test_invalid_transaction_amount(self):
        transactions = [{"id": 1, "amount": -50.0, "timestamp": "2023-10-01T10:20:30", "type": "debit"}]
        initial_balance = 100.0
        report = reconcile_transactions(transactions, initial_balance)
        self.assertEqual(len(report['discrepancies']), 1)
        self.assertEqual(report['discrepancies'][0]['reason'], "Invalid amount")

    def test_missing_transaction_fields(self):
        transactions = [{"id": 1, "amount": 50.0, "timestamp": "2023-10-01T10:20:30"}]  # Missing 'type'
        initial_balance = 100.0
        report = reconcile_transactions(transactions, initial_balance)
        self.assertEqual(len(report['discrepancies']), 1)
        self.assertEqual(report['discrepancies'][0]['reason'], "Missing required fields")

    def test_invalid_transaction_type(self):
        transactions = [{"id": 1, "amount": 50.0, "timestamp": "2023-10-01T10:20:30", "type": "withdraw"}]
        initial_balance = 100.0
        report = reconcile_transactions(transactions, initial_balance)
        self.assertEqual(len(report['discrepancies']), 1)
        self.assertEqual(report['discrepancies'][0]['reason'], "Invalid transaction type")

    def test_invalid_timestamp_format(self):
        transactions = [{"id": 1, "amount": 50.0, "timestamp": "2023-10-01 10:20:30", "type": "debit"}]
        initial_balance = 100.0
        report = reconcile_transactions(transactions, initial_balance)
        self.assertEqual(len(report['discrepancies']), 1)
        self.assertEqual(report['discrepancies'][0]['reason'], "Invalid timestamp format")

if __name__ == '__main__':
    unittest.main()