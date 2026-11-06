import re

svg_arrow_diag = '''<svg class="icon-arrow" viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="7" y1="17" x2="17" y2="7"/><polyline points="7 7 17 7 17 17"/></svg>'''
svg_arrow_down = '''<svg class="icon-arrow" viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="5" x2="12" y2="19"/><polyline points="19 12 12 19 5 12"/></svg>'''
svg_check = '''<svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>'''
svg_sparkle = '''<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m12 3-1.9 5.8a2 2 0 0 1-1.3 1.3L3 12l5.8 1.9a2 2 0 0 1 1.3 1.3L12 21l1.9-5.8a2 2 0 0 1 1.3-1.3L21 12l-5.8-1.9a2 2 0 0 1-1.3-1.3Z"/></svg>'''
svg_fire = '''<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.38-.5-2-1-3-1.072-2.143-.224-4.054 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.153.433-2.294 1-3a2.5 2.5 0 0 0 2.5 2.5z"/></svg>'''
svg_lantern = '''<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v20M2 7h20M5 7v10a7 7 0 0 0 14 0V7"/></svg>'''
svg_star_badge = '''<svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>'''
svg_clipboard = '''<svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><rect x="8" y="2" width="8" height="4" rx="1" ry="1"/><path d="M9 12h6"/><path d="M9 16h6"/></svg>'''

svg_wallet = '''<svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="2"/><line x1="2" y1="10" x2="22" y2="10"/><circle cx="18" cy="15" r="1.5"/></svg>'''
svg_coffee_lounge = '''<svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 8h1a4 4 0 0 1 0 8h-1"/><path d="M2 8h16v9a4 4 0 0 1-4 4H6a4 4 0 0 1-4-4V8z"/><line x1="6" y1="1" x2="6" y2="4"/><line x1="10" y1="1" x2="10" y2="4"/><line x1="14" y1="1" x2="14" y2="4"/></svg>'''
svg_utensils = '''<svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 2v20M2 12h8M12 2v20M20 2v6a2 2 0 0 1-2 2h-4a2 2 0 0 1-2-2V2M4 2v6a2 2 0 0 0 2 2h0a2 2 0 0 0 2-2V2"/></svg>'''

svg_scooter_small = '''<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="18.5" cy="17.5" r="3.5"/><circle cx="5.5" cy="17.5" r="3.5"/><path d="M15 6h4l2 5H9l2-5h4z"/><path d="M5.5 17.5 9 8h6l3.5 9.5"/></svg>'''
svg_scooter_lg = '''<svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="18.5" cy="17.5" r="3.5"/><circle cx="5.5" cy="17.5" r="3.5"/><path d="M15 6h4l2 5H9l2-5h4z"/><path d="M5.5 17.5 9 8h6l3.5 9.5"/><path d="M14 6V3H9"/></svg>'''
svg_shopping_bag = '''<svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 2 3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"/><line x1="3" y1="6" x2="21" y2="6"/><path d="M16 10a4 4 0 0 1-8 0"/></svg>'''
svg_package = '''<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/><polyline points="3.27 6.96 12 12.01 20.73 6.96"/><line x1="12" y1="22.08" x2="12" y2="12"/></svg>'''

svg_camera_badge = '''<svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"/><circle cx="8.5" cy="8.5" r="1.5"/><polyline points="21 15 16 10 5 21"/></svg>'''
svg_users = '''<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>'''

svg_zap = '''<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>'''
svg_leaf = '''<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.48 19 2c1 2 2 4.18 2 8 0 5.5-4.78 10-10 10Z"/><path d="M2 21c0-3 1.85-5.36 5.08-6C9.5 14.52 12 13 13 12"/></svg>'''
svg_parking = '''<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="3"/><path d="M9 17V7h4a3 3 0 0 1 0 6H9"/></svg>'''
svg_clock = '''<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>'''
svg_mappin = '''<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>'''

svg_whatsapp_filled = '''<svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z"/></svg>'''
svg_whatsapp_floating = '''<svg viewBox="0 0 24 24" width="30" height="30" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z"/></svg>'''

svg_instagram = '''<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"/></svg>'''
svg_tiktok = '''<svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M19.59 6.69a4.83 4.83 0 0 1-3.77-4.25V2h-3.45v13.67a2.89 2.89 0 0 1-5.2 1.74 2.89 2.89 0 0 1 2.31-4.64c.29 0 .58.04.85.12V9.41a6.33 6.33 0 0 0-.85-.06 6.34 6.34 0 0 0-6.34 6.34 6.34 6.34 0 0 0 8.79 5.86 6.33 6.33 0 0 0 3.89-5.86V8.71a8.18 8.18 0 0 0 4.77 1.52v-3.4a4.85 4.85 0 0 1-.99-.14z"/></svg>'''

