# \# VaR/ES Engine with Back-testing

# 

# Computes 1-day Value-at-Risk and Expected Shortfall (95% / 99%) for a

# multi-asset portfolio using three methods — Historical Simulation,

# Parametric (variance-covariance + EWMA), and Monte-Carlo — and validates

# each model with Kupiec POF tests and the Basel traffic-light framework.

# 

# \## Status

# 🚧 In progress — Phase 1 (data + portfolio construction)

# 

# \## Planned structure

# \- `src/data\_loader.py` — price download and cleaning

# \- `src/returns.py` — log returns, portfolio P\&L

# \- `src/var\_historical.py` — historical simulation VaR

# \- `src/var\_parametric.py` — variance-covariance \& EWMA VaR

# \- `src/var\_montecarlo.py` — Cholesky-based MC simulation

# \- `src/es.py` — Expected Shortfall

# \- `src/backtesting.py` — Kupiec POF, Basel traffic-light

# 

# \## Results

# (to be added)

