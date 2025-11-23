import pandas as pd
def test_load_news():
    df = pd.read_csv('raw_analyst_ratings.csv')  # Your news CSV
    assert len(df) > 1000000, "News dataset too small for EDA"
    print(f"Pass: Loaded {len(df)} rows – Ready for Task 1 EDA")
test_load_news()