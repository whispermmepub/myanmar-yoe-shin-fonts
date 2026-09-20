# Myanmar Yoe Shin Font Collection

> မြန်မာ Unicode ဖောင့်များ စုစည်းထားသော repository — Web, Android, Flutter, React, EPUB, PDF နှင့် Desktop projects များတွင် အသုံးပြုနိုင်ရန်။

## 📚 Included Fonts

Repository ထဲတွင် မြန်မာဖောင့်များစွာ ပါဝင်ပြီး **Walone** family ကိုလည်း ထည့်သွင်းထားပါသည်။

### Walone — One Click AI မှ web တွင်အသုံးပြုထားသော family

| Font | File | Weight | Style |
|---|---|---:|---|
| Walone Thin | `Walone-Thin.ttf` | 100 | Thin |
| Walone Regular | `Walone-Regular.ttf` | 400 | Regular |
| Walone Bold | `Walone-Bold.ttf` | 700 | Bold |

> Walone ၏ original web CSS တွင် တွေ့ရသော font-face definitions အရ Thin/Regular/Bold weight များကို သီးခြားထားရှိထားပါသည်။ Repo ထဲရှိ filename များသည် အသုံးပြုရလွယ်ကူစေရန် ရိုးရှင်းထားသော filenames ဖြစ်ပါသည်။

### Other featured fonts

- A10 YoeShin
- A07 Yadanabon (Light / Regular / Bold)
- Burma026
- M01 PuPu Bold
- M03 Myittar
- Myanmar Ayar Typewriter
- Myanmar PaOh
- PangLong
- Phantee Hand Written
- Tharlon
- နှင့် အခြား မြန်မာ Unicode ဖောင့်များ

ဖောင့်ဖိုင်များ၏ လက်ရှိစာရင်းအပြည့်အစုံကို `fonts/` folder တွင် ကြည့်နိုင်ပါသည်။

---

## 🌐 Web Usage

### Option 1 — Use the repository CSS

```html
<link rel="stylesheet"
      href="https://raw.githubusercontent.com/whispermmepub/myanmar-yoe-shin-fonts/main/css/myanmar-fonts.css">
```

ပြီးလျှင်:

```html
<p class="font-yoeshin">ယိုးရှင် ဖောင့်</p>
<p class="font-walone">Walone ဖောင့်</p>
<p class="font-burma026">Burma026 ဖောင့်</p>
<p class="font-pupu">PuPu ဖောင့်</p>
<p class="font-myittar">Myittar ဖောင့်</p>
```

### Walone weights

```html
<p class="font-walone font-walone-thin">Walone Thin</p>
<p class="font-walone">Walone Regular</p>
<p class="font-walone font-walone-bold">Walone Bold</p>
```

### Option 2 — Direct @font-face

```css
@font-face {
  font-family: 'Walone';
  src: url('fonts/Walone-Regular.ttf') format('truetype');
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}

@font-face {
  font-family: 'Walone';
  src: url('fonts/Walone-Bold.ttf') format('truetype');
  font-weight: 700;
  font-style: normal;
  font-display: swap;
}

body {
  font-family: 'Walone', sans-serif;
}
```

### GitHub Pages / jsDelivr

Raw GitHub URL ကို သုံးနိုင်ပါသည်။ Public website တွင် long-term delivery အတွက် repository CDN/hosting configuration ကို project လိုအပ်ချက်အတိုင်း ရွေးချယ်ပါ။

---

## 📱 Android / Flutter / React

### Android

```
app/src/main/assets/fonts/
└── Walone-Regular.ttf
```

Android XML/Compose project တွင် project structure အလိုက် font resource ထည့်ပြီး အသုံးပြုနိုင်ပါသည်။

### Flutter

```yaml
flutter:
  fonts:
    - family: Walone
      fonts:
        - asset: fonts/Walone-Regular.ttf
          weight: 400
        - asset: fonts/Walone-Bold.ttf
          weight: 700
        - asset: fonts/Walone-Thin.ttf
          weight: 100
```

### React / CSS

```css
@font-face {
  font-family: 'Walone';
  src: url('/fonts/Walone-Regular.ttf') format('truetype');
  font-weight: 400;
}

.walone {
  font-family: 'Walone', sans-serif;
}
```

---

## 📄 EPUB

EPUB ထဲသို့ font file ကို embed လုပ်ပြီး CSS `@font-face` ဖြင့် reference လုပ်နိုင်ပါသည်။

```css
@font-face {
  font-family: 'Walone';
  src: url('../fonts/Walone-Regular.ttf');
  font-weight: 400;
}

body {
  font-family: 'Walone', serif;
}
```

EPUB ထုတ်လုပ်ရာတွင် font file ကို EPUB package ထဲသို့ ထည့်ရန် မမေ့ပါနှင့်။

---

## 📁 Folder Structure

```
myanmar-yoe-shin-fonts/
├── fonts/
│   ├── Walone-Thin.ttf
│   ├── Walone-Regular.ttf
│   ├── Walone-Bold.ttf
│   ├── A10_YoeShin-Regular.ttf
│   ├── A07_Yadanabon-Light.ttf
│   ├── A07_Yadanabon-Regular.ttf
│   ├── A07_Yadanabon-Bold.ttf
│   └── ... other Myanmar fonts
├── css/
│   ├── myanmar-fonts.css
│   └── inline-fonts.css
├── examples/
├── demo.html
└── README.md
```

---

## 🧪 Demo

Browser တွင် `demo.html` ကိုဖွင့်ပြီး font rendering ကို စမ်းသပ်နိုင်ပါသည်။

GitHub Pages ကို enable လုပ်ထားပါက repository ၏ Pages site မှတစ်ဆင့် demo ကို online ကြည့်နိုင်ပါသည်။

---

## ⚠️ Font Licensing

ဒီ repository ထဲရှိ font တစ်ခုချင်းစီ၏ copyright/license သည် မတူနိုင်ပါသည်။

- Repository ထဲရှိခြင်းသည် font အားလုံးကို commercial redistribution ခွင့်ရှိသည်ဟု မဆိုလိုပါ။
- မူရင်း font author / copyright holder ၏ license ကို စစ်ဆေးပြီးမှ commercial use သို့မဟုတ် redistribution ပြုလုပ်ပါ။
- Walone အပါအဝင် license မရှင်းလင်းသော third-party fonts များအတွက် မူရင်း rights holder ၏ permission/license ကို အတည်ပြုပါ။

---

## 🔗 Repository

**GitHub:** https://github.com/whispermmepub/myanmar-yoe-shin-fonts

---

## 💡 Quick Start

```bash
git clone https://github.com/whispermmepub/myanmar-yoe-shin-fonts.git
cd myanmar-yoe-shin-fonts
```

Web project အတွက်:

```html
<link rel="stylesheet"
      href="https://raw.githubusercontent.com/whispermmepub/myanmar-yoe-shin-fonts/main/css/myanmar-fonts.css">
```

---

*Myanmar Epub Community အတွက် စုစည်းထားသော font collection.*
