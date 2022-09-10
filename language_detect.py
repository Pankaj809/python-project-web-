#import library
from langdetect import detect
#take the sentence from user for detection
text= input("Enter the text: ")

#printing output
print(detect(text))

#ISO 639 is a standardized nomenclature used to classify languages. Each language is assigned a two-letter (639-1) and three-letter (639-2 and 639-3) lowercase abbreviation, amended in later versions of the nomenclature.
#langdetect supports 55 languages out of the box (ISO 639-1 codes):