# Example wiring (no real data). Replace TODOs with real Kaggle inputs.
import pandas as pd
from pathlib import Path
from typing import List
from src.cv_baseline import estimate_velocity, predict_cv, predict_b1_interaction
from src.geometry import DT

def build_submission() -> pd.DataFrame:
    # TODO: Load test tracking and labels per competition schema
    # Here we mock a tiny example with one play, two players, 10 frames
    rows = []
    game_id, play_id = 1, 1
    nfl_ids = [101, 202]
    frame_ids = list(range(1, 11))
    T = len(frame_ids) * DT
    start = {101:(50.0, 25.0), 202:(48.0, 27.0)}
    vel = {k:(1.0, 0.0) for k in nfl_ids}
    for nfl_id in nfl_ids:
        traj = predict_cv(start[nfl_id][0], start[nfl_id][1], vel[nfl_id][0], vel[nfl_id][1], T)
        for j, (x,y) in enumerate(traj, start=1):
            rid = f"{game_id}_{play_id}_{nfl_id}_{j}"
            rows.append((rid, float(x), float(y)))
    df = pd.DataFrame(rows, columns=['id','x','y'])
    return df

if __name__ == '__main__':
    out = Path('submission.csv')
    df = build_submission()
    df.to_csv(out, index=False)
    print(f"Wrote {out} with {len(df)} rows.")
