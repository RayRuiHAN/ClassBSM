# ClassBSM

**!!Updated as "BSMSolver"!! This version should not be used**

Python Class for BSM function

Example:
```python
if __name__ == '__main__':
    bsm = BSM(asset_price=4815.226, exercise_price=4500, remaining=0.0877, call_put='C', sigma=0.2643, rf_rate=0)
    print(bsm.d1)
    print(bsm.d2)
    print(bsm.Price)
    print(bsm.Delta)
    print(bsm.Gamma)
    print(bsm.Theta)
    print(bsm.Vega)
    print(bsm.Rho)
    print(bsm.vol(target_price=354.205))
    print(BSM(asset_price=4815.226, exercise_price=4500, remaining=0.0877, rf_rate=0).vol(target_price=354.205))
 ```
