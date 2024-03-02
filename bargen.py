from barcode import *


def bcode_gen(data="https://idp.unicampania.it/idp/Authn/UserPassword"):
    from barcode import Code128
    from barcode.writer import ImageWriter
    code = Code128(data, writer=ImageWriter())  # Create a Code128 object
    mycode = code.save("barcode")


bcode_gen()
