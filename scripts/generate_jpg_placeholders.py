import os
from PIL import Image, ImageDraw, ImageFont

target_dir = os.path.join(os.path.dirname(__file__), '..', 'assets', 'images')
os.makedirs(target_dir, exist_ok=True)

# 9 Best Seller menus (3:4 ratio -> 600 x 800)
menus = [
    {
        "filename": "menu-mie-goreng.jpg",
        "category": "MAKANAN (1/3)",
        "title": "Mie Goreng Spesial Punakawan",
        "desc": "Mie rempah, telur ceplok, sosis, suwiran ayam, ati ampela",
        "price": "Rp 12.000",
        "tag": "BEST SELLER",
        "symbol": "[ MIE GORENG SPESIAL ]"
    },
    {
        "filename": "menu-nasi-goreng.jpg",
        "category": "MAKANAN (2/3)",
        "title": "Nasi Goreng Spesial Punakawan",
        "desc": "Nasi goreng rempah Jawa, telur, kerupuk, timun & tomat",
        "price": "Rp 13.000",
        "tag": "BEST SELLER",
        "symbol": "[ NASI GORENG JAWA ]"
    },
    {
        "filename": "menu-spagheti.jpg",
        "category": "MAKANAN (3/3)",
        "title": "Spagheti (Carbonara & Bolognese)",
        "desc": "Spagheti hangat saus gurih dengan sosis & taburan keju",
        "price": "Rp 15.000",
        "tag": "BEST SELLER",
        "symbol": "[ SPAGHETI SAUS KEJU ]"
    },
    {
        "filename": "menu-wedang-punakawan.jpg",
        "category": "MINUMAN (1/3)",
        "title": "Wedang Punakawan (Rempah Asli)",
        "desc": "Jahe geprek bakar, serai wangi, jeruk nipis segar",
        "price": "Rp 10.000",
        "tag": "BEST SELLER",
        "symbol": "[ WEDANG REMPAH ASLI ]"
    },
    {
        "filename": "menu-es-teh-tarik.jpg",
        "category": "MINUMAN (2/3)",
        "title": "Es Teh Tarik Spesial",
        "desc": "Teh wangi khas Solo ditarik dengan susu kental gurih",
        "price": "Rp 5.000",
        "tag": "BEST SELLER",
        "symbol": "[ ES TEH TARIK SOLO ]"
    },
    {
        "filename": "menu-badak-es.jpg",
        "category": "MINUMAN (3/3)",
        "title": "Badak + Es Batu (Sarsaparilla)",
        "desc": "Soda Cap Badak legendaris dingin es batu kristal",
        "price": "Rp 17.000",
        "tag": "BEST SELLER",
        "symbol": "[ SODA CAP BADAK ]"
    },
    {
        "filename": "menu-wonton-basah.jpg",
        "category": "SNACK (1/3)",
        "title": "Wonton Basah Kuah Pedas",
        "desc": "Pangsit ayam lembut kuah chili oil pedas gurih & pakcoy",
        "price": "Rp 12.000",
        "tag": "BEST SELLER",
        "symbol": "[ WONTON KUAH PEDAS ]"
    },
    {
        "filename": "menu-pisang-goreng.jpg",
        "category": "SNACK (2/3)",
        "title": "Pisang Goreng Punakawan",
        "desc": "Pisang crispy spesial topping coklat & keju parut",
        "price": "Rp 10.000",
        "tag": "BEST SELLER",
        "symbol": "[ PISANG CRISPY COKLAT KEJU ]"
    },
    {
        "filename": "menu-kentang-goreng.jpg",
        "category": "SNACK (3/3)",
        "title": "Kentang Goreng Crispy",
        "desc": "Kentang renyah gurih disajikan hangat saus cocolan",
        "price": "Rp 8.000",
        "tag": "BEST SELLER",
        "symbol": "[ KENTANG GORENG RENYAH ]"
    }
]

# Color palette (Warm Heritage)
C_TEAL = (30, 63, 71)        # #1E3F47
C_DARK_TEAL = (18, 38, 43)   # #12262B
C_GOLD = (212, 168, 87)      # #D4A857
C_CREAM = (244, 239, 230)    # #F4EFE6
C_YELLOW = (255, 204, 0)     # #FFCC00
C_BLACK = (17, 17, 17)       # #111111

def draw_dashed_rect(draw, bbox, color, dash_len=8, space_len=6, width=2):
    x0, y0, x1, y1 = bbox
    # top & bottom
    for x in range(x0, x1, dash_len + space_len):
        draw.line([(x, y0), (min(x + dash_len, x1), y0)], fill=color, width=width)
        draw.line([(x, y1), (min(x + dash_len, x1), y1)], fill=color, width=width)
    # left & right
    for y in range(y0, y1, dash_len + space_len):
        draw.line([(x0, y), (x0, min(y + dash_len, y1))], fill=color, width=width)
        draw.line([(x1, y), (x1, min(y + dash_len, y1))], fill=color, width=width)

