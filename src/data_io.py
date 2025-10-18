from dataclasses import dataclass
from typing import Iterable, Tuple, Dict, Any, List, Optional
import pandas as pd

@dataclass
class Paths:
    train_tracking: str
    train_labels: str
    test_tracking: str

def load_tracking(path: str) -> pd.DataFrame:
    """Load tracking CSV.
    Expected columns (example): game_id, play_id, frame_id, nfl_id, x, y, team, is_target, is_offense
    The actual competition schema may differ; adapt as needed.
    """
    return pd.read_csv(path)

def group_by_play(df: pd.DataFrame, keys=("game_id","play_id")):
    for (gid, pid), g in df.groupby(list(keys), sort=True):
        yield (gid, pid), g.sort_values("frame_id")
