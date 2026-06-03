# Spinoff-Data-2.0

This repository contains the empirical backtesting data, data pipeline structures, and performance modeling for an independent quantitative research project exploring structural pricing anomalies in corporate demergers (spinoffs) from 2015 to 2025. This research was developed to evaluate whether a systematic time-delayed entry window eliminates market inefficiencies and produces asymmetric returns. I attemped to create a strategy based on data from the years 2015 to 2024 year end. I used https://stockanalysis.com for all the data I gathered. I created and used an algorithm to extract all 265 recorded historical coropoarte spinoff events across US equity exchanges into a .csv file. I used conditional formatting to filter the wins and losses of this strategy. Of course, it is important to note that there were a few very large outliers, in the case for the losses those outliers are capped at 100%. The file strategy_backtest.py shows there outliers from the largest win to the largest loss.

The project investigates whether newly independent corporate spinoffs suffer from short-term institutional selling pressure, followed by a long-term fundamental recovery. To evaluate this systematically, the 3-21 Month Strategy executes a strict rules-based timeline:

              Wait 90 Days           Hold 21 Months
(Spinoff Date)------------>(Buy Date)------------->(Sell Date)

Following the date of a corporate separation (Spinoff Date), the strategy blocks all capital deployments for exactly 90 days. This observation window tracks price discovery and lets any mandatory or forced index fund selling exhaust itself. The position is initiated at Day 90 (Buy Date) and held for exactly 21 months. It is liquidated on Day 730 (Sell Date)—exactly two years post-spinoff—to assess the ultimate ratio of absolute profits against absolute losses.

The research is driven by a data pipeline structured across 5 distinct files:

- spinoff_master_2015_2025.csv: The master registry containing 265 recorded historical corporate spinoff events across US equity exchanges.
- my_3_21_strategy_results.csv: The comprehensive trade ledger consisting of 171 unique spinoff historical transactions that met data completeness constraints to undergo the 3-21 timeline backtest.
- my_3_21_yearly_breakdown.csv: Annualized strategic performance tables tracks metrics across rolling macroeconomic environments.
- my_pristine_cohort_results.csv: Focused analytical research tracking sectoral variations between the child company sector and parent company sector.
- my_precision_institutional_results.csv: Reference database mapping company tickers directly to their unique SEC Central Index Key (CIK) identifiers for filing transparency.

Empirical Backtest Findings:
Analyzing the 171 backtested transactions from 2015 through 2024 reveals a distinct right-tail performance asymmetry, proving that a time-delayed holding strategy captures significant growth but remains exposed to downside risks.

Cumulative Profit vs. Loss Performance:
  The strategy successfully demonstrates that absolute profits significantly outpace absolute losses across the observed historical universe:
  - Total Completed Strategy Trades: 171
  - Strategy Win Rate: 55.56%
  - Average Return per Trade: +29.58%
  - Annualized return: +15.96%
  - Median Return per Trade: +11.23%
  - Cumulative Sum of Positive Returns: +8,188.23%
  - Cumulative Sum of Negative Returns: -3,129.74%
  - Gross Return Profit Factor: 2.62x  *The gross return profit factor is the ratio of the total sum of all positive gains divided by the absolute value of the total sum of all negative losses within a trading strategy.

Outliers:
  The strategy's return profile is heavily characterized by extreme positive asymmetric outliers, though it remains vulnerable to complete capital impairments when weak corporate divisions are loaded with debt:
  - Peak Positive Asymmetric Winner: INBX (Inhibrx Biosciences Inc.) ---> +611.25%
  - Peak Negative Asymmetric Loser: SVRN (Severn Bancorp) ---> -99.73%

Annual Performance breakdown
Year: 2015 | Total spinoffs traded: 19 | Win Rate(%): 79.95% | Average Return for Year(%): 73.56%
Year: 2016 | Total spinoffs traded: 13 | Win Rate(%): 76.92% | Average Return for Year(%): 54.67%
Year: 2017 | Total spinoffs traded: 20 | Win Rate(%): 45.00% | Average Return for Year(%): -5.32%
Year: 2018 | Total spinoffs traded: 12 | Win Rate(%): 25.00% | Average Return for Year(%): -15.01%
Year: 2019 | Total spinoffs traded: 16 | Win Rate(%): 68.75% | Average Return for Year(%): 34.35%
Year: 2020 | Total spinoffs traded: 16 | Win Rate(%): 43.75% | Average Return for Year(%): 2.77%
Year: 2021 | Total spinoffs traded: 16 | Win Rate(%): 50.00% | Average Return for Year(%): -7.86%
Year: 2022 | Total spinoffs traded: 20 | Win Rate(%): 30.00% | Average Return for Year(%): 0.21%
Year: 2023 | Total spinoffs traded: 30 | Win Rate(%): 60.00% | Average Return for Year(%): 49.87%
Year: 2024 | Total spinoffs traded: 9 | Win Rate(%): 88.89% | Average Return for Year(%): 140.91%

