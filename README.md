# ClassBSM
Python Class for BSM function

Example:

if __name__ == '__main__':
    bsm = BSM(asset_price=4815.226, exercise_price=4500, remaining=0.0877, sigma=0.2643, rf_rate=0.01)
    print(bsm.d1)
    print(bsm.d2)
    print(bsm.CallPrice)
    print(bsm.PutPrice)
    print(bsm.CallDelta)
    print(bsm.PutDelta)
