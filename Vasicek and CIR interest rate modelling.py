# Stochastic Interest Rate Modelling
print("Stochastic Interest Rate Modelling")
print("1.Vasicek Interest Rate Modelling")
print("2.Cox Ingersoll Ross (CIR) Interest Rate Modelling")
Choice = int(input("Enter Choice:"))
print("List out all the Parameters")
r0 = float(input("Enter current interest rate r0: "))

a = float(input("Enter speed of mean reversion a: "))

b = float(input("Enter Long Tearm Mean of R:"))

sigma = float(input(("Enter volatility:")))

T = int(input(("Enter number of years:")))

N = 252 * T

print(N,"is the trading days !")

n_sims = int(input(("Enter number of simulations:")))  # number of simulations

print(n_sims, "number of simulations:")

dt = T / N

print(" TIME STEP (dt) is", dt)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
r=np.zeros((N+1,n_sims))
r[0,:]=r0

for t in range(N):
    z = np.random.normal(0,1,n_sims)
    if Choice==1:
        # Vasicek: dr = a(b - r)dt + sigma *dW
        r[t+1,:]= r[t,:] + a * (b - r[t,:]) * dt + sigma*np.sqrt(dt)*z
    else:
        # CIR: dr = a(b - r)dt + sigma sqrt(r) dW
        r_pos = np.maximum(r[t, :], 0)
        r[t + 1, :] = (r[t, :]+ a * (b - r[t, :]) * dt+ sigma * np.sqrt(r_pos) * np.sqrt(dt) * z)
        r[t + 1, :] = np.maximum(r[t + 1, :], 0)

#PLOT
Time= np.linspace(0,T,N+1)
plt.plot(Time,r)
plt.axhline(b, color="black", linestyle="--", label="Long-term mean")

plt.xlabel("Time")
plt.ylabel("Interest Rate")
if Choice == 1 :
    plt.title("Vasicek Interest Rate Modelling ")
else:
    plt.title("Cox Ingersoll Ross Model")
plt.legend()                            
plt.show()
