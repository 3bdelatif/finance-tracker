

from finance_tracker.models.wallet import *
from finance_tracker.utils.file_manager import FileManager


class CLI:
    def __init__(self,owner):
        self.wallet= Wallet(owner,[])
        self.FileManager=FileManager()
    def run(self):
        while True:
            print("=== Personal Finance Tracker ===")
            print("1. Add income")
            print("2. Add expense")
            print("3. View balance")
            print("4. View statistics")
            print("5. View by category")
            print("6. Monthly report")
            print("7. Save")
            print("8. Load")
            print("9. Exit")
            choise = input("Enter your choice: ")
            match choise:
                case "1":
                    amount = int(input("Enter your amount: "))
                    category = input("Enter your category: ")
                    description=input("Enter your description: ")
                    self.wallet.add_income(amount,category,description)
                case "2":
                    amount = int(input("Enter your amount: "))
                    category = input("Enter your category: ")
                    description=input("Enter your description: ")
                    self.wallet.add_expense(amount,category,description)
                case "3":
                    print(self.wallet.get_total())
                case "4":
                    self.wallet.get_static()
                case "5":
                    category = input("Enter your category: ")
                    self.wallet.get_by_category(category)
                case "6":
                    mounth_t=input("Enter your mounth: ")
                    self.wallet.get_mountly_static(mounth_t)
                case "7":
                    self.FileManager.save(self.wallet,"txt.txt")
                    print("save done")
                case "8":
                    self.wallet= self.FileManager.load("txt.txt")
                    print("load done")
                case "9":
                    exit(0)



