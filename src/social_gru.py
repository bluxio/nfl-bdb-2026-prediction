# Minimal scaffold (no heavy deps beyond torch)
from typing import Optional
import torch, torch.nn as nn

class NeighborPool(nn.Module):
    def __init__(self, in_dim: int, out_dim: int):
        super().__init__()
        self.mlp = nn.Sequential(nn.Linear(in_dim, out_dim), nn.ReLU(), nn.Linear(out_dim, out_dim))
    def forward(self, self_feats, neighbor_feats):
        # neighbor_feats: (B, N, K, F); self_feats: (B, N, F)
        pooled = neighbor_feats.mean(dim=2)  # simple mean; replace with attention later
        return self.mlp(torch.cat([self_feats, pooled], dim=-1))

class SocialGRU(nn.Module):
    def __init__(self, feat_dim=16, hidden=128):
        super().__init__()
        self.embed = nn.Linear(feat_dim, hidden)
        self.pool = NeighborPool(hidden+hidden, hidden)
        self.gru = nn.GRU(input_size=hidden, hidden_size=hidden, batch_first=True)
        self.head = nn.Linear(hidden, 2)  # Δx, Δy
    def forward(self, feats_seq, neighbor_seq, steps=25):
        # feats_seq: (B,N,T,F), neighbor_seq: (B,N,T,K,F)
        B,N,T,F = feats_seq.shape
        h = self.embed(feats_seq[:, :, -1, :])              # last pre-throw features
        h = torch.relu(h)
        pooled = self.pool(h, neighbor_seq[:, :, -1, :, :])
        H0 = pooled.transpose(0,1).contiguous()             # (N,B,H) -> treat N as batch for simplicity (toy)
        xs = []
        x_t = pooled
        for _ in range(steps):
            out, H0 = self.gru(x_t.unsqueeze(1), H0.unsqueeze(0))
            x_t = out.squeeze(1)
            xs.append(self.head(x_t))
        return torch.stack(xs, dim=2)  # (B,N,steps,2)
