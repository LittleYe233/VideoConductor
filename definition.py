# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont
from collections import OrderedDict
from constant import *

# Constant
# Has been already imported!

# Base Class
class BaseSE(object):
	def __init__(self):
		pass
		
	def show(self):
		pass

# Class
class Text(object):
	def __init__(self, pos, text, font, color):
		self.pos = pos
		self.text = text
		self.font = ImageFont.truetype(*font[: 3]) # (ttf, size, index)
		self.color = color # (r, g, b)
		
	def __image__(self):
		pass

class Picture(object):
	def __init__(self, pos, fp): # fp = path or size
		self.pos = pos # (x, y)
		self.img = Image.open(fp) if type(fp) == 'str' else Image.new('RGB', fp)
		self.size = self.img.size # Refer to the same variable
		
	def __image__(self):
		pass
		
class Graphic(object): # PIL.Image.Image object
	def __init__(self):
		pass
		
	def __image__(self):
		pass

class Timeline(object):
	def __init__(self, objects=None):
		self.objects = OrderedDict() if objects == None else OrderedDict(objects) # (time, object) objects = dict or OrderedDict

class Video(object):
	def __init__(self):
		pass
		
class Project(object):
	def __init__(self, name='myvideo.lyproj', ext_name='myvideo.mp4', size=(640, 480), fps=24):
		self.name = name
		self.ext_name = ext_name
		self.size = size # (width, height)
		self.fps = fps
		self.pic_format = 'RGB'
		self.bg_color = (255, 255, 255)
		self.timelines = [Timeline()] # Default: 1 timeline