import argparse
import sys
import pandas as pd

def validate(df: pd.DataFrame):
    required = ['id','x','y']
    if any(c not in df.columns for c in required):
        missing = [c for c in required if c not in df.columns]
        raise ValueError(f"Missing required columns: {missing}")
    if df[['x','y']].isnull().any().any():
        raise ValueError("Found NaNs in x/y.")
    # Basic schema check for id segments
    parts = df['id'].astype(str).str.split('_')
    bad = parts.map(len).ne(4).sum()
    if bad:
        raise ValueError(f"{bad} rows have malformed id (expected 4 segments)")
    print("Looks good: submission format passes basic checks.")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--path', default=None, help='Path to submission.csv')
    ap.add_argument('--fake', action='store_true', help='Generate fake submission and validate it')
    args = ap.parse_args()

    if args.fake:
        df = pd.DataFrame({'id':['1_1_1_1','1_1_2_1'], 'x':[50.0, 30.0], 'y':[20.0, 15.0]})
        validate(df)
        return

    if not args.path:
        print("Usage: python -m tools.check_submission --path submission.csv", file=sys.stderr)
        sys.exit(2)

    df = pd.read_csv(args.path)
    validate(df)

if __name__ == '__main__':
    main()
