# Myanmar Yoe Shin Font Collection

> **မြန်မာဖွန့် အသုံးပြုနည်း - Myanmar Font Collection for All Platforms**

မြန်မာ Unicode ဖွန့် ၈ မျိုး ပါဝင်ပါသည်။ ဘယ်နေရာမဆို အသုံးပြုနိုင်ပါသည်။

---

## 📋 Font List

| Font | File | Size | Author | Style |
|------|------|------|--------|-------|
| **A10_YoeShin** | `A10_YoeShin-Regular.ttf` | 58 KB | Kaung Myat | Classic |
| **Burma026** | `Burma026-Regular.ttf` | 263 KB | Moezed | Bold |
| **M01_PuPu Bold** | `M01_PuPu Bold.ttf` | 54 KB | Myat Ei Ei San (Suika) | Decorative |
| **M03_Myittar** | `M03_Myittar-Regular.ttf` | 63 KB | netpanchi.com | Modern |
| **Myanmar Ayar** | `MyanmarAyarTyepwriter.ttf` | 220 KB | Digital Signed | Typewriter |
| **MyanmarPaOhOne** | `MyanmarPaOhOne.ttf` | 334 KB | - | Traditional |
| **PangLong** | `PangLong_2011feb7.ttf` | 427 KB | - | Elegant |
| **Phantee Hand Written** | `Phantee Hand Written.ttf` | 129 KB | - | Handwritten |

---

## 🌐 Web / HTML / Blog

### Method 1: CSS Link

```html
<link rel="stylesheet" href="https://raw.githubusercontent.com/YOUR_USER/myanmar-yoe-shin-fonts/main/css/myanmar-fonts.css">
```

Then use font classes:

```html
<p class="font-yoeshin">ယိုးရှင် ဖွန့်ဖြင့် ရေးထားသည်</p>
<p class="font-burma026">Burma026 ဖွန့်ဖြင့် ရေးထားသည်</p>
<p class="font-pupu">PuPu ဖွန့်ဖြင့် ရေးထားသည်</p>
<p class="font-myittar">Myittar ဖွန့်ဖြင့် ရေးထားသည်</p>
<p class="font-myanmar-ayar">Ayar Typewriter ဖွန့်ဖြင့် ရေးထားသည်</p>
<p class="font-paoh">MyanmarPaOhOne ဖွန့်ဖြင့် ရေးထားသည်</p>
<p class="font-panglong">PangLong ဖွန့်ဖြင့် ရေးထားသည်</p>
<p class="font-phantee">Phantee Hand Written ဖွန့်ဖြင့် ရေးထားသည်</p>
```

### Method 2: Inline @font-face

```css
@font-face {
  font-family: 'MyanmarFont';
  src: url('fonts/A10_YoeShin-Regular.ttf') format('truetype');
  font-display: swap;
}

body {
  font-family: 'MyanmarFont', sans-serif;
}
```

### Method 3: GitHub Pages

1. `fonts/` folder ကို repo ထဲထည့်ပါ
2. CSS ထဲမှာ path ပြင်ပါ: `src: url('/fonts/A10_YoeShin-Regular.ttf')`
3. OR `css/myanmar-fonts.css` ကို link ထည့်ပါ

---

## 📄 PDF (Python)

```python
from fpdf import FPDF

pdf = FPDF()
pdf.add_font('YoeShin', '', 'fonts/A10_YoeShin-Regular.ttf')
pdf.add_font('PuPu', '', 'fonts/M01_PuPu Bold.ttf')
pdf.add_page()

pdf.set_font('YoeShin', '', 14)
pdf.cell(0, 10, 'ယိုးရှင် ဖွန့်ဖြင့် PDF ရေးခြင်း')

pdf.set_font('PuPu', '', 12)
pdf.cell(0, 10, 'PuPu ဖွန့်ဖြင့် PDF ရေးခြင်း')

pdf.output('output.pdf')
```

---

## 📱 EPUB

