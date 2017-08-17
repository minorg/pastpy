import wx


class AppFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title='PastPy')
        self.SetMenuBar(self._create_menu_bar())
        self.Show(True)
        self.Maximize(True)

    def _create_menu_bar(self):
        file_menu = wx.Menu()
        # file_menu.Append(wx.ID_ABOUT, "&About",
        #                  " Information about this program")
        # file_menu.AppendSeparator()
        menu_item = file_menu.Append(
            wx.ID_EXIT, "E&xit", " Terminate the program")
        self.Bind(wx.EVT_MENU, self.on_click_file_menu_exit, menu_item)

        menu_bar = wx.MenuBar()
        menu_bar.Append(file_menu, "&File")
        return menu_bar

    def on_click_file_menu_exit(self, _event):
        self.Close(True)
