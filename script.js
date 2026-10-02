document.addEventListener('DOMContentLoaded', () => {

  // ===== FILTERS =====
  const filters = document.querySelectorAll('.filter');
  const cards = document.querySelectorAll('.product-card');
  filters.forEach(btn => {
    btn.addEventListener('click', () => {
      filters.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const brand = btn.dataset.filter;
      cards.forEach(card => {
        card.style.display = (brand === 'all' || card.dataset.brand === brand) ? '' : 'none';
      });
    });
  });

  // ===== FADE-IN ON SCROLL =====
  const revealEls = document.querySelectorAll('.product-card, .how-card, .featured-shoe, .stat');
  revealEls.forEach(el => el.classList.add('reveal'));
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1 });
  revealEls.forEach(el => observer.observe(el));

  // ===== CART =====
  const CART_KEY = 'ausio-cart';
  let cart = JSON.parse(localStorage.getItem(CART_KEY) || '[]');
  const cartDrawer = document.getElementById('cartDrawer');
  const cartOverlay = document.getElementById('cartOverlay');
  const cartBadge = document.getElementById('cartBadge');
  const cartItemsEl = document.getElementById('cartItems');
  const cartBtn = document.getElementById('cartButton');
  const cartClose = document.getElementById('cartClose');
  const cartCheckout = document.getElementById('cartCheckout');
  const toast = document.getElementById('toast');

  function updateBadge() {
    cartBadge.textContent = cart.length;
    cartBadge.style.display = cart.length > 0 ? 'flex' : 'none';
  }
  function save() { localStorage.setItem(CART_KEY, JSON.stringify(cart)); }

  function renderCart() {
    if (cart.length === 0) {
      cartItemsEl.innerHTML = '<p class="cart-empty">Your cart is empty.</p>';
      return;
    }
    cartItemsEl.innerHTML = cart.map((item, i) => `
      <div class="cart-item">
        <img src="${item.image}" alt="${item.name}">
        <div class="cart-item-info">
          <p class="cart-item-name">${item.name}</p>
          <p class="cart-item-meta">${item.size}</p>
        </div>
        <button type="button" class="cart-remove" data-index="${i}" aria-label="Remove">×</button>
      </div>`).join('');
    cartItemsEl.querySelectorAll('.cart-remove').forEach(b => {
      b.addEventListener('click', () => {
        cart.splice(parseInt(b.dataset.index), 1);
        save(); renderCart(); updateBadge();
      });
    });
  }

  function openCart() {
    cartDrawer.classList.add('open'); cartOverlay.classList.add('open');
    cartDrawer.setAttribute('aria-hidden','false');
  }
  function closeCart() {
    cartDrawer.classList.remove('open'); cartOverlay.classList.remove('open');
    cartDrawer.setAttribute('aria-hidden','true');
  }
  function showToast(text) {
    toast.textContent = text; toast.classList.add('show');
    setTimeout(() => toast.classList.remove('show'), 1800);
  }
  function addToCart(item) {
    if (cart.find(x => x.id === item.id)) { showToast('Already in cart'); return; }
    cart.push(item); save(); updateBadge(); renderCart(); showToast('Added to cart');
  }

  cartBtn.addEventListener('click', openCart);
  cartClose.addEventListener('click', closeCart);
  cartOverlay.addEventListener('click', closeCart);
  cartCheckout.addEventListener('click', () => {
    if (cart.length === 0) return;
    const list = cart.map((item, i) => `${i+1}. ${item.name} (${item.size})`).join('\n');
    const msg = `Hi Au Sio [SITE], I'd like to order:\n\n${list}\n\nPlease confirm prices and availability.`;
    window.open(`https://wa.me/254740636756?text=${encodeURIComponent(msg)}`, '_blank');
  });

  // ===== PRODUCT MODAL =====
  const modal = document.getElementById('productModal');
  const modalClose = document.getElementById('modalClose');
  const modalImage = document.getElementById('modalImage');
  const modalBrand = document.getElementById('modalBrand');
  const modalName = document.getElementById('modalName');
  const modalMeta = document.getElementById('modalMeta');
  const modalDesc = document.getElementById('modalDesc');
  const modalAdd = document.getElementById('modalAdd');
  let currentProduct = null;

  function openModal(card) {
    currentProduct = {
      id: card.dataset.id, name: card.dataset.name, size: card.dataset.size,
      condition: card.dataset.condition, image: card.dataset.image,
      description: card.dataset.description,
      brand: card.querySelector('.product-brand').textContent
    };
    modalImage.src = currentProduct.image;
    modalImage.alt = currentProduct.name;
    modalBrand.textContent = currentProduct.brand;
    modalName.textContent = currentProduct.name;
    modalMeta.textContent = `${currentProduct.size} · ${currentProduct.condition} · Original mitumba`;
    modalDesc.textContent = currentProduct.description;
    modal.classList.add('open'); modal.setAttribute('aria-hidden','false');
    document.body.style.overflow = 'hidden';
  }
  function closeModal() {
    modal.classList.remove('open'); modal.setAttribute('aria-hidden','true');
    document.body.style.overflow = '';
  }

  cards.forEach(card => {
    card.addEventListener('click', (e) => {
      if (e.target.closest('.add-to-cart')) return;
      openModal(card);
    });
  });
  modalClose.addEventListener('click', closeModal);
  modal.addEventListener('click', (e) => { if (e.target === modal) closeModal(); });
  modalAdd.addEventListener('click', () => {
    if (currentProduct) { addToCart(currentProduct); closeModal(); openCart(); }
  });

  document.querySelectorAll('.add-to-cart').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.stopPropagation();
      const card = btn.closest('.product-card');
      addToCart({
        id: card.dataset.id, name: card.dataset.name, size: card.dataset.size,
        condition: card.dataset.condition, image: card.dataset.image,
        description: card.dataset.description,
        brand: card.querySelector('.product-brand').textContent
      });
    });
  });

  updateBadge(); renderCart();
});
