# BSM Solver including Greeks, using the Newton-Raphson iterative algorithm
import math
from scipy.stats import norm


class bsm_solver(object):

    def __init__(self, asset_price, exercise_price, remaining, call_put=1, sigma=0.5, rf_rate=0.1):
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
        self.T = remaining
        self.q = sigma
        self.r = rf_rate
        self.call_put = call_put
        self.d1 = (math.log(self.S / self.K) + (self.r + 0.5 * self.q * self.q) * self.T) / (
                self.q * math.sqrt(self.T))
        self.d2 = self.d1 - self.q * math.sqrt(self.T)
        self.Gamma = norm.pdf(self.d1) / (self.S * self.q * math.sqrt(self.T))
        self.Vega = self.S * norm.pdf(self.d1) * math.sqrt(self.T)

        if call_put == 1:
            self.Price = norm.cdf(self.d1) * self.S - norm.cdf(self.d2) * self.K * math.exp(-self.r * self.T)
            self.Delta = norm.cdf(self.d1)
            self.Theta = -1 * (self.S * norm.pdf(self.d1) * self.q) / (
                2 * math.sqrt(self.T)) - self.r * self.K * math.exp(-self.r * self.T) * norm.cdf(self.d2)
            self.Rho = self.T * self.K * math.exp(-self.r * self.T) * norm.cdf(self.d2)
        else:
            self.Price = self.K * math.exp(-self.r * self.T) - self.S + norm.cdf(self.d1) * self.S \
                         - norm.cdf(self.d2) * self.K * math.exp(-self.r * self.T)
            self.Delta = norm.cdf(self.d1) - 1
            self.Theta = -1 * (self.S * norm.pdf(self.d1) * self.q) / (
                2 * math.sqrt(self.T)) + self.r * self.K * math.exp(-self.r * self.T) * norm.cdf(-1 * self.d2)
            self.Rho = -1 * self.T * self.K * math.exp(-self.r * self.T) * norm.cdf(-1 * self.d2)

    def vol(self, target_price, max_iterations=500, precision=1.0e-5):
        q = 0.5
        call_put = self.call_put
        for i in range(0, max_iterations):
            d1 = (math.log(self.S / self.K) + (self.r + 0.5 * q * q) * self.T) / (q * math.sqrt(self.T))
            d2 = d1 - q * math.sqrt(self.T)
            vega = self.S * norm.pdf(d1) * math.sqrt(self.T)
            if call_put == 'C':
                price = norm.cdf(d1) * self.S - norm.cdf(d2) * self.K * math.exp(-self.r * self.T)
            else:
                price = self.K * math.exp(-self.r * self.T) - self.S + norm.cdf(d1) * self.S \
                        - norm.cdf(d2) * self.K * math.exp(-self.r * self.T)
            diff = target_price - price
            if abs(diff) < precision:
                return q
            q = q + diff / vega  # f(x) / f'(x)
        return q


if __name__ == '__main__':
    bsm = bsm_solver(asset_price=4815.226, exercise_price=4500, remaining=0.0877, call_put='C', sigma=0.2643, rf_rate=0)
    print(bsm.d1)
    print(bsm.d2)
    print(bsm.Price)
    print(bsm.Delta)
    print(bsm.Gamma)
    print(bsm.Theta)
    print(bsm.Vega)
    print(bsm.Rho)
    print(bsm.vol(target_price=354.205))
    print(BSM(asset_price=4815.226, exercise_price=4500, remaining=0.0877, call_put=1, rf_rate=0).vol(target_price=354.205))
