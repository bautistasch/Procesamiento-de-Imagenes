import numpy as np

from property import Range


def radon(image: np.ndarray, angles: list[float]) -> list[np.ndarray]:
    # TODO: Hacer
    return [image for angle in angles]

def inverse_radon(radon: list[tuple[float, np.ndarray]], interpolation: str, filter: str, size: int) -> np.ndarray:
    # TODO: Hacer
    return np.zeros((size, size), dtype=np.float32)
