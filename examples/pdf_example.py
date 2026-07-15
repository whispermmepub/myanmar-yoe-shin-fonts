"""
Myanmar Font PDF Example - မြန်မာဖွန့်ဖြင့် PDF ဖန်တီးနည်း
Requires: pip install fpdf2
"""
from fpdf import FPDF

class MyanmarPDF(FPDF):
    def __init__(self):
        super().__init__()
        # Font files တွေထည့်
        self.add_font('YoeShin', '', '../fonts/A10_YoeShin-Regular.ttf')
        self.add_font('Burma026', '', '../fonts/Burma026-Regular.ttf')
        self.add_font('PuPu', '', '../fonts/M01_PuPu Bold.ttf')
        self.add_font('Myittar', '', '../fonts/M03_Myittar-Regular.ttf')
        self.add_font('MyanmarAyar', '', '../fonts/MyanmarAyarTyepwriter.ttf')

pdf = MyanmarPDF()
pdf.add_page()

# YoeShin font
pdf.set_font('YoeShin', '', 16)
pdf.cell(0, 12, 'ယိုးရှင် ဖွန့် - Whisper Of Words', ln=True)
pdf.set_font('YoeShin', '', 12)
pdf.multi_cell(0, 8, 'မြန်မာစာအုပ်များကို epub/kfx format ဖြင့် အခမဲ့ဖြန့်ဝေပါသည်။')

pdf.ln(10)

# PuPu Bold
pdf.set_font('PuPu', '', 14)
pdf.cell(0, 10, 'PuPu Bold - ဘာသာပြန်စာအုပ်များ', ln=True)
pdf.set_font('PuPu', '', 10)
pdf.multi_cell(0, 8, 'သင့်ဖုန်းတွင် epub reader app ဖြင့် ဖတ်ရှုနိုင်ပါသည်။ အွန်လိုင်းမှ အခမဲ့ download ရယူနိုင်ပါသည်။')

pdf.ln(10)

# Myanmar Ayar
pdf.set_font('MyanmarAyar', '', 14)
pdf.cell(0, 10, 'Ayar Typewriter - စာတိုက်ပုံ', ln=True)
pdf.set_font('MyanmarAyar', '', 10)
pdf.multi_cell(0, 8, 'Myanmar Ayar font ဖြင့် typewriter style စာရေးနည်း')

pdf.output('myanmar_fonts_demo.pdf')
print('PDF created: myanmar_fonts_demo.pdf')
