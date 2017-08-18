@ECHO OFF
set PYTHONPATH=%~dp0..\src;%~dp0..\..\..\lib\src
python %~dp0..\src\site_generator.py %*