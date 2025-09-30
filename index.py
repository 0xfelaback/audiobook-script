import pyttsx3
import PyPDF3

with open('book.pdf', 'rb') as book:

    reader = PyPDF3.PdfFileReader(book)
    for i,page in enumerate(reader.pages):
        text = page.extract_text()
    with open(f"chapter_{i+1}.txt", "w", encoding="utf-8") as f:
        f.write(text)

    reader = PyPDF3.PdfFileReader(book)
    
    
    audio_reader = pyttsx3.init()
    full_text = ""
    audio_reader.setProperty("rate", 100)
    for page in range(reader.numPages):
        next_page = reader.getPage(page)
        content = next_page.extractText()
        full_text += content

    audio_reader.save_to_file(full_text, "myaudiobook.mp3")
    audio_reader.runAndWait()
