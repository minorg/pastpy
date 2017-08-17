import wx


class ControlPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        sizer = wx.FlexGridSizer(2)
        sizer.Add(wx.StaticText(
            parent=self, label="PastPerfect installation directory"), flag=wx.EXPAND)
        self.__text_ctrl = wx.TextCtrl(parent=self)
        self.__text_ctrl.Bind(wx.EVT_LEFT_DOWN, self.__on_text_ctrl_click)
        sizer.Add(self.__text_ctrl, flag=wx.EXPAND)
        sizer.AddGrowableCol(1)
        self.SetAutoLayout(True)
        self.SetSizerAndFit(sizer)
        self.__pp_install_dir_path = None

    def __on_text_ctrl_click(self, _event):
        dir_dialog = wx.DirDialog(
            parent=self, style=wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST)
        if dir_dialog.ShowModal() == wx.OK:
            path = dir_dialog.GetPath()
            if path:
                self.__pp_install_dir_path = path
                self.__text_ctrl.Clear()
                self.__text_ctrl.WriteText(path)

    @property
    def pp_install_dir_path(self):
        return self.__pp_install_dir_path
