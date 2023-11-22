import numpy as np

from property import Range
from scipy.interpolate import RectBivariateSpline
from skimage.data import shepp_logan_phantom
from skimage.transform import radon, rescale, rotate
from skimage.transform import radon, iradon

def radon(image: np.ndarray, angles: list[float]) -> list[np.ndarray]:
    sinogram = radon(image, theta=angles)
    return sinogram


def inverse_radon(radon: list[tuple[float, np.ndarray]], interpolation: str, filter: str, size: int) -> np.ndarray:
    reconstruction_img = iradon(radon[1], theta=radon[0], filter_name='ramp')
    res = np.zeros((size, size), dtype=np.float32)
    return reconstruction_img
