import chardet
with open(r'catalogo_cf.csv', 'rb') as f:
    msg = f.read()
    result = chardet.detect(msg)
    print(result)