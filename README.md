# Vasicek-and-CIR-interest-rate-modelling
STOCHASTIC INTEREST RATE MODELLING
=================================

Project overview
----------------
This Python project simulates interest-rate paths using two stochastic
interest-rate models:

1. Vasicek model
2. Cox-Ingersoll-Ross (CIR) model

The program asks the user to choose a model, enter the model parameters,
choose the number of years to simulate, and specify the number of simulations.
It then plots the simulated interest-rate paths and shows the long-term mean.

Project Objectives
- Introduce stochastic short-rate modelling.
- Implement two classical mean-reverting interest-rate models.
- Use the Euler–Maruyama method to discretise stochastic differential equations.
- Generate multiple Monte Carlo paths.
- Compare constant volatility (Vasicek) with rate-dependent volatility (CIR).
- Visualise simulated rates and their long-term mean.
- Establish a foundation for future fixed-income and quantitative risk projects

Models
------
Vasicek model:
    dr = a(b - r)dt + sigma dW

Cox-Ingersoll-Ross (CIR) model:
    dr = a(b - r)dt + sigma sqrt(r)dW

The program uses an Euler-style discretisation with 252 time steps per year.
For the CIR model, negative rates are floored at zero after each simulated
step. This is a simple numerical approximation, not an exact simulation.

Requirements
------------
- Python 3
- NumPy
- Pandas
- Matplotlib

Note: Pandas is imported by the current script but is not currently used
in the simulation.

Installation
------------
1. Install Python 3 from https://www.python.org/downloads/ if it is not
   already installed.
2. Open Command Prompt or a terminal in the project folder.
3. Install the required libraries:

       python -m pip install numpy pandas matplotlib

If your computer uses the Python launcher on Windows, this can also work:

       py -m pip install numpy pandas matplotlib

How to run
----------
Run the script from a terminal:

    python "Vasicek and CIR interest rate modelling.py"

On Windows, you can also open the file in IDLE and press F5.

Inputs
------
- Model choice: enter 1 for Vasicek or 2 for CIR.
- Current interest rate (r0): the starting rate.
- Speed of mean reversion (a): how quickly the rate is pulled toward its
  long-term mean.
- Long-term mean (b): the level toward which the rate tends to revert.
- Volatility (sigma): controls the randomness of the simulated paths.
- Number of years (T): simulation horizon in years.
- Number of simulations: number of paths to generate and plot.

Example inputs
--------------
Model choice: 1
Current interest rate r0: 0.04
Speed of mean reversion a: 0.5
Long-term mean b: 0.1
Volatility sigma: 0.01
Number of years: 10
Number of simulations: 10

Rates are entered as decimals. For example, 0.04 represents 4%.

Output
------
A chart showing simulated interest-rate paths over time, with a dashed
horizontal line representing the long-term mean.

Repository structure
--------------------
Vasicek-CIR-Interest-Rate-Modelling/
|-- Vasicek and CIR interest rate modelling.py
|-- README.txt

Limitations and possible improvements
-------------------------------------
- The program currently does not validate user inputs.
- Any model choice other than 1 follows the CIR branch; use 1 or 2.
- The CIR implementation floors negative rates at zero, but this simple
  discretisation does not guarantee all theoretical properties of the CIR
  process.
- Pandas is imported but is not used yet.
- Possible extensions include parameter validation, saving simulated data,
  summary statistics, confidence intervals, and comparing both models on
  the same chart.

Disclaimer
----------
This project is for educational and research practice. It is not investment
advice and should not be used on its own for pricing or risk-management
decisions.

Author
------
Pratik Patil
