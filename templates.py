import numpy as np

TEMPLATES = {}

# Baseball
TEMPLATES["baseball"] = {}
TEMPLATES["baseball"]["home_plate"] = np.array([0, 0, 0], dtype=np.float32)
TEMPLATES["baseball"]["left_batters"] = np.array([-1, 0, 0], dtype=np.float32)
TEMPLATES["baseball"]["right_batters"] = np.array([1, 0, 0], dtype=np.float32)
TEMPLATES["baseball"]["pitchers_mound"] = np.array([0, 18.39, 0], dtype=np.float32)
TEMPLATES["baseball"]["first_base"] = np.array([18.39, 18.39, 0], dtype=np.float32)
TEMPLATES["baseball"]["second_base"] = np.array([0, 36.78, 0], dtype=np.float32)
TEMPLATES["baseball"]["third_base"] = np.array([-18.39, 18.39, 0], dtype=np.float32)