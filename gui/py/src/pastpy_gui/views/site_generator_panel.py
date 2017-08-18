import logging
from site_generator import SiteGenerator
from models.site_generator_model import SiteGeneratorModel
import wx


class SiteGeneratorPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        self.__model = SiteGeneratorModel()

        self.__grid_sizer = wx.FlexGridSizer(cols=6, hgap=10, vgap=10)
        self.__grid_sizer.AddGrowableCol(2)
        self.__add_pp_install_dir_path_input()
        self.__add_output_dir_path_input()
        self.__add_generate_site_button()

        vertical_sizer = wx.BoxSizer(orient=wx.VERTICAL)
        vertical_sizer.AddSpacer(10)
        vertical_sizer.Add(self.__grid_sizer, flag=wx.EXPAND)
        vertical_sizer.AddSpacer(10)
        self.SetSizerAndFit(vertical_sizer)

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

        self.__grid_sizer.AddSpacer(10)
        self.__grid_sizer.Add(button)
        self.__grid_sizer.AddSpacer(0)
        self.__grid_sizer.AddSpacer(0)
        button.SetFocus()

    def __add_dir_path_input(self, instructions, label, model_property_name, style=0):
        panel = wx.Panel(parent=self)

        text_ctrl = wx.TextCtrl(
            parent=panel, size=wx.Size(256, wx.DefaultSize.height))

        value = getattr(self.model, model_property_name)
        if value is not None:
            text_ctrl.SetValue(value)

        def on_button_click(_event):
            dir_dialog = wx.DirDialog(
                parent=self, style=wx.DD_DEFAULT_STYLE | style)
            if dir_dialog.ShowModal() == wx.ID_OK:
                path = dir_dialog.GetPath()
                if path:
                    setattr(self.model, model_property_name, path)
                    text_ctrl.SetValue(path)
        button = wx.Button(parent=panel, label='Browse')
        button.Bind(wx.EVT_LEFT_DOWN, on_button_click)

        sizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        sizer.Add(text_ctrl, flag=wx.ALIGN_CENTRE_VERTICAL | wx.EXPAND)
        sizer.Add(button, flag=wx.ALIGN_CENTRE_VERTICAL)
        panel.SetSizerAndFit(sizer)

        return self.__add_input(control=panel, instructions=instructions, label=label)

    def __add_input(self, label, control, instructions=None):
        self.__grid_sizer.AddSpacer(10)
        self.__grid_sizer.Add(wx.StaticText(
            parent=self, label=label), flag=wx.ALIGN_CENTRE_VERTICAL)
        self.__grid_sizer.Add(control)
        self.__grid_sizer.AddSpacer(10)
        if instructions is not None:
            self.__grid_sizer.Add(wx.StaticText(
                parent=self, label=instructions), flag=wx.ALIGN_CENTRE_VERTICAL)
        else:
            self.__grid_sizer.AddSpacer(0)
        self.__grid_sizer.AddSpacer(10)

    def __add_output_dir_path_input(self):
        return self.__add_dir_path_input(
            instructions="Directory where generated files and copied images will be stored.",
            label='Output directory',
            model_property_name='output_dir_path')

    def __add_pp_install_dir_path_input(self):
        return self.__add_dir_path_input(
            instructions="Directory where PastPerfect is installed, such as C:\pp5. This directory will contain an Images folder.",
            label='PastPerfect installation directory',
            model_property_name='pp_install_dir_path',
            style=wx.DD_DIR_MUST_EXIST)

    @property
    def model(self):
        return self.__model