```python
from ebooklib import epub
import os

book = epub.EpubBook()
book.set_identifier('myanmar-fonts-book')
book.set_title('Myanmar Font Demo')
book.set_language('my')

# Font file ထည့်
fonts = {
    'yoeshin': 'fonts/A10_YoeShin-Regular.ttf',
    'pupu': 'fonts/M01_PuPu Bold.ttf',
    'myittar': 'fonts/M03_Myittar-Regular.ttf',
}

for name, path in fonts.items():
    with open(path, 'rb') as f:
        font_data = f.read()
    item = epub.EpubItem(
        uid=name,
        file_name=f'fonts/{os.path.basename(path)}',
        media_type='application/octet-stream',
        content=font_data
    )
    book.add_item(item)

# CSS ထဲမှာ font-face
css = b'''
@font-face {
    font-family: 'YoeShin';
    src: url('fonts/A10_YoeShin-Regular.ttf') format('truetype');
}
body { font-family: 'YoeShin', serif; line-height: 1.8; }
'''
style = epub.EpubItem(uid='style', file_name='style/myanmar.css',
                      media_type='text/css', content=css)
book.add_item(style)
```

---

## 📝 Markdown / GitHub README

GitHub Markdown မှာ CSS မသုံးနိုင်ပေမယ့်:

1. **GitHub Pages** - CSS ချိတ်ပြီး မြန်မာဖွန့် သုံးနိုင်
2. **Jekyll Blog** - `_includes/head.html` ထဲမှာ link ထည့်
3. **Hugo Blog** - `layouts/partials/head.html` ထဲမှာ link ထည့်
4. **WordPress** - Theme CSS ထဲမှာ @font-face ထည့်

```markdown
# My Blog

> Font: [YoeShin](https://github.com/YOUR_USER/myanmar-yoe-shin-fonts)

<!-- GitHub Pages မှာ blog post ထဲမှာ CSS ထည့်ပြီး သုံးနိုင် -->
```

---

## 🛠 Setup

### Quick Start (3 steps)

```bash
# 1. Clone or download
git clone https://github.com/YOUR_USER/myanmar-yoe-shin-fonts.git

# 2. Copy fonts to your project
cp fonts/*.ttf /your/project/fonts/

# 3. Link CSS (for web)
# Add to your HTML:
# <link rel="stylesheet" href="css/myanmar-fonts.css">
```

### Folder Structure

```
myanmar-yoe-shin-fonts/
├── fonts/
│   ├── A10_YoeShin-Regular.ttf      (58 KB)
│   ├── Burma026-Regular.ttf          (263 KB)
│   ├── M01_PuPu Bold.ttf            (54 KB)
│   ├── M03_Myittar-Regular.ttf      (63 KB)
│   └── MyanmarAyarTyepwriter.ttf    (220 KB)
├── css/
│   └── myanmar-fonts.css
├── examples/
│   └── (usage examples)
├── demo.html
└── README.md
```

---

## 📌 License

These fonts are **free for personal use**.
- **A10_YoeShin** - Copyright (c) 2024 Kaung Myat
- **Burma026** - Copyright (c) 2022 Moezed
- **M01_PuPu Bold** - Copyright (c) 2024 Myat Ei Ei San (Suika)
- **M03_Myittar** - Copyright (c) 2024 netpanchi.com
- **Myanmar Ayar** - Version 3.30, 2020
- **MyanmarPaOhOne** - Free for personal use
- **PangLong** - Free for personal use
- **Phantee Hand Written** - Free for personal use

For commercial use, please contact the respective font authors.

---

## 🔗 Links

- **Facebook**: [Whisper Of Words](https://www.facebook.com/mmebookwhisper/)
- **Telegram**: [@TheBookR](https://t.me/TheBookR)
- **YouTube**: [@whisperofwordsebook](https://www.youtube.com/@whisperofwordsebook)

---

## 💡 Tips

| Platform | How to Use |
|----------|------------|
| **Website/Blog** | CSS `@font-face` + class |
| **GitHub Pages** | Same as website |
| **WordPress** | Theme settings or Custom CSS |
| **PDF** | Python `fpdf2` library |
| **EPUB** | `ebooklib` + embedded fonts |
| **App (Flutter/React)** | Copy fonts/ to assets folder |
| **Desktop App** | System font install |
| **Figma/Design** | Install font on system |

---

*Created for Myanmar Epub Community*
