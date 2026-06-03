import pandas as pd
import numpy as np

def analyze_spinoff_research():
    print("=========================================================================")
    print("📈 EXCHANGES SPINOFF ANOMALY RESEARCH: THE 3-21 MONTH STRATEGY")
    print("=========================================================================\n")
    
    # Load primary data structures
    try:
        strategy_df = pd.read_csv('my_3_21_strategy_results.csv')
        yearly_df = pd.read_csv('my_3_21_yearly_breakdown.csv')
        cohort_df = pd.read_csv('my_pristine_cohort_results.csv')
        inst_df = pd.read_csv('my_precision_institutional_results.csv')
        master_df = pd.read_csv('spinoff_master_2015_2025.csv')
    except Exception as e:
        print(f"❌ File Load Error: Ensure all 5 CSV data files match exact names. Details: {e}")
        return

    # Process metrics
    returns = strategy_df['Return_Percent'].values
    total_trades = len(returns)
    
    gains = strategy_df[strategy_df['Return_Percent'] > 0]['Return_Percent'].values
    losses = strategy_df[strategy_df['Return_Percent'] <= 0]['Return_Percent'].values
    
    win_rate = (len(gains) / total_trades) * 100
    avg_return = np.mean(returns)
    median_return = np.median(returns)
    
    total_gains_pct = np.sum(gains)
    total_losses_pct = np.sum(losses)
    profit_factor = total_gains_pct / abs(total_losses_pct) if total_losses_pct != 0 else np.inf

    # Print Dashboard
    print(f"📊 DATA SELECTION & METRIC PROFILES:")
    print(f"   ▫️ Total Corporate Spinoff Events Parsed:    {len(master_df)}")
    print(f"   ▫️ Total Backtested Strategy Executions:    {total_trades}")
    print(f"   ▫️ Strategy Success Frequency (Win Rate):   {win_rate:.2f}%")
    print(f"   ▫️ Average Trade Outcome:                    {avg_return:.2f}%")
    print(f"   ▫️ Median Trade Outcome:                     {median_return:.2f}%")
    
    print("\n💰 PROFIT VS. LOSS RECONCILIATION:")
    print(f"   ▫️ Cumulative Strategy Positive Gains:      +{total_gains_pct:.2f}%")
    print(f"   ▫️ Cumulative Strategy Negative Losses:     {total_losses_pct:.2f}%")
    print(f"   ▫️ Gross Return Profit Factor:               {profit_factor:.2f}x (Gains/Losses)")
    
    print("\n🚀 PEAK OUTLIER MOMENTUM:")
    top_win = strategy_df.sort_values(by='Return_Percent', ascending=False).iloc[0]
    top_loss = strategy_df.sort_values(by='Return_Percent', ascending=True).iloc[0]
    print(f"   ▫️ Maximum Asymmetric Gain:  +{top_win['Return_Percent']:.2f}% ({top_win['Ticker']})")
    print(f"   ▫️ Maximum Downside Erosion: {top_loss['Return_Percent']:.2f}% ({top_loss['Ticker']})")
    
    print("\n🗓️ ANNUAL PERFORMANCE COHORTS:")
    for _, row in yearly_df.iterrows():
        print(f"   ▫️ Year {int(row['Calendar_Year'])} | Trades: {int(row['Total_Spinoffs_Traded'])} | Win Rate: {row['Win_Rate_Pct']:.1f}% | Avg Return: {row['Average_Return_Pct']:.2f}%")
    print("\n=========================================================================")

if __name__ == "__main__":
    analyze_spinoff_research()
