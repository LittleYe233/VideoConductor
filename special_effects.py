# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont
from definition import BaseSE

# We define a base class 'BaseSE' to define the base of every special effect (defined in definition.py).
# Some base effects like 'Fade', 'Move' will inherit 'BaseSE' and called 'BaseFade', 'BaseMove'.
# And the other special effects like 'Move in a line' will inherit the base effect classes and called 'MoveLinear'.

# Base Special Effect Class
class BaseFade(BaseSE):
	pass
	
class BaseMove(BaseSE):
	pass
	
class BaseRotate(BaseSE):
	pass

# Special Effect Class
class FadeIn(BaseFade):
	pass