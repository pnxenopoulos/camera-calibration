import numpy as np

TEMPLATES = {}

# Baseball, in meters
TEMPLATES["baseball"] = {}
TEMPLATES["baseball"]["home_plate"] = np.array([0, 0, 0], dtype=np.float32)
TEMPLATES["baseball"]["left_batters"] = np.array([-1, 0, 0], dtype=np.float32)
TEMPLATES["baseball"]["right_batters"] = np.array([1, 0, 0], dtype=np.float32)
TEMPLATES["baseball"]["pitchers_mound_center"] = np.array([0, 18.39, 0], dtype=np.float32)  # or 0.254?
TEMPLATES["baseball"]["pitchers_mound_left"] = np.array([-0.4572, 18.39, 0], dtype=np.float32)
TEMPLATES["baseball"]["first_base"] = np.array([18.39, 18.39, 0], dtype=np.float32)
TEMPLATES["baseball"]["second_base"] = np.array([0, 36.78, 0], dtype=np.float32)
TEMPLATES["baseball"]["third_base"] = np.array([-18.39, 18.39, 0], dtype=np.float32)

# Basketball. in feet
TEMPLATES["basketball"] = {}
TEMPLATES["basketball"]["left_basket_base"] = np.array([0, 0, 0], dtype=np.float32)
TEMPLATES["basketball"]["left_basket_base_left"] = np.array([0,8,0], dtype=np.float32)
TEMPLATES["basketball"]["left_basket_base_right"] = np.array([0,-8,0], dtype=np.float32)
TEMPLATES["basketball"]["left_basket_base_left_inside"] = np.array([0,6,0], dtype=np.float32)
TEMPLATES["basketball"]["left_basket_base_right_inside"] = np.array([0,-6,0], dtype=np.float32)
TEMPLATES["basketball"]["upper_left"] = np.array([0,25,0], dtype=np.float32)
TEMPLATES["basketball"]["bottom_left"] = np.array([0,-25,0], dtype=np.float32)
TEMPLATES["basketball"]["left_basket_lower_curve"] = np.array([0, -3, 0], dtype=np.float32)
TEMPLATES["basketball"]["left_basket_upper_curve"] = np.array([0, 3, 0], dtype=np.float32)

