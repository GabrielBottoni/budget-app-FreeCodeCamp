class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({
            "amount": amount,
            "description": description
        })

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({
                "amount": -amount,
                "description": description
            })
            return True
        return False

    def get_balance(self):
        balance = 0

        for item in self.ledger:
            balance += item["amount"]

        return balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True

        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        result = self.name.center(30, "*") + "\n"

        for item in self.ledger:
            description = item["description"][:23]
            amount = f"{item['amount']:.2f}"

            result += description.ljust(23) + amount.rjust(7) + "\n"

        result += f"Total: {self.get_balance():.2f}"

        return result


def create_spend_chart(categories):
    result = "Percentage spent by category\n"

    # Calcula o total gasto em todas as categorias
    total_spent = 0

    for category in categories:
        for item in category.ledger:
            if item["amount"] < 0:
                total_spent += abs(item["amount"])

    # Calcula a porcentagem de cada categoria
    percentages = []

    for category in categories:
        spent = 0

        for item in category.ledger:
            if item["amount"] < 0:
                spent += abs(item["amount"])

        percentage = int((spent / total_spent) * 100)
        percentage = percentage // 10 * 10

        percentages.append(percentage)

    # Cria as barras de 100 até 0
    for level in range(100, -1, -10):
        result += str(level).rjust(3) + "|"

        for percentage in percentages:
            if percentage >= level:
                result += " o "
            else:
                result += "   "

        result += " \n"

    # Linha horizontal
    result += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Nomes das categorias na vertical
    max_length = max(len(category.name) for category in categories)

    for i in range(max_length):
        result += "     "

        for category in categories:
            if i < len(category.name):
                result += category.name[i] + "  "
            else:
                result += "   "

        if i < max_length - 1:
            result += "\n"

    return result