
def bcode_gen(data= "BS34000405" ):
    from barcode import Code128
    from barcode.writer import ImageWriter 
    code = Code128(data, writer=ImageWriter())  # Create a Code128 object
    mycode = code.save("Mycode")
    return code