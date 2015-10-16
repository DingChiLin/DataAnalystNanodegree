import numpy as np
import statsmodels.api as sm

Y = [1,4,2,6]
X = [[1,5],[4,2],[6,3],[8,9]]
X = sm.add_constant(X)
model = sm.OLS(Y,X)
results = model.fit()

print results.summary()
print results.params
print results.tvalues
