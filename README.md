
# nfl-bdb-2026-prediction
# NFL Big Data Bowl 2026 — Prediction (Starter Repo)

> Predict NFL player movement while the ball is in the air — with an emphasis on **learning** and **clean progression**.

This repository is designed to help you *learn by building*. It starts with a clear baseline and grows to more expressive models. Each step is documented and backed by a small, reliable validation harness so you can trust your improvements.

---

## What you’ll build (milestones)

1. **B0 — Constant Velocity (CV) Baseline**
   - Extrapolate each player’s last pre-throw velocity through the ball-flight frames.
   - Nudge the *targeted receiver* toward the known landing spot.
   - Clamp speeds and keep everyone in-bounds.
2. **B1 — CV + Simple Interaction**
   - Defenders get a small attraction toward the target or landing spot.
   - Add smoothness (acceleration) penalty to avoid jitter.
3. **M2 — Social-GRU (Lightweight Interaction RNN)**
   - Encode pre-throw context, then autoregress positions with a GRU.
   - Neighbor pooling over nearby players per frame.
4. **M3 — GNN-Transformer (Stretch)**
   - Nodes are players; edges by proximity.
   - Temporal transformer decoder to generate the trajectory sequence.

At every step: keep the same **offline RMSE** so results are comparable.

---

## Competition constraints (Kaggle Notebook)

- **Inputs:** Pre-throw tracking, targeted receiver, pass landing (x, y).
- **Outputs:** For each player and each frame in flight, predicted `(x, y)`.
- **Metric:** RMSE on `(x, y)` over all players/frames.
- **Notebook rules:** no internet, no external data, ≤ 9h runtime, output `submission.csv`.
- **ID format:** `{game_id}_{play_id}_{nfl_id}_{frame_id}`.

> This repo is for local learning and structure. Your final Kaggle Notebook should inline the necessary code (no `pip install`), or you can paste relevant modules into cells. Keep it portable.

---

## Repo layout

```
.
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt              # For local development only (not used on Kaggle)
├── notebooks/
│   └── 01_explore.ipynb         # Guided exploration & CV harness explanation
├── src/
│   ├── data_io.py               # Thin I/O layer (replace with Kaggle paths in Notebook)
│   ├── geometry.py              # Unit conversions, bounds, utilities
│   ├── metrics.py               # RMSE and diagnostics
│   ├── cv_baseline.py           # B0/B1 baselines
│   ├── social_gru.py            # M2 model (starter scaffold)
│   └── validation.py            # Time-based splits & evaluation loop
├── tools/
│   ├── check_submission.py      # Validates submission.csv format and stats
│   └── make_submission.py       # Example wiring (stubbed without real data)
└── kaggle/
    └── notebook_skeleton.md     # Copy-paste scaffold for Kaggle Notebook
```

---

## Learning-first explanation

### Why constant velocity first?
- It’s transparent, easy to debug, and gives a quick **yardstick**.
- You’ll learn how much of the task is resolved by just good extrapolation.
- It forces you to build the **evaluation loop** you’ll keep forever.

### Why a custom CV (validation) harness?
- The public LB scores **future weeks**. Mimic that locally via a **time-based split**.
- Fix the harness and never touch it; only models change. This prevents self-delusion.

### Why simple interaction next?
- Defenders don’t run randomly — they *pursue*. A tiny attraction force closes a big realism gap.
- You’ll feel the trade-off between physics priors and overfitting.

### Why GRU/GNN?
- Multi-agent motion is relational. A GRU with neighbor pooling is an approachable intro.
- GNN/transformer adds capacity to model complex interactions (if time allows).

---

## Getting started locally

1. **Create a virtual environment (optional):**
   ```bash
   uv venv && source .venv/bin/activate  # or: python -m venv .venv
   pip install -r requirements.txt
   ```
2. **Run quick checks:**
   ```bash
   python -m tools.check_submission --fake  # generates a tiny fake submission, validates format
   ```
3. **Read the Notebook skeleton:** `kaggle/notebook_skeleton.md` and `notebooks/01_explore.ipynb`.
4. **Implement B0:** in `src/cv_baseline.py`, fill in the TODOs. Then wire in `tools/make_submission.py`.

> When you move to Kaggle, paste the relevant `src/` code cells into the Notebook (or upload as a Kaggle Dataset for your own use if allowed by rules).

---

## Progression plan for GitHub (storytelling)

- **Commit 1:** project scaffold + README + fake submission validator.  
  _Message:_ “chore: repo scaffold + submission checker + learning roadmap”
- **Commit 2:** B0 constant-velocity baseline (no interactions).  
  _Message:_ “feat: B0 constant-velocity baseline + offline RMSE eval”
- **Commit 3:** B1 interactions + speed/bounds clamps.  
  _Message:_ “feat: B1 interactions and physics clamps; CV improvement”
- **Commit 4:** Social-GRU skeleton and training loop (no tuning).  
  _Message:_ “feat: M2 social-GRU model scaffold + trainer”
- **Commit 5:** Kaggle notebook export + submission script.  
  _Message:_ “feat: notebook export; ready for leaderboard”

Each commit should include a short note with **what you learned** and a **before/after CV RMSE**.

---

## License

MIT — do whatever you want; attribution appreciated.

---

## Acknowledgments

Inspired by the NFL Big Data Bowl 2026 competition. This repo is not affiliated with the NFL or Kaggle.
>>>>>>> eefcd5e (chore: repo scaffold + submission checker + learning roadmap)
