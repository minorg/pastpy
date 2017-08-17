import wx
from app_frame import AppFrame
import logging


logging.basicConfig(level=logging.INFO)
app = wx.App(redirect=False, useBestVisual=True)
frame = AppFrame()
app.MainLoop()
