import numpy as np
from tasks.task4 import generate_square_matrix


def test_square_matrix():
    m = generate_square_matrix()
    assert isinstance(m, np.ndarray)
    assert m.shape == (5, 5)
    assert np.allclose(m[1], np.square(m[0]))
