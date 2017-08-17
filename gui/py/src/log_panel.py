import wx


class LogPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, wx.ID_ANY)

        box_sizer = wx.BoxSizer(wx.VERTICAL)
        box_sizer.Add(wx.StaticText(self, label="Log"))
        self.__text_ctrl = wx.TextCtrl(self, wx.ID_ANY,
                                       style=wx.TE_MULTILINE | wx.TE_READONLY | wx.HSCROLL)
        box_sizer.Add(self.__text_ctrl, 1, wx.EXPAND)
        self.SetSizer(box_sizer)

    def write(self, string):
        self.__text_ctrl.WriteText(string)
