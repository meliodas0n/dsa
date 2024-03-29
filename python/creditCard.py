class CreditCard:
  def __init__(self, customer, bank, acnt, limit):
    self._customer = customer
    self._bank = bank
    self._account = acnt
    self._limit = limit
    self._balance = 0
  
  def get_customer(self):
    return self._customer

  def get_bank(self):
    return self._bank

  def get_account(self):
    return self._bank

  def get_limit(self):
    return self._limit

  def get_balance(self):
    return self._balance

  def charge(self, price):
    if price + self._balance > self._limit: return False
    else: self._balance += price; return True
  
  def make_payment(self, amount):
    self._balance -= amount

if __name__ == "__main__":
  wallet = []
  wallet.append(CreditCard('John Bowman', 'California Savings', '5391 0375 9387 5309', 2500))
  wallet.append(CreditCard('John Bowman', 'California Federal', '5391 0375 9387 5309', 3500))
  wallet.append(CreditCard('John Bowman', 'California Finance', '5391 0375 9387 5309', 5500))

  for val in range(1, 17):
    wallet[0].charge(val)
    wallet[1].charge(2 * val)
    wallet[2].charge(3 * val)

  for c in range(3):
    print(f'Customer = {wallet[c].get_customer()}')
    print(f'Bank = {wallet[c].get_bank()}')
    print(f'Acount = {wallet[c].get_account()}')
    print(f'Limit = {wallet[c].get_limit()}')
    print(f'Balance = {wallet[c].get_balance()}')
    while wallet[c].get_balance() > 100:
      wallet[c].make_payment(100)
      print(f'New balance = {wallet[c].get_balance()}')
    print()
