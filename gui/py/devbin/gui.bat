@ECHO OFF
set PYTHONPATH=%~dp0..\src;%~dp0..\..\..\lib\src;%~dp0..\..\..\site_generator\src
python %~dp0..\src\pastpy_gui\app.py