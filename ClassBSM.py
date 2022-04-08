# BS function
import math
from scipy.stats import norm


class BSM(object):

    def __init__(self, asset_price, exercise_price, annualized_remaining, annualized_sigma, rf_rate):
        """
        asset_price: self.S
        exercise_price: self.K
        annualized_remaining: self.T
        annualized_sigma: self.q
        rf_rate: self.r
        attr: self.d1, d2, CallPrice, PutPrice, CallDelta, PutDelta
        """
        self.S = asset_price
        self.K = exercise_price
        self.T = annualized_remaining
        self.q = annualized_sigma
        self.r = rf_rate
        self.d1 = (math.log(self.S / self.K) + (self.r + 0.5 * self.q * self.q) * self.T) / (
                self.q * math.sqrt(self.T))
        self.d2 = self.d1 - self.q * math.sqrt(self.T)
        self.CallPrice = norm.cdf(self.d1) * self.S - norm.cdf(self.d2) * self.K * math.exp(-self.r * self.T)
        self.PutPrice = self.K * math.exp(-self.r * self.T) - self.S + self.CallPrice
        self.CallDelta = norm.cdf(self.d1)
        self.PutDelta = norm.cdf(self.d1) - 1


if __name__ == '__main__':
    bsm = BSM(4815.226, 4500, 0.0877, 0.2643, 0.01)
    print(bsm.d1)
    print(bsm.d2)
    print(bsm.CallPrice)
    print(bsm.PutPrice)
    print(bsm.CallDelta)
    print(bsm.PutDelta)
