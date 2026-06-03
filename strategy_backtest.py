import pandas as pd
import numpy as np

def analyze_spinoff_research():
    print("=========================================================================")
    print("📈 SPINOFF DATA 2.0: THE 3-21 STRATEGY & PRISTINE COHORT RECONCILIATION")
    print("=========================================================================\n")
    
    # Load primary data structures
    try:
        strategy_df = pd.read_csv('my_3_21_strategy_results.csv')
        yearly_df = pd.read_csv('my_3_21_yearly_breakdown.csv')
        cohort_df = pd.read_csv('my_pristine_cohort_results.csv')
        master_df = pd.read_csv('spinoff_master_2015_2025.csv')
    except Exception as e:
        print(f"❌ File Load Error: Ensure all CSV files match exact filenames. Details: {e}")
        return

    # 1. Process 3-21 Broad Market Baseline Method Metrics
    base_returns = strategy_df['Return_Percent'].values
    total_base_trades = len(base_returns)
    base_gains = strategy_df[strategy_df['Return_Percent'] > 0]['Return_Percent'].values
    base_losses = strategy_df[strategy_df['Return_Percent'] <= 0]['Return_Percent'].values
    
    base_win_rate = (len(base_gains) / total_base_trades) * 100
    base_avg_return = np.mean(base_returns)
    base_median_return = np.median(base_returns)
    
    # Calculate exact annualized return based on a 21-month holding period (1.75 years)
    base_annualized = ((1 + base_avg_return / 100) ** (1 / 1.75) - 1) * 100
    
    total_gains_pct = np.sum(base_gains)
    total_losses_pct = np.sum(base_losses)
    profit_factor = total_gains_pct / abs(total_losses_pct) if total_losses_pct != 0 else np.inf

    # 2. Process Filtered Pristine Cohort Metrics
    pristine_returns = cohort_df['Return_Percent'].values
    total_pristine_trades = len(pristine_returns)
    pristine_gains = cohort_df[cohort_df['Return_Percent'] > 0]['Return_Percent'].values
    
    pristine_win_rate = (len(pristine_gains) / total_pristine_trades) * 100
    pristine_avg_return = np.mean(pristine_returns)
    
    # Calculate exact annualized return for the Pristine Cohort over 21 months
    pristine_annualized = ((1 + pristine_avg_return / 100) ** (1 / 1.75) - 1) * 100
    alpha_expansion = pristine_avg_return - base_avg_return

    # --- Print Dashboard Outputs ---
    
    print(f"📊 DATA SELECTION & EXTRACTION SUMMARY:")
    print(f"   ▫️ Total Spinoff Events Extracted (Master Registry):  {len(master_df)}")
    print(f"   ▫️ Total Base Strategy Executions Tested (3-21):     {total_base_trades}")
    print(f"   ▫️ Baseline Strategy Win Rate:                        {base_win_rate:.2f}%")
    print(f"   ▫️ Baseline Average Return per Trade:                  +{base_avg_return:.2f}%")
    print(f"   ▫️ Baseline Annualized Return Rate:                   +{base_annualized:.2f}%")
    print(f"   ▫️ Baseline Median Return per Trade:                  +{base_median_return:.2f}%")
    print(f"   ▫️ Cumulative Sum of Positive Returns (Gains):         +{total_gains_pct:.2f}%")
    print(f"   ▫️ Cumulative Sum of Negative Returns (Losses):        {total_losses_pct:.2f}%")
    print(f"   ▫️ Gross Return Profit Factor:                    {profit_factor:.2f}x (Gains/Losses)")
    
    print("\n💎 CORE FILTER UPGRADE: THE PRISTINE COHORT")
    print("   (Programmatic screen filtering for parent-child Sector Mismatch)")
    print(f"   ▫️ High-Conviction Pristine Trades Isolated:       {total_pristine_trades} positions across 9 years")
    print(f"   ▫️ Successful Pristine Trades (Wins):               {len(pristine_gains)}")
    print(f"   ▫️ Unsuccessful Pristine Trades (Losses):           {total_pristine_trades - len(pristine_gains)}")
    print(f"   ▫️ Pristine Cohort Optimized Win Rate:             {pristine_win_rate:.2f}%")
    print(f"   ▫️ Pristine Cohort Average Return per Trade:       +{pristine_avg_return:.2f}%")
    print(f"   ▫️ Pristine Cohort Annualized Return Rate:         +{pristine_annualized:.2f}%")
    print(f"   ▫️ Net Strategy Alpha Expansion Captured:          +{alpha_expansion:.2f}% absolute expansion")
    
    print("\n🏛️ CAPITAL ALLOCATION ENGINE TARGETS (Mitigating Stagnant Cash Drag):")
    print("   ▫️ Operational Drawback Identified: Stagnant cash risk over 9-year cycle")
    print("   ▫️ High-Liquidity Staging Pool Target: Recycle principal into inflation-shielded, liquid assets.")
    print("   ▫️ Permanent Core Reallocation Outlets for Harvested Alpha:")
    print("     1. Secular Growth Core: Sweep realized gains into dominant companies (e.g., ASML)")
    print("     2. Equity Stability Core: Sweep realized gains into Dividend Kings (e.g., Parker Hannifin [PH])")
    
    print("\n🚀 PEAK BASELINE OUTLIERS:")
    top_win = strategy_df.sort_values(by='Return_Percent', ascending=False).iloc[0]
    top_loss = strategy_df.sort_values(by='Return_Percent', ascending=True).iloc[0]
    print(f"   ▫️ Maximum Asymmetric Gain:  +{top_win['Return_Percent']:.2f}% ({top_win['Ticker']})")
    print(f"   ▫️ Maximum Downside Erosion: {top_loss['Return_Percent']:.2f}% ({top_loss['Ticker']})")
    
    print("\n🗓️ ANNUAL TIMELINE BREAKDOWN (3-21 BASELINE COHORTS):")
    for _, row in yearly_df.iterrows():
        print(f"   ▫️ Year {int(row['Calendar_Year'])} | Spinoffs: {int(row['Total_Spinoffs_Traded'])} | Win Rate: {row['Win_Rate_Pct']:.2f}% | Avg Return: {row['Average_Return_Pct']:.2f}%")
    print("\n=========================================================================")

if __name__ == "__main__":
    analyze_spinoff_research()
