from wsgiref.validate import InputWrapper
from xml.sax.xmlreader import InputSource


x = int(InputWrapper())
y = int(InputSource())
res = (x * y) /12
print(f'{res:.3f}')