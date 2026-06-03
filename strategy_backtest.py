import pandas as pd
import numpy as np

def run_portfolio_analysis():
    print("=========================================================================")
    print("🧮 SYSTEMATIC SPINOFF ARBITRAGE: PORTFOLIO BACKTEST ENGINE")
    print("=========================================================================\n")
    
    # 1. Load the underlying data structures
    try:
        strategy_results = pd.read_csv('my_3_21_strategy_results.csv')
        yearly_breakdown = pd.read_csv('my_3_21_yearly_breakdown.csv')
    except Exception as e:
        print(f"❌ Initialization Error: Ensure the CSV files exist in the directory. Details: {e}")
        return

    # 2. Extract baseline parameters
    raw_returns = strategy_results['Return_Percent'].values
    total_trades = len(raw_returns)
    
    raw_mean = np.mean(raw_returns)
    raw_std = np.std(raw_returns)
    raw_sum = np.sum(raw_returns)
    
    # 3. Apply the Risk Mitigation Optimization (-25% Left-Tail Truncation)
    # This simulates a programmatic stop-loss executing at the purchase boundary
    shielded_returns = np.where(raw_returns < -25.0, -25.0, raw_returns)
    
    shielded_mean = np.mean(shielded_returns)
    shielded_std = np.std(shielded_returns)
    shielded_sum = np.sum(shielded_returns)
    
    # 4. Generate Performance Matrix
    print("📊 METRIC ANALYSIS PANEL:")
    print(f"   ▫️ Total Spinoff Transactions Audited: {total_trades}")
    print(f"   ▫️ Baseline Performance Sample Mean:   {raw_mean:.2f}%")
    print(f"   ▫️ Baseline Performance Volatility:    {raw_std:.2f}%")
    print(f"   ▫️ Optimized Performance Sample Mean:  {shielded_mean:.2f}%  📈 (+{(shielded_mean - raw_mean)*100:.0f} bps alpha expansion)")
    print(f"   ▫️ Optimized Performance Volatility:   {shielded_std:.2f}%  📉 (Volatility Truncated)")
    
    print("\n📦 CUMULATIVE STRATEGY ARBITRAGE OUTPUT:")
    print(f"   ▫️ Aggregate Unmanaged Absolute Return: {raw_sum:.2f}%")
    print(f"   ▫️ Aggregate Risk-Managed Absolute Return: {shielded_sum:.2f}%")
    
    # 5. Extract Historical Outliers
    print("\n🚀 RIGHT-TAIL ASYMMETRIC DRIVERS (TOP WINNERS):")
    top_winners = strategy_results.sort_values(by='Return_Percent', ascending=False).head(3)
    for idx, row in top_winners.iterrows():
        print(f"   ▫️ Ticker: {row['Ticker']} | Spinoff Date: {row['Spinoff_Date']} | Absolute Return: +{row['Return_Percent']:.2f}%")
        
    print("\n🚨 UNMANAGED LEFT-TAIL VALUE DESTROYERS (TOP CRATERS):")
    top_losers = strategy_results.sort_values(by='Return_Percent', ascending=True).head(3)
    for idx, row in top_losers.iterrows():
        print(f"   ▫️ Ticker: {row['Ticker']} | Spinoff Date: {row['Spinoff_Date']} | Absolute Return: {row['Return_Percent']:.2f}%")
    print("\n=========================================================================")

if __name__ == "__main__":
    run_portfolio_analysis()
