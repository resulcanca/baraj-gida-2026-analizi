# 2026 Dam Crisis vs Food Inflation - Turkey
Does drought hit grocery prices and how fast? I joined Istanbul dam levels with food inflation.
## What I did
- Pulled dam levels from ISKI and food CPI from CBRT EVDS.
- Aggregated to monthly and checked lagged correlation (-0.84 with 1-month lag).
## Run
pip install -r requirements.txt
python src/main.py
python src/analysis.py
