import easyocr
reader = easyocr.Reader(['en']) # this needs to run only once to load the model into memory
result = reader.readtext('/Users/erickduarte/git/segmentation/pagesegment.png')

for (bbox, text, prob) in result:
    print(f'Text: {text}')