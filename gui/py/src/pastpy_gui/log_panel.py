import wx


class LogPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        sizer = wx.BoxSizer(orient=wx.VERTICAL)
        sizer.Add(wx.StaticText(self, label="Log"),
                  flag=wx.EXPAND | wx.CENTER)
        self.__text_ctrl = wx.TextCtrl(self,
                                       style=wx.TE_MULTILINE | wx.TE_READONLY | wx.HSCROLL)
        sizer.Add(self.__text_ctrl, flag=wx.EXPAND)
        self.SetSizerAndFit(sizer)

    def write(self, string):
        self.__text_ctrl.WriteText(string)
