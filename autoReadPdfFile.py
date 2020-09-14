import pyttsx3
import PyPDF2
resume = open('Biddut Bhowmik.pdf', 'rb') #which pdf you want to read
pdfReader = PyPDF2.PdfFileReader(resume)
pages = pdfReader.numPages
friend = pyttsx3.init()
page = pdfReader.getPage(0) # page number you want to read
text = page.extractText()
friend.say(text)
friend.runAndWait()
