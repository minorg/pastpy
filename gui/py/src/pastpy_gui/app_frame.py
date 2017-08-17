from control_panel import ControlPanel
from log_panel import LogPanel
import logging
import sys
import wx


class AppFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title='PastPy')

        self.SetMenuBar(self._create_menu_bar())

        box_sizer = wx.BoxSizer(orient=wx.VERTICAL)
        box_sizer.Add(self._add_control_panel(), flag=wx.EXPAND)
        box_sizer.Add(self._add_log_panel(), flag=wx.EXPAND)
        self.SetSizer(box_sizer)

        self.Show(True)
        self.Maximize(True)

    def _add_control_panel(self):
        return ControlPanel(parent=self)

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