svg_newspaper = '''<svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>'''
svg_feather = '''<svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg>'''
svg_calendar = '''<svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>'''
svg_clock_small = '''<svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>'''
svg_mappin_small = '''<svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>'''
svg_lightbulb = '''<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 18h6"/><path d="M10 22h4"/><path d="M15.09 14c.18-.98.65-1.74 1.41-2.5A4.65 4.65 0 0 0 18 8 6 6 0 0 0 6 8c0 1 .23 2.23 1.5 3.5.76.76 1.23 1.52 1.41 2.5"/></svg>'''

with open(r"D:\WarmindoPunakawan\index.html", "r", encoding="utf-8") as f:
    c = f.read()

# Fix broken filenames if any
c = c.replace('src="assets/images/menu-mie-rebus.jpeg"', 'src="assets/images/menu-mie-goreng.jpeg"')
c = c.replace('src="assets/images/ .jpeg"', 'src="assets/images/tempat-area-kasir.jpeg"')

# 1. Header CTA button
c = c.replace('Pesan Sekarang ↗', f'Pesan Sekarang {svg_arrow_diag}')

# 2. Hero Badge
c = c.replace('<span>🏮 KULINER RAKYAT &amp; WARMINDO NAIK KELAS DI COLOMADU</span>',
              f'<span class="icon-inline">{svg_lantern}</span><span>KULINER RAKYAT &amp; WARMINDO NAIK KELAS DI COLOMADU</span>')

# 3. Hero CTAs
c = c.replace('Lihat 9 Menu Best Seller ↓', f'Lihat 9 Menu Best Seller {svg_arrow_down}')
c = c.replace('Order via Aplikasi ↗', f'Order via Aplikasi {svg_arrow_diag}')

# 4. Trust badges
c = c.replace('<span class="check">✓</span>', f'<span class="check">{svg_check}</span>')

# 5. Floating badges on Hero
c = c.replace('✨ Semi-Outdoor Bambu &amp; Meja Kayu Cozy', f'<span class="icon-inline">{svg_sparkle}</span>Semi-Outdoor Bambu &amp; Meja Kayu Cozy')
c = c.replace('🔥 9 Menu BEST SELLER Pilihan!', f'<span class="icon-inline">{svg_fire}</span>9 Menu BEST SELLER Pilihan!')

# 6. Value Prop Section
c = c.replace('<span class="section-badge">✨ KEUNGGULAN UTAMA</span>', f'<span class="section-badge">{svg_star_badge} KEUNGGULAN UTAMA</span>')
c = c.replace('<div class="value-card-icon">💰</div>', f'<div class="value-card-icon">{svg_wallet}</div>')
c = c.replace('<div class="value-card-icon">🎋</div>', f'<div class="value-card-icon">{svg_coffee_lounge}</div>')
c = c.replace('<div class="value-card-icon">🍜</div>', f'<div class="value-card-icon">{svg_utensils}</div>')

# 7. Best seller section
c = c.replace('<span class="section-badge">🔥 REKOMENDASI TERPOPULER</span>', f'<span class="section-badge">{svg_fire} REKOMENDASI TERPOPULER</span>')
c = c.replace('>Pesan ↗</a>', f'>Pesan {svg_arrow_diag}</a>')

# 8. Daftar Harga section
c = c.replace('<span class="section-badge badge-gold">📋 DAFTAR HARGA RESMI</span>', f'<span class="section-badge badge-gold">{svg_clipboard} DAFTAR HARGA RESMI</span>')

# 9. Order Section
c = c.replace('<span class="section-badge">🛵 TERSEDIA 3 OPSI MERCHANT: GOFOOD, SHOPEEFOOD &amp; GRABFOOD</span>',
              f'<span class="section-badge">{svg_scooter_small} TERSEDIA 3 OPSI MERCHANT: GOFOOD, SHOPEEFOOD &amp; GRABFOOD</span>')
