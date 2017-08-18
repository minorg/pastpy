import logging
import sys
import wx


class LogPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        vertical_sizer = wx.BoxSizer(orient=wx.VERTICAL)
        vertical_sizer.AddSpacer(10)

        title_sizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        checkbox = wx.CheckBox(parent=self, label='Enable debug logging')

        def on_checkbox(event):
            if event.IsChecked():
                logging.getLogger().setLevel(logging.DEBUG)
                logging.debug('enabled debug logging')
            else:
                logging.getLogger().setLevel(logging.INFO)
                logging.debug('disabled debug logging')
                logging.info('disabled debug logging')
        checkbox.Bind(wx.EVT_CHECKBOX, on_checkbox)
        title_sizer.Add(wx.StaticText(parent=self, label="Log"),
                        flag=wx.ALIGN_CENTRE_HORIZONTAL)
        vertical_sizer.Add(title_sizer,
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

        sys.stdout = self
        sys.stderr = self
        root_logger = logging.getLogger()
        for handler in list(root_logger.handlers):
            root_logger.removeHandler(handler)
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s'))
        root_logger.addHandler(handler)

    def write(self, string):
        self.__text_ctrl.SetValue(self.__text_ctrl.GetValue() + string)
