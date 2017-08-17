import wx
from app_frame import AppFrame

app = wx.App(redirect=False, useBestVisual=True)
frame = AppFrame()
app.MainLoop()
