import pyqrcode
import png
from pyqrcode import QRCode
s="https://github.com/bhatnagaranshika02"
url = pyqrcode.create(s)
url.svg("myqr.svg",scale = 8)
url.png("myqrcode.png",scale=6)
