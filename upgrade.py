import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ---------- 1. Header: WhatsApp button → Cart button ----------
old_btn = re.search(r'<a href="https://wa\.me/254740636756\?text=Hi%20Au%20Sio%20\[SITE\]%2C%20I%20have%20a%20question"[^>]*>WhatsApp</a>', html)
if old_btn:
    html = html.replace(old_btn.group(0),
        '''<button type="button" class="cart-button" id="cartButton" aria-label="Open cart">
    <svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="21" r="1.5"/><circle cx="19" cy="21" r="1.5"/><path d="M2.5 3h2.5l2.5 13h11l2-9H6"/></svg>
    <span class="cart-badge" id="cartBadge">0</span>
  </button>''', 1)

# ---------- 2. Replace product cards ----------
cards_data = [
    {'brand':'jordan','id':'shoe-1','label':'JORDAN','name':'Air Jordan 12 Retro — Pink/White','size':'UK 9','cond':'Excellent','desc':"The most-wanted pair in the collection. Original mitumba, excellent condition, iconic pink-and-white colorway."},
    {'brand':'puma','id':'shoe-2','label':'PUMA','name':'Puma Suede — White/Blue','size':'UK 8','cond':'Excellent','desc':"Clean classic Puma Suede with blue accents. Original, excellent condition. A timeless everyday pair."},
    {'brand':'select','id':'shoe-3','label':'AU SIO SELECT','name':'Chukka Boot — African Print','size':'UK 10','cond':'Unique','desc':"One-of-a-kind chukka boot with African print detailing. Handpicked — you won't find another like it."},
    {'brand':'select','id':'shoe-4','label':'AU SIO SELECT','name':'Suede Runner — Grey/Orange','size':'UK 9','cond':'Excellent','desc':"Clean grey suede runner with a bold orange sole. Original, excellent condition, easy to wear with anything."},
]

pattern = re.compile(r'<article class="product-card"[^>]*>.*?</article>', re.DOTALL)
matches = pattern.findall(html)
print(f'Found {len(matches)} product cards')

for i, m in enumerate(matches):
    c = cards_data[i]
    new_card = f'''<article class="product-card" data-brand="{c['brand']}" data-id="{c['id']}" data-name="{c['name']}" data-size="{c['size']}" data-condition="{c['cond']}" data-image="images/{c['id']}.jpg" data-description="{c['desc']}">
        <div class="product-image">
          <img src="images/{c['id']}.jpg" alt="{c['name']}" loading="lazy">
          <span class="condition">{c['cond']}</span>
          <span class="tap-hint">Tap to view</span>
        </div>
        <div class="product-info">
          <p class="product-brand">{c['label']}</p>
          <h3>{c['name']}</h3>
          <p class="product-meta">{c['size']} · Original mitumba</p>
          <div class="product-footer">
            <span class="product-price">Ask price</span>
            <button type="button" class="product-order add-to-cart" data-id="{c['id']}">Add to cart</button>
          </div>
        </div>
      </article>'''
    html = html.replace(m, new_card, 1)

# ---------- 3. Cart drawer + modal + toast before </body> ----------
extras = '''
<aside class="cart-drawer" id="cartDrawer" aria-hidden="true">
  <div class="cart-header">
    <h3>Your order</h3>
    <button type="button" class="cart-close" id="cartClose" aria-label="Close">×</button>
  </div>
  <div class="cart-items" id="cartItems"><p class="cart-empty">Your cart is empty.</p></div>
  <div class="cart-footer">
    <p class="cart-note">Final prices confirmed on WhatsApp.</p>
    <button type="button" class="btn btn-primary cart-checkout" id="cartCheckout">Send order on WhatsApp</button>
  </div>
</aside>
<div class="cart-overlay" id="cartOverlay"></div>

<div class="modal" id="productModal" aria-hidden="true">
  <div class="modal-content">
    <button type="button" class="modal-close" id="modalClose" aria-label="Close">×</button>
    <div class="modal-image"><img id="modalImage" src="" alt=""></div>
    <div class="modal-info">
      <p class="product-brand" id="modalBrand"></p>
      <h3 id="modalName"></h3>
      <p class="product-meta" id="modalMeta"></p>
      <p class="modal-desc" id="modalDesc"></p>
      <div class="modal-footer">
        <span class="product-price">Ask price</span>
        <button type="button" class="btn btn-primary" id="modalAdd">Add to cart</button>
      </div>
    </div>
  </div>
</div>

<div class="toast" id="toast">Added to cart</div>
'''

html = html.replace('</body>', extras + '\n</body>', 1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Done. Cart, modal, and card upgrades applied.')
