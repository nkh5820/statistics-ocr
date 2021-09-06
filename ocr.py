import requests


def ocr_file(filename, overlay=False, api_key='4b71beff2b88957', language='eng', ocr_engine=1):
    payload = {
        'isOverlayRequired': overlay,
        'apikey': api_key,
        'language': language,
        'OCREngine': ocr_engine
    }
    with open(filename, 'rb') as f:
        r = requests.post('https://api.ocr.space/parse/image',
                          files={filename: f},
                          data=payload,
                          )
    return r.content.decode()
