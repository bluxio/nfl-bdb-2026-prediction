from dataclasses import dataclass
from typing import Tuple, List
import pandas as pd
import numpy as np
from .metrics import rmse_xy

@dataclass
class SplitConfig:
    time_col: str = "game_date"
    holdout_weeks: int = 2

def time_based_split(df: pd.DataFrame, cfg: SplitConfig):
    df = df.copy()
    df[cfg.time_col] = pd.to_datetime(df[cfg.time_col])
    last_date = df[cfg.time_col].max()
    cutoff = last_date - pd.to_timedelta(cfg.holdout_weeks*7, unit='D')
    return df[df[cfg.time_col] <= cutoff], df[df[cfg.time_col] > cutoff]

def evaluate_rmse(pred_df: pd.DataFrame, true_df: pd.DataFrame) -> float:
    # pred_df,true_df: columns [game_id, play_id, nfl_id, frame_id, x, y]
    merged = true_df.merge(pred_df, on=["game_id","play_id","nfl_id","frame_id"], suffixes=("_true","_pred"))
    pred = merged[["x_pred","y_pred"]].to_numpy()
    true = merged[["x_true","y_true"]].to_numpy()
    return rmse_xy(pred, true)
