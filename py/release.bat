@ECHO OFF
rm -fr build dist *.egg-info
python setup.py sdist bdist_wheel
python -m twine upload dist/*
