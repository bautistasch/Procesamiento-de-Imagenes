import numpy as np

from property import Range
from scipy.interpolate import RectBivariateSpline
from skimage.data import shepp_logan_phantom
from skimage.transform import radon as skradon, rescale, rotate, iradon

def radon(image: np.ndarray, angles: list[float]) -> list[np.ndarray]:
    sinogram = skradon(image, theta=angles)
    return sinogram


def inverse_radon(radon: np.ndarray, angles: list[float], interpolation: str, filter: str, size: int) -> np.ndarray:
    reconstruction_img = iradon(radon, theta=angles, filter_name=filter)
    return reconstruction_img
