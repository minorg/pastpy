import wx


class LogPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        vertical_sizer = wx.BoxSizer(orient=wx.VERTICAL)
        vertical_sizer.AddSpacer(10)
        vertical_sizer.Add(wx.StaticText(self, label="Log"),
                           flag=wx.ALIGN_CENTRE_HORIZONTAL)
        vertical_sizer.AddSpacer(10)
        self.__text_ctrl = wx.TextCtrl(self,
                                       size=wx.Size(
                                           width=wx.DefaultSize.width, height=128),
                                       style=wx.TE_MULTILINE | wx.TE_READONLY | wx.HSCROLL)
        vertical_sizer.Add(self.__text_ctrl, flag=wx.EXPAND)
        vertical_sizer.AddSpacer(10)

        # horizontal_sizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        # horizontal_sizer.AddSpacer(10)
        # horizontal_sizer.Add(vertical_sizer, proportion=1, flag=wx.EXPAND)
        # horizontal_sizer.AddSpacer(10)

        self.SetSizerAndFit(vertical_sizer)

    def write(self, string):
        self.__text_ctrl.WriteText(string)
