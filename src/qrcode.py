import pyqrcode

url = pyqrcode.create('http://uca.edu')
print(url.terminal(quiet_zone=1))