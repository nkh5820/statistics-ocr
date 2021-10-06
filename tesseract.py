from subprocess import PIPE
import subprocess
import re


# def command(txt):
#     lst = txt.split(" ")
#     cmd = ['cmd.exe', '/c']
#     [cmd.append(lst[i]) for i in range(len(lst))]
#     subprocess.run(cmd)


#width = int(input("Width: "))
#height = int(input("Height: "))
width = 70
height = 175
image = input("Image: ").split(".")

subprocess.run(["G:\\ImageMagick-7.1.0-Q16-HDRI\\convert.exe",
                f"G:\\Statistics-OCR\\Sample Images - Copy\\{image[0]}.PNG",
                "-crop",
                f"{width}x{height}",
                f"G:\\Statistics-OCR\\Sample Images - Copy\\{image[0]}.PNG"])
test = subprocess.run(["cmd.exe",
                       "/c",
                       "cd",
                       "G:\\Statistics-OCR\\Sample Images - Copy",
                       "&&",
                       "dir",
                       "/b"], stdout=PIPE)
images = test.stdout.decode("utf-8").replace("\r\n", " ").strip()
prefix = image[0]
subsections = re.findall("%s-[0-9]*" % prefix, images)
print(subsections)

for subsection in range(len(subsections)):
    subprocess.run(["G:\\Tesseract\\tesseract.exe",
                    f"G:\\Statistics-OCR\\Sample Images - Copy\\{image[0]}-{subsection}.PNG",
                    f"G:\\Statistics-OCR\\Sample Images - Copy Output\\Output ({subsection})",
                    "-c",
                    "tessedit_char_whitelist=0123456789"])
    with open(f"G:\\Statistics-OCR\\Sample Images - Copy Output\\Output (MASTER).txt", "a") as master:
        with open(f"G:\\Statistics-OCR\\Sample Images - Copy Output\\Output ({subsection}).txt", "r") as file:
            lines = file.readlines()
            for line in range(len(lines)):
                if len(lines[line].strip()) > 0:
                    master.write(lines[line].strip() + '\n')
total = 0
average = 0
with open(f"G:\\Statistics-OCR\\Sample Images - Copy Output\\Output (MASTER).txt", "r") as master:
    lines = master.readlines()
    for line in range(len(lines)):
        total += int(lines[line])
    average = total / len(lines)
    print(lines)
print(total)
print(average)
