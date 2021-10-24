import unittest
import math
from src.dto.entities.loan import Loan
from src.dto.entities.payment import Payment

class Testmain(unittest.TestCase):
    # more tests to be added

    def test_loan(self):
        p,t,r = 10000,4,10
        myloan = Loan(p,t,r)
        _,emisLeft = myloan.getBalance(0)
        ground_truth = self.groundTruthEmisLeft(p,t,r)
        self.assertEqual(emisLeft,ground_truth)

    def test_paymentBalance1(self):
        p,t,r = 10000,4,10
        myloan = Loan(p,t,r)
        payment_1 = Payment(1000)
        myloan.addPayment(payment_1.getPaymentID(),1000,10)
        amount_repaid,emisLeft = myloan.getBalance(15)
        self.assertEqual([5380,30],[amount_repaid,emisLeft])

    def test_paymentBalance2(self):
        p, t, r = 10000, 4, 10
        myloan = Loan(p, t, r)
        payment_1 = Payment(1000)
        myloan.addPayment(payment_1.getPaymentID(), 1000, 50)
        amount_repaid, emisLeft = myloan.getBalance(15)
        self.assertEqual([4380,33],[amount_repaid,emisLeft])

    def test_paymentBalance3(self):
        p, t, r = 10000, 4, 10
        myloan = Loan(p, t, r)
        payment_1 = Payment(10000)
        myloan.addPayment(payment_1.getPaymentID(), 10000, 4)
        tup1 = myloan.getBalance(15)
        tup2 = myloan.getBalance(14)
        self.assertEqual(tup1,tup2)

    def test_balance(self):
        p, t, r = 10000, 4, 10
        myloan = Loan(p, t, r)
        amount_repaid, emisLeft = myloan.getBalance(60)
        self.assertEqual([14016,0],[amount_repaid,emisLeft])

    def groundTruthEmisLeft(self,p,t,r):
        maturity_amount = math.ceil(p * (1 + (r * t) / 100))
        emi_val = math.ceil(maturity_amount / (t * 12))
        ground_truth = math.ceil(maturity_amount / emi_val)
        return ground_truth

if __name__ == '__main__':
    unittest.main()