from ocr import ocr_file
import json

img = ocr_file(filename='C:/Users/Owner/Downloads/ocrtest.PNG')
print(img)
text = json.loads(img.strip())
print(text)

data = text['ParsedResults'][0]['ParsedText']
x = data.replace("\r\n", " ")
y = x.split(" ")
y.remove("")
z = sorted([int(y[i]) for i in range(0, len(y))])

print("Sum: ", sum(z))
print("Length: ", len(z))
print("Mean: ", round(sum(z) / len(y), 2))
