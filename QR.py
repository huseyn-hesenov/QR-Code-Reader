import pyqrcode,png
from pyqrcode import QRCode
QRstring="------" # url yazilmalidi
url=pyqrcode.create(QRstring)
url.png('Desktop\\kod.png',scale=8)