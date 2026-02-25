import numpy as np
from app.routes.query import chunk_similarity


def test_chunk_similarity():
    a = np.array([1, 0])
    b = np.array([1, 0])
    assert chunk_similarity(a, b) == 1.0