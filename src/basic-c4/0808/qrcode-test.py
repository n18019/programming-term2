import qrcode

img = qrcode.make("https://ja.wikipedia.org/wiki/%E3%83%81%E3%83%A7%E3%83%B3%E3%83%BB%E3%82%B8%E3%83%92%E3%83%A7%E3%83%B3")
img.save("qrcode-test.png")
