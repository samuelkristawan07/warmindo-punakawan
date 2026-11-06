const fs = require('fs');
const path = require('path');

const targetDir = path.join(__dirname, '..', 'assets', 'images');
if (!fs.existsSync(targetDir)) {
  fs.mkdirSync(targetDir, { recursive: true });
}

const items = [
  {
    filename: 'menu-mie-goreng.svg',
    category: 'MAKANAN',
    title: 'Mie Goreng Spesial',
    subtitle: 'Punakawan',
    price: 'Rp 12.000',
    icon: '🍜',
    accent: '#E65100',
    bg1: '#1E3F47',
    bg2: '#13282D',
    details: 'Telur Ceplok • Sosis • Suwiran Ayam • Ati Ampela'
  },
  {
    filename: 'menu-nasi-goreng.svg',
    category: 'MAKANAN',
    title: 'Nasi Goreng Spesial',
    subtitle: 'Punakawan',
    price: 'Rp 13.000',
    icon: '🍳',
    accent: '#D4A857',
    bg1: '#1E3F47',
    bg2: '#182C31',
    details: 'Rempah Khas Jawa • Kerupuk • Timun & Tomat'
  },
  {
    filename: 'menu-spagheti.svg',
    category: 'MAKANAN',
    title: 'Spagheti Warmindo',
    subtitle: 'Carbonara & Bolognese',
    price: 'Rp 15.000',
    icon: '🍝',
    accent: '#E53935',
    bg1: '#1E3F47',
    bg2: '#162F35',
    details: 'Sosis Sapi • Taburan Keju Gurih Melimpah'
  },
  {
    filename: 'menu-wedang-punakawan.svg',
    category: 'MINUMAN',
    title: 'Wedang Punakawan',
    subtitle: 'Rempah Asli Solo',
    price: 'Rp 10.000',
    icon: '🫖',
    accent: '#FFA726',
    bg1: '#1E3F47',
    bg2: '#14292E',
    details: 'Jahe Geprek Bakar • Serai Wangi • Jeruk Nipis'
  },
  {
    filename: 'menu-es-teh-tarik.svg',
    category: 'MINUMAN',
    title: 'Es Teh Tarik',
    subtitle: 'Spesial Berbusa',
    price: 'Rp 5.000',
    icon: '🧋',
    accent: '#D4A857',
    bg1: '#1E3F47',
    bg2: '#183036',
    details: 'Teh Wangi Khas Solo • Susu Kental Gurih'
  },
  {
    filename: 'menu-badak-es.svg',
    category: 'MINUMAN',
    title: 'Badak + Es Batu',
    subtitle: 'Sarsaparilla Legendaris',
    price: 'Rp 17.000',
    icon: '🧊',
    accent: '#26C6DA',
    bg1: '#1E3F47',
    bg2: '#12262B',
    details: 'Soda Cap Badak Dingin • Sensasi Klasik Segar'
  },
  {
    filename: 'menu-wonton-basah.svg',
    category: 'SNACK',
    title: 'Wonton Basah Pedas',
    subtitle: 'Kuah Chili Oil Gurih',
    price: 'Rp 12.000',
    icon: '🥟',
    accent: '#EF5350',
    bg1: '#1E3F47',
    bg2: '#1B2C30',
    details: 'Pangsit Ayam Lembut • Pakcoy • Pangsit Renyah'
  },
  {
    filename: 'menu-pisang-goreng.svg',
    category: 'SNACK',
    title: 'Pisang Goreng Punakawan',
    subtitle: 'Crispy Coklat Keju',
    price: 'Rp 10.000',
    icon: '🍌',
    accent: '#FDD835',
    bg1: '#1E3F47',
    bg2: '#162F34',
    details: 'Pisang Crispy Renyah • Lelehan Coklat & Keju'
  },
  {
    filename: 'menu-kentang-goreng.svg',
    category: 'SNACK',
    title: 'Kentang Goreng Crispy',
    subtitle: 'Saus Cocolan Gurih',
    price: 'Rp 8.000',
    icon: '🍟',
    accent: '#FFB300',
    bg1: '#1E3F47',
    bg2: '#182C31',
    details: 'Kentang Renyah Gurih • Saus Sambal & Saus Tomat'
  }
];

