import logging
from site_generator import SiteGenerator
import wx


class ControlPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        self._pp_install_dir_path = None
        self._output_dir_path = None

        # TODO: use a FlexGridSizer instead of the nested sizers
        sizer = wx.BoxSizer(orient=wx.VERTICAL)
        sizer.Add(self.__add_pp_install_dir_path_input())
        sizer.AddSpacer(20)
        sizer.Add(self.__add_output_dir_path_input())
        sizer.AddSpacer(20)
        sizer.Add(self.__add_generate_site_button())
        self.SetSizerAndFit(sizer)

    def __add_generate_site_button(self):
        button = wx.Button(self, label='Generate site')

        def on_button_click(event):
            if self._output_dir_path is None:
                logging.warn("Must set output directory path")
                event.Skip()
                return
            elif self._pp_install_dir_path is None:
                logging.warn(
                    "Must set PastPerfect installation directory path")
                event.Skip()
                return

            SiteGenerator(output_dir_path=self._output_dir_path,
                          pp_install_dir_path=self._pp_install_dir_path).generate()

        button.Bind(wx.EVT_LEFT_DOWN, on_button_click)
        sizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        sizer.AddSpacer(10)
        sizer.Add(button, proportion=1,
                  flag=wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND)
        sizer.AddSpacer(10)
        button.SetFocus()
        return sizer

    def __add_dir_path_input(self, label, property_name, style=0):
        text_ctrl = wx.TextCtrl(parent=self)

        def on_text_ctrl_click(_event):
            dir_dialog = wx.DirDialog(
                parent=self, style=wx.DD_DEFAULT_STYLE | style)
            if dir_dialog.ShowModal() == wx.ID_OK:
                path = dir_dialog.GetPath()
                if path:
                    setattr(self, '_' + property_name, path)
                    text_ctrl.Clear()
                    text_ctrl.WriteText(path)
        text_ctrl.Bind(wx.EVT_LEFT_DOWN, on_text_ctrl_click)

        return self.__add_input(control=text_ctrl, label=label)

    def __add_input(self, label, control):
        sizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        sizer.AddSpacer(10)
        sizer.Add(wx.StaticText(
            parent=self, label=label), flag=wx.ALIGN_CENTER_VERTICAL)
        sizer.AddSpacer(20)
        sizer.Add(control,
                  flag=wx.EXPAND, proportion=2)
        sizer.AddSpacer(10)
        return sizer

    def __add_output_dir_path_input(self):
        return self.__add_dir_path_input(label='Output directory', property_name='output_dir_path')

    def __add_pp_install_dir_path_input(self):
        return self.__add_dir_path_input(label='PastPerfect installation directory', property_name='pp_install_dir_path', style=wx.DD_DIR_MUST_EXIST)

    @property
    def pp_install_dir_path(self):
        return self._pp_install_dir_path
