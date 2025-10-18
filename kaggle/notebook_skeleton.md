# Kaggle Notebook Skeleton — NFL BDB 2026 Prediction

This is a copy-paste scaffold. Create a new Kaggle Notebook and paste sections as code/markdown cells.

---

## 1) Imports & Config

```python
import numpy as np, pandas as pd, math
# Avoid non-allowed installs; rely on builtins + numpy/pandas (already present)
SEED = 42
rng = np.random.default_rng(SEED)
```

## 2) Utility Functions (geometry, metrics)

```python
FIELD_X_MIN, FIELD_X_MAX = 0.0, 120.0
FIELD_Y_MIN, FIELD_Y_MAX = 0.0, 53.3

def clamp_field(x, y):
    return np.clip(x, FIELD_X_MIN, FIELD_X_MAX), np.clip(y, FIELD_Y_MIN, FIELD_Y_MAX)

def rmse_xy(pred_xy, true_xy):
    # pred_xy, true_xy: (N,2) arrays
    return float(np.sqrt(np.mean((pred_xy - true_xy)**2)))
```

## 3) Data Load (competition paths)

```python
# TODO: replace with competition-provided paths (train/test)
# Example shapes only; the actual competition schema may differ.
```

## 4) Baseline B0 (Constant Velocity)

```python
def estimate_vel(x_hist, y_hist, dt=0.1, k=5):
    # simple last-k-step average velocity
    dx = np.diff(x_hist[-k:]) / dt
    dy = np.diff(y_hist[-k:]) / dt
    return np.mean(dx) if len(dx) else 0.0, np.mean(dy) if len(dy) else 0.0

def predict_cv(x0, y0, vx, vy, T, dt=0.1):
    ts = int(round(T/dt))
    xs = x0 + vx * np.arange(1, ts+1) * dt
    ys = y0 + vy * np.arange(1, ts+1) * dt
    xs, ys = clamp_field(xs, ys)
    return np.stack([xs, ys], axis=1)
```

## 5) Evaluation Harness

```python
# Time-based split; compute RMSE on holdout weeks
```

## 6) Build Submission

```python
# Produce rows: id,x,y with id = game_play_nflid_frame
```

---

## Notes
- Keep everything within Notebook runtime; no internet or external data.
- Start with B0 to validate your harness, then iterate.