for m in menus:
    w, h = 600, 800
    img = Image.new('RGB', (w, h), C_TEAL)
    draw = ImageDraw.Draw(img)

    # Gradient-like inner block
    draw.rectangle([20, 20, w-20, h-20], fill=C_DARK_TEAL)
    draw_dashed_rect(draw, [25, 25, w-25, h-25], C_GOLD, dash_len=10, space_len=6, width=3)

    # Category badge top-left
    draw.rectangle([45, 45, 230, 85], fill=C_TEAL, outline=C_GOLD, width=2)
    draw.text((60, 55), m["category"], fill=C_GOLD)

    # Best Seller ribbon top-right
    draw.rectangle([w-210, 45, w-45, 85], fill=C_YELLOW)
    draw.text((w-185, 55), m["tag"], fill=C_BLACK)

    # Central emblem
    draw.ellipse([w//2 - 140, h//2 - 180, w//2 + 140, h//2 + 100], fill=C_TEAL, outline=C_GOLD, width=3)
    draw.ellipse([w//2 - 120, h//2 - 160, w//2 + 120, h//2 + 80], fill=C_DARK_TEAL, outline=C_CREAM, width=1)
    
    # Text emblem
    draw.text((w//2 - 100, h//2 - 60), m["symbol"], fill=C_YELLOW)
    draw.text((w//2 - 95, h//2 - 20), "PUNAKAWAN EATERY", fill=C_GOLD)
    draw.text((w//2 - 80, h//2 + 15), "Slot Kosong Terstruktur (3:4)", fill=C_CREAM)

    # Menu Title
    draw.text((45, h - 230), m["title"], fill=C_CREAM)
    draw.line([(45, h - 200), (w - 45, h - 200)], fill=C_GOLD, width=2)

    # Description
    draw.text((45, h - 180), m["desc"], fill=(194, 209, 212))

    # Price Tag & Filename
    draw.rectangle([45, h - 130, 250, h - 65], fill=C_YELLOW)
    draw.text((70, h - 110), m["price"], fill=C_BLACK)

    draw.text((280, h - 105), f"Aset: {m['filename']}", fill=C_GOLD)

    out_path = os.path.join(target_dir, m["filename"])
    img.save(out_path, "JPEG", quality=92)

# 2 Venue Images (4:3 ratio -> 800 x 600)
venues = [
    {
        "filename": "tempat-bambu-malam.jpg",
        "title": "Area Semi-Outdoor Atap Bambu & Meja Kayu",
        "badge": "✨ Semi-Outdoor Bambu & Meja Kayu Cozy",
        "subtitle": "Suasana Malam Asri, Adem & Tenang di Colomadu",
        "desc": "Anyaman bambu tradisional Solo Raya dengan sirkulasi terbuka dan penerangan hangat."
    },
    {
        "filename": "tempat-area-kasir.jpg",
        "title": "Area Kasir & Meja Rombongan Komunitas",
        "badge": "👥 Kapasitas Luas untuk Komunitas & Bukber",
        "subtitle": "Tempat Nongkrong Bersahabat Dekat Kampus UMS",
        "desc": "Kapasitas meja luas untuk nugas bareng, rapat komunitas, hingga kumpul santai keluarga."
    }
]

for v in venues:
    w, h = 800, 600
    img = Image.new('RGB', (w, h), C_TEAL)
    draw = ImageDraw.Draw(img)

    draw.rectangle([25, 25, w-25, h-25], fill=C_DARK_TEAL)
    draw_dashed_rect(draw, [30, 30, w-30, h-30], C_GOLD, dash_len=12, space_len=8, width=3)

    # Floating badge top left
    draw.rectangle([50, 50, 480, 100], fill=C_TEAL, outline=C_GOLD, width=2)
    draw.text((70, 68), v["badge"], fill=C_YELLOW)

    # Center emblem
    draw.ellipse([w//2 - 160, h//2 - 130, w//2 + 160, h//2 + 90], fill=C_TEAL, outline=C_GOLD, width=3)
    draw.text((w//2 - 110, h//2 - 40), "[ PUNAKAWAN SPACE ]", fill=C_YELLOW)
    draw.text((w//2 - 100, h//2 - 5), "Colomadu - Karanganyar", fill=C_GOLD)
    draw.text((w//2 - 120, h//2 + 30), "Clean Structured Placeholder", fill=C_CREAM)

    # Venue title & desc bottom
    draw.rectangle([50, h - 160, w - 50, h - 50], fill=C_TEAL, outline=C_GOLD, width=1)
    draw.text((70, h - 145), v["title"], fill=C_CREAM)
    draw.text((70, h - 115), v["subtitle"], fill=C_GOLD)
    draw.text((70, h - 85), f"File Target: {v['filename']} | {v['desc']}", fill=(194, 209, 212))

    out_path = os.path.join(target_dir, v["filename"])
    img.save(out_path, "JPEG", quality=92)

print("All 11 JPG images successfully generated in assets/images/!")