c = c.replace('<span>🍽️</span>', svg_utensils)
c = c.replace('<span>🛍️</span>', svg_shopping_bag)
c = c.replace('<span>🛵</span>', svg_scooter_lg)
c = c.replace('Buka GoFood Sekarang ↗', f'Buka GoFood Sekarang {svg_arrow_diag}')
c = c.replace('Buka ShopeeFood Sekarang ↗', f'Buka ShopeeFood Sekarang {svg_arrow_diag}')
c = c.replace('Buka GrabFood Sekarang ↗', f'Buka GrabFood Sekarang {svg_arrow_diag}')
c = c.replace('🍱 Mau pesan Take Away', f'<span class="icon-inline">{svg_package}</span>Mau pesan Take Away')
c = c.replace('Pesan &amp; Reservasi via WhatsApp (0896-5355-7758) ↗',
              f'<span class="icon-inline">{svg_whatsapp_filled}</span>Pesan &amp; Reservasi via WhatsApp (0896-5355-7758) {svg_arrow_diag}')

# 10. Suasana Section
c = c.replace('<span class="section-badge">🎋 SUASANA &amp; BOOKING</span>', f'<span class="section-badge">{svg_camera_badge} SUASANA &amp; BOOKING</span>')
c = c.replace('<span class="venue-floating-badge">✨ Semi-Outdoor Bambu &amp; Meja Kayu</span>',
              f'<span class="venue-floating-badge"><span class="icon-inline">{svg_sparkle}</span>Semi-Outdoor Bambu &amp; Meja Kayu</span>')
c = c.replace('<span class="venue-floating-badge">👥 Kapasitas Luas untuk Komunitas</span>',
              f'<span class="venue-floating-badge"><span class="icon-inline">{svg_users}</span>Kapasitas Luas untuk Komunitas</span>')

c = c.replace('<span class="icon">⚡</span>', f'<span class="icon">{svg_zap}</span>')
c = c.replace('<span class="icon">🍃</span>', f'<span class="icon">{svg_leaf}</span>')
c = c.replace('<span class="icon">🛵</span>', f'<span class="icon">{svg_parking}</span>')
c = c.replace('<span class="icon">🕒</span>', f'<span class="icon">{svg_clock}</span>')
c = c.replace('<span class="icon">📍</span>', f'<span class="icon">{svg_mappin}</span>')

c = c.replace('💬 <strong>WhatsApp:</strong> 0896 5355 7758',
              f'<span class="icon-inline">{svg_whatsapp_filled}</span><strong>WhatsApp:</strong> 0896 5355 7758')
c = c.replace('📸 <strong>Instagram &amp; TikTok:</strong> @punakawanspaceeatery',
              f'<span class="icon-inline">{svg_instagram}</span><span class="icon-inline">{svg_tiktok}</span><strong>Instagram &amp; TikTok:</strong> @punakawanspaceeatery')

c = c.replace('Kirim Reservasi ke WhatsApp (0896-5355-7758) ↗',
              f'<span class="icon-inline">{svg_whatsapp_filled}</span>Kirim Reservasi ke WhatsApp (0896-5355-7758) {svg_arrow_diag}')

# 11. Article Section
c = c.replace('<span class="section-badge">📰 CONTENT MARKETING &amp; EDUKASI KULINER</span>',
              f'<span class="section-badge">{svg_newspaper} CONTENT MARKETING &amp; EDUKASI KULINER</span>')
c = c.replace('<span>✍️ Ditulis oleh Tim Publikasi Punakawan</span>',
              f'<span><span class="icon-inline">{svg_feather}</span>Ditulis oleh Tim Publikasi Punakawan</span>')
c = c.replace('<span>📅 Update Terkini</span>',
              f'<span><span class="icon-inline">{svg_calendar}</span>Update Terkini</span>')
c = c.replace('<span>⏱️ 4 Menit Baca</span>',
              f'<span><span class="icon-inline">{svg_clock_small}</span>4 Menit Baca</span>')
c = c.replace('<span>📍 Colomadu, Solo Raya</span>',
              f'<span><span class="icon-inline">{svg_mappin_small}</span>Colomadu, Solo Raya</span>')
c = c.replace('💡 <em>"Di Punakawan', f'<span class="icon-inline">{svg_lightbulb}</span><em>"Di Punakawan')

# 12. Footer
c = c.replace('📍 Colomadu, Kabupaten Karanganyar', f'<span class="icon-inline">{svg_mappin_small}</span>Colomadu, Kabupaten Karanganyar')

