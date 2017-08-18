import logging
from site_generator import SiteGenerator
from models.site_generator_model import SiteGeneratorModel
import wx


class SiteGeneratorPanel(wx.Panel):
    class NotebookPanel(wx.Panel):
        GRID_HGAP_PX = 10
        GRID_VGAP_PX = 40
        INPUT_INSTRUCTIONS_HGAP_PX = 10
        INSTRUCTIONS_LABEL_WIDTH_PX = 400
        PADDING_LEFT_PX = 10
        PADDING_BOTTOM_PX = 10
        PADDING_RIGHT_PX = 10
        PADDING_TOP_PX = 10

        def __init__(self, model, parent):
            wx.Panel.__init__(self, parent=parent)

            self.__model = model

            self._grid_sizer = wx.FlexGridSizer(
                cols=6, hgap=self.GRID_HGAP_PX, vgap=self.GRID_VGAP_PX)
            self._add_inputs()
            self.__add_output_dir_path_input()
            self.__add_generate_site_button()

            vertical_sizer = wx.BoxSizer(orient=wx.VERTICAL)
            vertical_sizer.AddSpacer(self.PADDING_TOP_PX)
            vertical_sizer.Add(self._grid_sizer, flag=wx.EXPAND)
            vertical_sizer.AddSpacer(self.PADDING_BOTTOM_PX)
            self.SetSizerAndFit(vertical_sizer)

        def _add_dir_path_input(self, **kwds):
            return self.__add_path_input(dir_=True, **kwds)

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

            self._grid_sizer.AddSpacer(self.PADDING_LEFT_PX)
            self._grid_sizer.AddSpacer(0)
            self._grid_sizer.Add(button)
            self._grid_sizer.AddSpacer(0)
            self._grid_sizer.AddSpacer(0)
            self._grid_sizer.AddSpacer(self.PADDING_RIGHT_PX)
            button.SetFocus()

        def _add_file_path_input(self, **kwds):
            return self.__add_path_input(dir_=False, **kwds)

        def __add_input(self, label, control, instructions=None):
            self._grid_sizer.AddSpacer(self.PADDING_LEFT_PX)
            self._grid_sizer.Add(wx.StaticText(
                parent=self, label=label), flag=wx.ALIGN_TOP)
            self._grid_sizer.Add(control)
            self._grid_sizer.AddSpacer(self.INPUT_INSTRUCTIONS_HGAP_PX)
            if instructions is not None:
                instructions_label = wx.StaticText(
                    parent=self, label=instructions)
                instructions_label.Wrap(self.INSTRUCTIONS_LABEL_WIDTH_PX)
                self._grid_sizer.Add(instructions_label,
                                     flag=wx.ALIGN_CENTRE_VERTICAL)
            else:
                self._grid_sizer.AddSpacer(0)
            self._grid_sizer.AddSpacer(self.PADDING_RIGHT_PX)

        def __add_path_input(self, dir_, instructions, label, model_property_name, style=0, wildcard=None):
            panel = wx.Panel(parent=self)

            text_ctrl = wx.TextCtrl(
                parent=panel, size=wx.Size(256, wx.DefaultSize.height))

            value = getattr(self.model, model_property_name)
            if value is not None:
                text_ctrl.SetValue(value)

            def on_button_click(_event):
                if dir_:
                    dialog = wx.DirDialog(
                        parent=self,
                        style=wx.DD_DEFAULT_STYLE | style)
                else:
                    dialog = wx.FileDialog(
                        parent=self,
                        style=wx.FD_OPEN | style,
                        wildcard=wildcard
                    )
                if dialog.ShowModal() == wx.ID_OK:
                    path = dialog.GetPath()
                    if path:
                        setattr(self.model, model_property_name, path)
                        text_ctrl.SetValue(path)
            button = wx.Button(parent=panel, label='Browse')
            button.Bind(wx.EVT_LEFT_DOWN, on_button_click)

            sizer = wx.BoxSizer(orient=wx.HORIZONTAL)
            sizer.Add(text_ctrl, flag=wx.ALIGN_CENTRE_VERTICAL | wx.EXPAND)
            sizer.AddSpacer(10)
            sizer.Add(button, flag=wx.ALIGN_CENTRE_VERTICAL)
            panel.SetSizerAndFit(sizer)

            return self.__add_input(control=panel, instructions=instructions, label=label)

        def __add_output_dir_path_input(self):
            return self._add_dir_path_input(
                instructions="Directory where generated files and copied images will be stored.",
                label='Output directory',
                model_property_name='output_dir_path')

        def _add_pp_objects_dbf_file_path(self, optional):
            instructions = "Path to a PastPerfect objects database, such as C:\pp5\Data\OBJECTS.DBF. This can be also an exported DBF (FoxPro) with a selection of objects, such as C:\pp5Reports\PPSdata.dbf."
            if optional:
                instructions = instructions + " Leave blank to use all objects."
            return self._add_file_path_input(
                instructions=instructions,
                label='PastPerfect objects database',
                model_property_name='pp_objects_dbf_file_path',
                wildcard="DBF files (*.dbf)|*.dbf"
            )

        @property
        def model(self):
            return self.__model

        def _sync_from_model(self):
            raise NotImplementedError(self)

    class AdvancedPanel(NotebookPanel):
        def _add_inputs(self):
            self._add_dir_path_input(
                instructions="Directory where PastPerfect Images reside, such as C:\pp5\Images.",
                label='PastPerfect images directory',
                model_property_name='pp_images_dir_path',
                style=wx.DD_DIR_MUST_EXIST)

            self._add_pp_objects_dbf_file_path(optional=False)

    class BasicPanel(NotebookPanel):
        def _add_inputs(self):
            self._add_dir_path_input(
                instructions="Directory where PastPerfect is installed, such as C:\pp5. One way to find this directory on Windows is to go to the start menu, find the PastPerfect program icon, right-click on it, and look at the 'Target' property under the 'Shortcuts' tab. It will be something like C:\pp5\pp5.exe. In this case the PastPerfect installation directory is C:\pp5 (taking off the pp5.exe part).",
                label='PastPerfect installation directory',
                model_property_name='pp_install_dir_path',
                style=wx.DD_DIR_MUST_EXIST)

            self._add_pp_objects_dbf_file_path(optional=True)

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        self.__model = SiteGeneratorModel()

        notebook = wx.Notebook(parent=self)
        notebook.AddPage(self.BasicPanel(
            model=self.__model, parent=notebook), "Basic")
        notebook.AddPage(self.AdvancedPanel(
            model=self.__model, parent=notebook), "Advanced")

        vertical_sizer = wx.BoxSizer(orient=wx.VERTICAL)
        vertical_sizer.Add(notebook, flag=wx.EXPAND)
        self.SetSizerAndFit(vertical_sizer)

    @property
    def model(self):
        return self.__model
