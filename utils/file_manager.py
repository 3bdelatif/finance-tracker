import json


from finance_tracker.models.transaction import Transaction
from finance_tracker.models.wallet import Wallet


class FileManager:
    @staticmethod
    def save(wallet,filename):
        data = {
            'owner': wallet.owner,
            'transactions': [t.to_dict() for t in wallet.transactions]
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
    @staticmethod
    def load(filename):
        with open(filename, 'r') as f:
            data = json.load(f)

        wallet = Wallet(data['owner'], [])
        for t in data['transactions']:
            wallet.transactions.append(Transaction.from_dict(t))