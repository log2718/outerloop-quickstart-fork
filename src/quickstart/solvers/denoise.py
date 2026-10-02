"""Signal denoiser. Baseline: centered moving average, window 9.

Improvement ladder: better windows, Savitzky-Golay, Wiener/wavelet filtering,
anything that lowers held-out MSE. `denoise` must return an array of the same
shape; it sees only the noisy signal.
"""

from __future__ import annotations

import numpy as np


def denoise(noisy: np.ndarray) -> np.ndarray:
    """Return an estimate of the clean signal."""
    window = 39
    sigma = 9.0
    x = np.arange(window) - window // 2
    kernel = np.exp(-(x**2) / (2 * sigma**2))
    kernel = kernel / np.sum(kernel)
    padded = np.pad(noisy, window // 2, mode="reflect")
    return np.convolve(padded, kernel, mode="valid")
