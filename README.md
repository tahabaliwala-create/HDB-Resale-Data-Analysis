# HDB Resale Price Analysis (2017 to 2025)

A data analysis project using **pandas**, **NumPy** and **matplotlib** on Singapore's public HDB resale flat transaction data.

## Question

> How have HDB resale prices changed across towns since 2017, and how much do flat type and remaining lease matter?

## Data

- **Source:** [Resale flat prices based on registration date from Jan-2017 onwards](https://data.gov.sg/datasets/d_8b84c4ee58e3cfc0ece0d773c8ca6abc/view) on data.gov.sg, published by HDB under the Singapore Open Data Licence.
- **Columns used:** month, town, flat_type, floor_area_sqm, lease_commence_date, remaining_lease, resale_price.

## Method

1. **Cleaning**
   - Removed a title row and blank rows left over from the spreadsheet export.
   - Converted `month` to a real date and extracted a `year` column.
   - Converted `resale_price` and `floor_area_sqm` to numbers.
   - Converted `remaining_lease` (text such as "61 years 04 months") into a number of years.
2. **New columns:** `price_per_sqm` (resale price divided by floor area) and `lease_era` (lease commencement year grouped by decade with `pd.cut`).
3. **Summaries:** average price by town, by year, and by flat type using `groupby`.
4. **Growth calculation:** for each group, average price per year, reshaped with `unstack`, then percentage growth between 2017 and 2025.
5. **Focused analysis:** 4 ROOM flats in Tampines, comparing price growth across lease eras, so flat type and town stay the same.

## Charts

Add your saved charts here, for example:

```
![Average price by flat type](charts/price_by_flat_type.png)
![Tampines 4 ROOM price by lease era](charts/tampines_lease_era.png)
```

## Findings

Fill these in with your own numbers after running the analysis.

- **Across time:** [e.g. average resale prices rose from S$X in 2017 to S$Y in 2025, a change of Z%.]
- **Across towns:** [e.g. the fastest-growing towns for 4 ROOM flats were ... and the slowest were ...]
- **Lease era (Tampines, 4 ROOM):** [e.g. flats with older leases grew X% compared with Y% for newer leases.]
- **Hypothesis:** [state what you expected, and whether the data supported it.]

## Limitations

- The lease era analysis covers one town and one flat type, so the results may not apply elsewhere.
- Some groups have few sales, which makes their averages less reliable.
- Prices are affected by many things not in this dataset, such as floor level, renovation condition and market cycles. The results show associations, not proof that lease length causes price changes.
- The 2017 to 2025 window is one choice of period, and other windows could give different results.

## How to run

```
pip install pandas numpy matplotlib
python main.py
```

Make sure `HDB_resale_price_data.csv` is in the same folder as `main.py`.

## Tools

Python, pandas, NumPy, matplotlib.
