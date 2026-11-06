/**
 * PUNAKAWAN SPACE & EATERY - OFFICIAL JAVASCRIPT
 * Mengatur interaktivitas: Filter 9 Menu Best Seller, Form Reservasi WhatsApp, Navigasi Mobile, & Tracking
 */

document.addEventListener('DOMContentLoaded', () => {
  initMobileNav();
  initMenuFilter();
  initReservationForm();
  initSmoothScroll();
});

/**
 * MOD-01: Navigasi Mobile (Hamburger Toggle)
 */
function initMobileNav() {
  const toggleBtn = document.querySelector('.mobile-nav-toggle');
  const navMenu = document.querySelector('.nav-menu');
  const navLinks = document.querySelectorAll('.nav-link');

  if (toggleBtn && navMenu) {
    toggleBtn.addEventListener('click', () => {
      navMenu.classList.toggle('open');
      toggleBtn.setAttribute('aria-expanded', navMenu.classList.contains('open'));
    });

    navLinks.forEach(link => {
      link.addEventListener('click', () => {
        navMenu.classList.remove('open');
        toggleBtn.setAttribute('aria-expanded', 'false');
      });
    });
  }
}

/**
 * MOD-03: Filter Interaktif 9 Menu Best Seller
 * Pilihan: Semua (9), 3 Menu Makanan, 3 Menu Minuman, 3 Menu Snack
 */
function initMenuFilter() {
  const filterButtons = document.querySelectorAll('.filter-btn');
  const menuCards = document.querySelectorAll('.menu-card');

  if (!filterButtons.length || !menuCards.length) return;

  filterButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      // Set active button
      filterButtons.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const filterValue = btn.getAttribute('data-filter');

      // Filter cards
      menuCards.forEach(card => {
        const category = card.getAttribute('data-category');

        if (filterValue === 'all' || category === filterValue) {
          card.classList.remove('hidden');
          // Smooth fade in
          card.style.opacity = '0';
          card.style.transform = 'translateY(10px)';
          setTimeout(() => {
            card.style.transition = 'all 0.3s ease';
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
          }, 50);
        } else {
          card.classList.add('hidden');
        }
      });
    });
  });
}

/**
 * MOD-06: Formulir Reservasi Meja / Pesan Partai via WhatsApp
 * Nomor Resmi: 0896 5355 7758 (6289653557758)
 */
function initReservationForm() {
  const form = document.getElementById('reservationForm');
  if (!form) return;

  form.addEventListener('submit', (e) => {
    e.preventDefault();

    const name = document.getElementById('resName').value.trim();
    const count = document.getElementById('resCount').value.trim();
    const purpose = document.getElementById('resPurpose').value;
    const notes = document.getElementById('resNotes').value.trim();

    if (!name || !count) {
      alert('Mohon isi Nama dan Jumlah Orang/Porsi terlebih dahulu.');
      return;
    }

    // Format WhatsApp Message
    const waNumber = '6289653557758';
    let text = `Halo Punakawan Space & Eatery (Colomadu),\n`;
    text += `Saya ingin melakukan reservasi / pemesanan:\n\n`;
    text += `👤 *Nama Pemesan / Komunitas:* ${name}\n`;
    text += `👥 *Jumlah Orang / Porsi:* ${count}\n`;
    text += `📌 *Keperluan:* ${purpose}\n`;
    if (notes) {
      text += `📝 *Catatan Menu / Jam Kedatangan:* ${notes}\n`;
    }
    text += `\nMohon informasi dan konfirmasinya. Terima kasih!`;

    const encodedText = encodeURIComponent(text);
    const waUrl = `https://wa.me/${waNumber}?text=${encodedText}`;

    // Buka di tab baru
    window.open(waUrl, '_blank', 'noopener,noreferrer');
  });
}

/**
 * Smooth scrolling untuk tautan internal
 */
function initSmoothScroll() {
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      const targetId = this.getAttribute('href');
      if (targetId === '#' || !targetId) return;
      
      const targetElement = document.querySelector(targetId);
      if (targetElement) {
        e.preventDefault();
        targetElement.scrollIntoView({
          behavior: 'smooth'
        });
      }
    });
  });
}



