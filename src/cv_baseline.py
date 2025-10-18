from typing import Tuple
import numpy as np
from .geometry import clamp_field, clamp_speed, DT

def estimate_velocity(x_hist, y_hist, dt=DT, k=5) -> Tuple[float, float]:
    """Estimate last-k-step average velocity."""
    if len(x_hist) < 2:
        return 0.0, 0.0
    dx = np.diff(x_hist[-k:]) / dt
    dy = np.diff(y_hist[-k:]) / dt
    vx = float(dx.mean()) if len(dx) else 0.0
    vy = float(dy.mean()) if len(dy) else 0.0
    return vx, vy

def predict_cv(x0, y0, vx, vy, T, dt=DT):
    n = max(int(round(T / dt)), 1)
    xs = x0 + vx * np.arange(1, n+1) * dt
    ys = y0 + vy * np.arange(1, n+1) * dt
    xs, ys = clamp_field(xs, ys)
    return np.stack([xs, ys], axis=1)

def attraction_step(x, y, target_x, target_y, alpha=0.5, dt=DT):
    # small step toward target point
    dx = target_x - x
    dy = target_y - y
    vx = alpha * dx / max(dt, 1e-6)
    vy = alpha * dy / max(dt, 1e-6)
    vx, vy = clamp_speed(vx, vy)
    return x + vx * dt, y + vy * dt

def predict_b1_interaction(x0, y0, vx, vy, T, attract_to=None, alpha=0.15, dt=DT):
    """CV + mild attraction to a point (e.g., ball landing or WR)."""
    n = max(int(round(T / dt)), 1)
    xs, ys = [], []
    x, y = x0, y0
    for _ in range(n):
        # CV step
        x = x + vx * dt
        y = y + vy * dt
        # Interaction
        if attract_to is not None:
            x, y = attraction_step(x, y, attract_to[0], attract_to[1], alpha=alpha, dt=dt)
        xs.append(x); ys.append(y)
    xs = np.array(xs); ys = np.array(ys)
    xs, ys = clamp_field(xs, ys)
    return np.stack([xs, ys], axis=1)