// Generate 3:4 aspect ratio cards (300 x 400)
items.forEach(item => {
  const svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 400" width="300" height="400">
  <defs>
    <linearGradient id="bg-${item.filename}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="${item.bg1}" />
      <stop offset="100%" stop-color="${item.bg2}" />
    </linearGradient>
    <radialGradient id="glow-${item.filename}" cx="50%" cy="40%" r="50%">
      <stop offset="0%" stop-color="${item.accent}" stop-opacity="0.35"/>
      <stop offset="100%" stop-color="${item.accent}" stop-opacity="0"/>
    </radialGradient>
  </defs>

  <!-- Background Card -->
  <rect width="300" height="400" fill="url(#bg-${item.filename})" rx="16"/>
  <circle cx="150" cy="160" r="110" fill="url(#glow-${item.filename})"/>

  <!-- Heritage Border Accent -->
  <rect x="10" y="10" width="280" height="380" fill="none" stroke="#D4A857" stroke-width="1.5" stroke-dasharray="4,3" rx="12" opacity="0.6"/>

  <!-- Category Pill -->
  <g transform="translate(24, 28)">
    <rect width="90" height="24" rx="12" fill="#D4A857" fill-opacity="0.2"/>
    <text x="45" y="16" fill="#D4A857" font-size="11" font-weight="700" font-family="'Plus Jakarta Sans', sans-serif" text-anchor="middle" letter-spacing="1">${item.category}</text>
  </g>

  <!-- Icon Illustration Circle -->
  <circle cx="150" cy="155" r="62" fill="#152B30" stroke="#D4A857" stroke-width="2"/>
  <circle cx="150" cy="155" r="54" fill="#1C383F"/>
  <text x="150" y="172" font-size="52" text-anchor="middle">${item.icon}</text>

  <!-- Title & Subtitle -->
  <text x="150" y="252" fill="#F4EFE6" font-size="18" font-weight="700" font-family="'Plus Jakarta Sans', sans-serif" text-anchor="middle">${item.title}</text>
  <text x="150" y="274" fill="#D4A857" font-size="13" font-weight="500" font-family="'Plus Jakarta Sans', sans-serif" text-anchor="middle">${item.subtitle}</text>

  <!-- Decorative Separator -->
  <line x1="80" y1="292" x2="220" y2="292" stroke="#D4A857" stroke-width="1" opacity="0.3"/>
  <polygon points="150,290 153,292 150,294 147,292" fill="#D4A857"/>

  <!-- Details text -->
  <text x="150" y="316" fill="#C2D1D4" font-size="11" font-family="'Plus Jakarta Sans', sans-serif" text-anchor="middle">${item.details}</text>

  <!-- Price Badge -->
  <g transform="translate(75, 340)">
    <rect width="150" height="34" rx="17" fill="#FFCC00"/>
    <text x="75" y="22" fill="#111111" font-size="15" font-weight="800" font-family="'Plus Jakarta Sans', sans-serif" text-anchor="middle">${item.price}</text>
  </g>
</svg>`;

  fs.writeFileSync(path.join(targetDir, item.filename), svg);
});

// Generate Venue 1: tempat-bambu-malam.svg
const venue1 = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 450" width="600" height="450">
  <defs>
    <linearGradient id="v1-sky" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0E1D21"/>
      <stop offset="70%" stop-color="#1B3940"/>
      <stop offset="100%" stop-color="#264D56"/>
    </linearGradient>
    <linearGradient id="warm-light" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#FFDD77" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#D4A857" stop-opacity="0"/>
    </linearGradient>
    <pattern id="bamboo-roof" width="20" height="40" patternUnits="userSpaceOnUse">
      <line x1="0" y1="0" x2="20" y2="40" stroke="#7A562B" stroke-width="2"/>
      <line x1="20" y1="0" x2="0" y2="40" stroke="#5E401E" stroke-width="2"/>
    </pattern>
  </defs>

  <!-- Night Sky & Base -->
  <rect width="600" height="450" fill="url(#v1-sky)"/>

  <!-- Stars / Ambient night glow -->
  <circle cx="100" cy="50" r="1.5" fill="#FFEAA7" opacity="0.6"/>
  <circle cx="220" cy="80" r="1" fill="#FFEAA7" opacity="0.5"/>
  <circle cx="480" cy="60" r="1.5" fill="#FFEAA7" opacity="0.7"/>
  <circle cx="530" cy="110" r="1" fill="#FFEAA7" opacity="0.4"/>

  <!-- Bamboo Roof Structure -->
  <polygon points="50,110 300,30 550,110 570,140 30,140" fill="#4B331A" stroke="#2D1E0E" stroke-width="3"/>
  <polygon points="60,115 300,45 540,115 555,135 45,135" fill="url(#bamboo-roof)" opacity="0.8"/>

  <!-- Wooden Pillars -->
  <rect x="75" y="140" width="18" height="240" fill="#5D3E1F" stroke="#3A2510" stroke-width="2"/>
  <rect x="291" y="140" width="18" height="240" fill="#5D3E1F" stroke="#3A2510" stroke-width="2"/>
  <rect x="507" y="140" width="18" height="240" fill="#5D3E1F" stroke="#3A2510" stroke-width="2"/>

  <!-- Warm Hanging Bamboo Lanterns -->
  <g transform="translate(180, 140)">
    <line x1="0" y1="0" x2="0" y2="35" stroke="#222" stroke-width="2"/>
    <ellipse cx="0" cy="50" rx="16" ry="18" fill="#FFC837"/>
    <ellipse cx="0" cy="50" rx="28" ry="30" fill="url(#warm-light)"/>
  </g>
  <g transform="translate(420, 140)">
    <line x1="0" y1="0" x2="0" y2="35" stroke="#222" stroke-width="2"/>
    <ellipse cx="0" cy="50" rx="16" ry="18" fill="#FFC837"/>
    <ellipse cx="0" cy="50" rx="28" ry="30" fill="url(#warm-light)"/>
  </g>

  <!-- Cozy Wooden Hangout Tables -->
  <polygon points="90,320 250,320 270,360 70,360" fill="#7C5028" stroke="#4D3014" stroke-width="2"/>
  <polygon points="340,320 510,320 530,360 320,360" fill="#7C5028" stroke="#4D3014" stroke-width="2"/>

  <!-- Flooring Deck -->
  <polygon points="0,380 600,380 600,450 0,450" fill="#2E1C0C"/>
  <line x1="0" y1="410" x2="600" y2="410" stroke="#3F2712" stroke-width="2"/>

  <!-- Heritage Border & Watermark -->
  <rect x="15" y="15" width="570" height="420" fill="none" stroke="#D4A857" stroke-width="2" stroke-dasharray="6,4" rx="8" opacity="0.7"/>

  <!-- Information Overlay Badge -->
  <g transform="translate(30, 390)">
    <rect width="540" height="38" rx="8" fill="#1E3F47" fill-opacity="0.9" stroke="#D4A857" stroke-width="1"/>
    <text x="270" y="24" fill="#F4EFE6" font-size="13" font-weight="700" font-family="'Plus Jakarta Sans', sans-serif" text-anchor="middle">
      🏮 Area Semi-Outdoor Atap Anyaman Bambu &amp; Meja Kayu Hangat (Colomadu)
    </text>
  </g>
</svg>`;
fs.writeFileSync(path.join(targetDir, 'tempat-bambu-malam.svg'), venue1);

// Generate Venue 2: tempat-area-kasir.svg
const venue2 = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 450" width="600" height="450">
  <defs>
    <linearGradient id="v2-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1E3F47"/>
      <stop offset="100%" stop-color="#10252A"/>
    </linearGradient>
    <linearGradient id="gold-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#F3E7BE"/>
      <stop offset="50%" stop-color="#D4A857"/>
      <stop offset="100%" stop-color="#9C7227"/>
    </linearGradient>
  </defs>

  <rect width="600" height="450" fill="url(#v2-bg)"/>

  <!-- Modern Kasir Counter -->
  <polygon points="120,220 480,220 520,380 80,380" fill="#3D2915" stroke="#5D3E1F" stroke-width="3"/>
  <rect x="140" y="235" width="320" height="130" fill="#1C383F" rx="8" stroke="url(#gold-grad)" stroke-width="2"/>

  <!-- POS Terminal & Order Display -->
  <rect x="260" y="170" width="80" height="50" rx="4" fill="#0E1E22" stroke="#D4A857" stroke-width="1.5"/>
  <line x1="300" y1="220" x2="300" y2="235" stroke="#D4A857" stroke-width="3"/>
  <rect x="280" y="233" width="40" height="4" fill="#D4A857"/>
  <text x="300" y="198" fill="#00E676" font-size="12" font-family="monospace" text-anchor="middle">PUNAKAWAN</text>

  <!-- Big Menu Boards behind cashier -->
  <rect x="100" y="50" width="115" height="100" fill="#152B30" stroke="#D4A857" stroke-width="1.5" rx="6"/>
  <text x="157" y="72" fill="#D4A857" font-size="10" font-weight="700" text-anchor="middle">MENU PAKET</text>
  <line x1="110" y1="80" x2="205" y2="80" stroke="#D4A857" stroke-width="0.5"/>

  <rect x="242" y="50" width="115" height="100" fill="#152B30" stroke="#D4A857" stroke-width="1.5" rx="6"/>
  <text x="300" y="72" fill="#D4A857" font-size="10" font-weight="700" text-anchor="middle">SNACK</text>
  <line x1="252" y1="80" x2="347" y2="80" stroke="#D4A857" stroke-width="0.5"/>

  <rect x="385" y="50" width="115" height="100" fill="#152B30" stroke="#D4A857" stroke-width="1.5" rx="6"/>
  <text x="442" y="72" fill="#D4A857" font-size="10" font-weight="700" text-anchor="middle">MINUMAN</text>
  <line x1="395" y1="80" x2="490" y2="80" stroke="#D4A857" stroke-width="0.5"/>

  <!-- Community Long Tables on foreground -->
  <polygon points="40,390 560,390 600,450 0,450" fill="#2A1B0E" stroke="#5D3E1F" stroke-width="2"/>

  <!-- Heritage Border -->
  <rect x="15" y="15" width="570" height="420" fill="none" stroke="#D4A857" stroke-width="2" stroke-dasharray="6,4" rx="8" opacity="0.7"/>

  <!-- Information Overlay Badge -->
  <g transform="translate(30, 390)">
    <rect width="540" height="38" rx="8" fill="#1E3F47" fill-opacity="0.95" stroke="#D4A857" stroke-width="1"/>
    <text x="270" y="24" fill="#F4EFE6" font-size="13" font-weight="700" font-family="'Plus Jakarta Sans', sans-serif" text-anchor="middle">
      👥 Area Kasir Ramah &amp; Kapasitas Meja Luas Rombongan Komunitas
    </text>
  </g>
</svg>`;
fs.writeFileSync(path.join(targetDir, 'tempat-area-kasir.svg'), venue2);

console.log('All 11 asset SVGs successfully generated in assets/images/');

