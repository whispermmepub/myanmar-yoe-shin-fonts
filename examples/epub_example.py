"""
Myanmar Font EPUB Example - မြန်မာဖွန့်ဖြင့် EPUB ဖန်တီးနည်း
Requires: pip install ebooklib
"""
from ebooklib import epub
import os

def create_myanmar_epub():
    book = epub.EpubBook()
    book.set_identifier('myanmar-font-demo-001')
    book.set_title('Myanmar Font Demo')
    book.set_language('my')
    book.add_metadata('DC', 'creator', 'Whisper Of Words')
    
    # Font files ထည့်
    font_dir = '../fonts'
    fonts_to_embed = {
        'yoeshin': 'A10_YoeShin-Regular.ttf',
        'burma026': 'Burma026-Regular.ttf', 
        'pupu': 'M01_PuPu Bold.ttf',
        'myittar': 'M03_Myittar-Regular.ttf',
        'ayar': 'MyanmarAyarTyepwriter.ttf',
    }
    
    for name, filename in fonts_to_embed.items():
        filepath = os.path.join(font_dir, filename)
        with open(filepath, 'rb') as f:
            font_data = f.read()
        
        font_item = epub.EpubItem(
            uid=name,
            file_name=f'fonts/{filename}',
            media_type='application/octet-stream',
            content=font_data
        )
        book.add_item(font_item)
    
    # CSS ဖန်တီး
    css_content = b'''
@font-face {
    font-family: 'YoeShin';
    src: url('fonts/A10_YoeShin-Regular.ttf') format('truetype');
}
@font-face {
    font-family: 'PuPu';
    src: url('fonts/M01_PuPu Bold.ttf') format('truetype');
}
@font-face {
    font-family: 'MyanmarAyar';
    src: url('fonts/MyanmarAyarTyepwriter.ttf') format('truetype');
}

body {
    font-family: 'YoeShin', serif;
    line-height: 2;
    margin: 20px;
}
h1 { font-family: 'PuPu', sans-serif; color: #2c3e50; }
.typewriter { font-family: 'MyanmarAyar', monospace; }
'''
    
    style = epub.EpubItem(
        uid='style',
        file_name='style/myanmar.css',
        media_type='text/css',
        content=css_content
    )
    book.add_item(style)
    
    # Chapter 1
    chapter1 = epub.EpubHtml(
        title='Chapter 1 - ယိုးရှင်',
        file_name='ch01.xhtml',
        lang='my'
    )
    chapter1.content = '''
<html><head><link rel="stylesheet" href="style/myanmar.css"/></head>
<body>
<h1>ယိုးရှင် ဖွန့်ဖြင့် ရေးထားသည်</h1>
<p>မြန်မာစာအုပ်များကို epub/kfx format ဖြင့် အခမဲ့ဖြန့်ဝေပါသည်။</p>
<p>သင့်ဖုန်းတွင် epub reader app ဖြင့် ဖတ်ရှုနိုင်ပါသည်။</p>
<p>အွန်လိုင်းမှ အခမဲ့ download ရယူနိုင်ပါသည်။</p>
</body></html>
'''
    book.add_item(chapter1)
    
    # Chapter 2 - Typewriter style
    chapter2 = epub.EpubHtml(
        title='Chapter 2 - အရေး',
        file_name='ch02.xhtml',
        lang='my'
    )
    chapter2.content = '''
<html><head><link rel="stylesheet" href="style/myanmar.css"/></head>
<body>
<h1>Myanmar Ayar Typewriter</h1>
<div class="typewriter">
<p>ဒီ chapter ကတော့ Ayar Typewriter ဖွန့်ဖြင့် ရေးထားတာပါ</p>
<p>Typewriter style ကို ကြိုက်ရင် ဒီဖွန့်ကို သုံးနိုင်ပါတယ်</p>
</div>
</body></html>
'''
    book.add_item(chapter2)
    
    # TOC
    book.toc = [chapter1, chapter2]
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())
    book.spine = ['nav', chapter1, chapter2]
    
    epub.write_epub('myanmar_font_demo.epub', book)
    print('EPUB created: myanmar_font_demo.epub')

if __name__ == '__main__':
    create_myanmar_epub()