These findings are specifically for the 3-21 method, with complete disregard for any fundamental analysis. This ofcourse was not enough, however, I needed a way to narrow the list, so that the average return and win rate would increase. This repository contains the empirical data, programmatic filtering criteria, and performance results tracking a high-conviction subset of corporate demergers known as the Pristine Cohort. This research explores whether combining a systematic time-based timeline with strict structural regulatory filters can remove market noise, isolate pure-play operations, and improve overall portfolio win rates. Before applying advanced company filters, a baseline 3-21 Month Strategy was backtested across the broad market universe using a dataset of 171 unique historical spinoff transactions (`my_3_21_strategy_results.csv`). Under this unmanaged baseline approach, positions were initiated exactly 90 days (3 months) post-spinoff and held for exactly 21 months. This unmanaged broad-market execution yielded an overall strategy win rate of **55.56%** and generated a baseline sample average return of 29.58 per trade. While profitable, the baseline performance exhibited significant variance and left-tail volatility caused by weak corporate divisions acting as "liability dumps" for their parent companies.

Filter Methodology: Constructing the Pristine Cohort

To filter out low-quality listings and optimize performance, a strict secondary filtration pipeline was built to isolate the **Pristine Cohort** (`my_pristine_cohort_results.csv`). To graduate into this high-conviction list, a spinoff event had to pass two strict structural criteria:

1. The SEC CIK Audit Layer: Tickers were cross-referenced with official SEC Edgar filings using unique Central Index Key (CIK) identifiers (`my_precision_institutional_results.csv`) to verify institutional reporting completeness, ensuring data integrity and removing highly illiquid, unbacked penny stock anomalies.
2. The Industrial Sector Mismatch Screen:** Using sector classifications, the pipeline automatically flagged and removed any child company that matched the exact industrial sector of its parent organization. 
   * The Theory: If a parent and child company share a sector, the separation is frequently an accounting maneuver to offload corporate liabilities or legacy debt. 
   * The Target: A complete sector mismatch (e.g., a real estate child spun off from a consumer cyclical parent) identifies a true structural breakout designed to unlock hidden, independent operational value.

Empirical Results: Baseline vs. Pristine Cohort

Applying these filters condensed the broad testing pool down to an optimized group of 33 high-conviction transactions. The filtered performance data reveals a substantial improvement across all primary portfolio metrics:

### 1. Win-to-Loss Distribution
The sector mismatch screen successfully filtered out catastrophic downside events, resulting in a cleaner distribution of profitable outcomes:
* Total Isolated Pristine Trades: 33
* Successful Trades (Wins): 22
* Unsuccessful Trades (Losses): 11
* Optimized Strategy Win Rate: 66.67%(an 1,111 basis point increase over the baseline win rate of 55.56%).

### 2. Return Comparison Summary
Beyond increasing the mathematical probability of a winning trade, the Pristine Cohort generated a higher average return per position by effectively removing heavy downside outliers from the portfolio.

* Broad Market Baseline Average Return: +29.58%
* Pristine Cohort Average Return: +38.89%
* Annualized return using Pristine Cohort: +20.65%
By systematically applying programmatic sector filters, the final framework successfully captured an extra +9.31% of absolute alpha expansion per trade compared to blindly purchasing every spinoff in the broad asset universe.

Though these numbers may seem great at first, average returns can decline. According to the Pristine Cohort you are merely buying 33 companies across 9 years. Once you take profits, your cash may stay stagnant for months, which ulitmately decreases the value of the cash itself. The profits should be set in a highly liquid asset that keeps up with inflation in order to be reinvested into the investment plan, or the profits can be reallocated to a different stock one that is either a dominant growth company such as ASML or a dividend king company that pays stable income to shareholders such as Parker Hannifin.
