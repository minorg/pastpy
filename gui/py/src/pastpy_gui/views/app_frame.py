from .log_panel import LogPanel
from .site_generator_panel import SiteGeneratorPanel
import logging
import sys
import wx


class AppFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title='PastPy')

        # self.SetBackgroundColour(wx.WHITE)
        self.SetMenuBar(self._create_menu_bar())

        vertical_sizer = wx.BoxSizer(orient=wx.VERTICAL)

        vertical_sizer.AddSpacer(10)

        title_label = wx.StaticText(
            parent=self, label='PastPy', style=wx.ALIGN_CENTRE_HORIZONTAL)
        title_label.SetFont(wx.Font(24, wx.DECORATIVE, wx.NORMAL, wx.BOLD))
        vertical_sizer.Add(
            title_label, flag=wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND)

        vertical_sizer.AddSpacer(10)

        vertical_sizer.Add(self._add_site_generator_panel(), flag=wx.EXPAND)

        vertical_sizer.AddSpacer(100)

        vertical_sizer.Add(self._add_log_panel(), flag=wx.EXPAND)

        horizontal_sizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        horizontal_sizer.AddStretchSpacer(prop=1)
        horizontal_sizer.Add(vertical_sizer, proportion=4, flag=wx.EXPAND)
        horizontal_sizer.AddStretchSpacer(prop=1)
        self.SetSizerAndFit(horizontal_sizer)

        self.Show(True)
        self.Maximize(True)

    def _add_site_generator_panel(self):
        return SiteGeneratorPanel(parent=self)

    def _add_log_panel(self):
        log_panel = LogPanel(parent=self)
        sys.stdout = log_panel
        sys.stderr = log_panel
        root_logger = logging.getLogger()
        for handler in list(root_logger.handlers):
            root_logger.removeHandler(handler)
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        root_logger.addHandler(handler)
        return log_panel

    def _create_menu_bar(self):
        file_menu = wx.Menu()
        # file_menu.Append(wx.ID_ABOUT, "&About",
        #                  " Information about this program")
        # file_menu.AppendSeparator()
        menu_item = file_menu.Append(
            wx.ID_EXIT, "E&xit", " Terminate the program")
        self.Bind(wx.EVT_MENU, self.on_menu_exit, menu_item)

        menu_bar = wx.MenuBar()
        menu_bar.Append(file_menu, "&File")
        return menu_bar

    def on_menu_exit(self, _event):
        self.Close(True)
