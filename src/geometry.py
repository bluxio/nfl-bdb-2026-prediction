import numpy as np

FIELD_X_MIN, FIELD_X_MAX = 0.0, 120.0
FIELD_Y_MIN, FIELD_Y_MAX = 0.0, 53.3
MAX_SPEED = 10.0  # m/s (approx 22.4 mph)
DT = 0.1          # seconds between frames

def clamp_field(x, y):
    return np.clip(x, FIELD_X_MIN, FIELD_X_MAX), np.clip(y, FIELD_Y_MIN, FIELD_Y_MAX)

def clamp_speed(vx, vy, vmax=MAX_SPEED):
    v = np.hypot(vx, vy)
    if v <= vmax or v == 0.0:
        return vx, vy
    s = vmax / v
    return vx * s, vy * s
