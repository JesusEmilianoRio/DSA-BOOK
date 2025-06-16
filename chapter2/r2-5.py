"""
Use the techniques of Section 1.7 to revise the charge and make payment
 methods of the CreditCard class to ensure that the caller sends a number
 as a parameter.

If the parameter to the make payment method of the CreditCard class
 were a negative number, that would have the effect of raising the balance
 on the account. Revise the implementation so that it raises a ValueError if
 a negative value is sent.

 The CreditCard class of Section 2.3 initializes the balance of a new ac
count to zero. Modify that class so that a new account can be given a
 nonzero balance using an optional fifth parameter to the constructor. The
 four-parameter constructor syntax should continue to produce an account
 with zero balance.


"""
class CreditCard:
    """A consumer credit card."""
    def __init__(self, customer, bank, acnt, limit, balance = 0):
        """
            Createanewcreditcardinstance.

            Theinitialbalanceiszero.
 
            customer thenameof thecustomer(e.g., JohnBowman)
            bank thenameof thebank(e.g., CaliforniaSavings)
            acnt theacount identifier(e.g., 5391037593875309)
            limit credit limit(measuredindollars)
        """
        self._customer = customer
        self._bank = bank
        self._acnt = acnt
        self._limit = limit
        self._balance = balance

    def charge(self, price):
        try:
            if not isinstance(price, (int, float)):
                raise TypeError("Insert numbers")

            if price + self._balance > self._limit:
                return False
            else:
                self._balance += price
                return True
        except TypeError as e:
            print("Error: ", e)

    def make_payment(self, amount):
        try:
            if not isinstance(amount, (int, float)):
                raise TypeError("Insert numbers.")
            self._balance -= amount
        except TypeError as e:
            print("Error: ", e)
