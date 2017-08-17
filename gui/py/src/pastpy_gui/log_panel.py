import wx


class LogPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        box_sizer = wx.BoxSizer(orient=wx.VERTICAL)
        box_sizer.Add(wx.StaticText(self, label="Log"),
                      flag=wx.EXPAND | wx.CENTER)
        self.__text_ctrl = wx.TextCtrl(self,
                                       style=wx.TE_MULTILINE | wx.TE_READONLY | wx.HSCROLL)
        box_sizer.Add(self.__text_ctrl, flag=wx.EXPAND)
        self.SetAutoLayout(True)
        self.SetSizerAndFit(box_sizer)
        self.SetFocus()

    def write(self, string):
        self.__text_ctrl.WriteText(string)