footer_links_old = '''        <!-- Kolom 3: Saluran Pemesanan Resmi -->
        <div class="footer-col">
          <h4 class="footer-col-title">Saluran Pemesanan</h4>
          <ul class="footer-links">
            <li><a href="https://gofood.co.id/" target="_blank" rel="noopener noreferrer" class="footer-link">GoFood Delivery ↗</a></li>
            <li><a href="https://shopee.co.id/m/shopeefood" target="_blank" rel="noopener noreferrer" class="footer-link">ShopeeFood Promo ↗</a></li>
            <li><a href="https://food.grab.com/id/id/" target="_blank" rel="noopener noreferrer" class="footer-link">GrabFood Order ↗</a></li>
            <li><a href="https://wa.me/6289653557758" target="_blank" rel="noopener noreferrer" class="footer-link">WhatsApp: 0896 5355 7758 ↗</a></li>
            <li><span class="footer-link">Instagram: @punakawanspaceeatery</span></li>
            <li><span class="footer-link">TikTok: @punakawanspaceeatery</span></li>
          </ul>
        </div>

      <!-- Bottom Bar -->'''

footer_links_new = f'''        <!-- Kolom 3: Saluran Pemesanan Resmi -->
        <div class="footer-col">
          <h4 class="footer-col-title">Saluran Pemesanan</h4>
          <ul class="footer-links">
            <li><a href="https://gofood.co.id/" target="_blank" rel="noopener noreferrer" class="footer-link">GoFood Delivery {svg_arrow_diag}</a></li>
            <li><a href="https://shopee.co.id/m/shopeefood" target="_blank" rel="noopener noreferrer" class="footer-link">ShopeeFood Promo {svg_arrow_diag}</a></li>
            <li><a href="https://food.grab.com/id/id/" target="_blank" rel="noopener noreferrer" class="footer-link">GrabFood Order {svg_arrow_diag}</a></li>
            <li><a href="https://wa.me/6289653557758" target="_blank" rel="noopener noreferrer" class="footer-link"><span class="icon-inline">{svg_whatsapp_filled}</span>WhatsApp: 0896 5355 7758 {svg_arrow_diag}</a></li>
            <li><a href="https://instagram.com/punakawanspaceeatery" target="_blank" rel="noopener noreferrer" class="footer-link"><span class="icon-inline">{svg_instagram}</span>Instagram: @punakawanspaceeatery</a></li>
            <li><a href="https://tiktok.com/@punakawanspaceeatery" target="_blank" rel="noopener noreferrer" class="footer-link"><span class="icon-inline">{svg_tiktok}</span>TikTok: @punakawanspaceeatery</a></li>
          </ul>
        </div>

        <!-- Kolom 4: Identitas Proyek Akademik (UAS Digital Marketing) -->
        <div class="footer-col">
          <div class="academic-badge-box">
            <h5>Mata Kuliah: Digital Marketing (UAS)</h5>
            <p><strong>Dosen Pengampu:</strong> Ibu Nurul Sutarti</p>
            <p><strong>Topik Pilihan:</strong> Topik 3 – SEO &amp; Content Marketing untuk Website Portofolio/Katalog</p>
            <div class="team-members-list">
              <div>• <strong>Anugrah Adiantoro</strong> (B220231008)</div>
              <div>• <strong>Andri Tri Wijayanto</strong> (B220231007)</div>
              <div>• <strong>Abraham Theo</strong> (B220231041)</div>
              <div>• <strong>Samuel Kristawan</strong> (B220231030)</div>
            </div>
          </div>
        </div>
      </div>

      <!-- Bottom Bar -->'''

c = c.replace(footer_links_old, footer_links_new)

# 13. Floating WhatsApp button
c = c.replace('''  <!-- Floating Quick WhatsApp Button -->
  <a href="https://wa.me/6289653557758?text=Halo%20Punakawan%20Space%20%26%20Eatery,%20saya%20ingin%20tanya%20menu%20/%20reservasi." 
     target="_blank" 
     rel="noopener noreferrer" 
     class="floating-wa-btn" 
     aria-label="Chat WhatsApp Resmi Punakawan">
    💬
  </a>''',
  f'''  <!-- Floating Quick WhatsApp Button -->
  <a href="https://wa.me/6289653557758?text=Halo%20Punakawan%20Space%20%26%20Eatery,%20saya%20ingin%20tanya%20menu%20/%20reservasi." 
     target="_blank" 
     rel="noopener noreferrer" 
     class="floating-wa-btn" 
     aria-label="Chat WhatsApp Resmi Punakawan">
    {svg_whatsapp_floating}
  </a>''')

with open(r"D:\WarmindoPunakawan\index.html", "w", encoding="utf-8") as f:
    f.write(c)

print("Updated index.html successfully with Figma-style SVG icons!")

