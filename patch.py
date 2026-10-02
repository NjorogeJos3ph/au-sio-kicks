import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Insert ticker + stats after hero section
ticker_stats = '''
  <div class="ticker">
    <div class="ticker-track">
      <span>Just in — Air Jordan 12 Retro</span><span class="dot">•</span>
      <span>Puma Suede — White/Blue</span><span class="dot">•</span>
      <span>Chukka Boot — African Print</span><span class="dot">•</span>
      <span>Suede Runner — Grey/Orange</span><span class="dot">•</span>
      <span>Original mitumba · Curated in Githurai</span><span class="dot">•</span>
      <span>Just in — Air Jordan 12 Retro</span><span class="dot">•</span>
      <span>Puma Suede — White/Blue</span><span class="dot">•</span>
      <span>Chukka Boot — African Print</span><span class="dot">•</span>
      <span>Suede Runner — Grey/Orange</span><span class="dot">•</span>
      <span>Original mitumba · Curated in Githurai</span><span class="dot">•</span>
    </div>
  </div>

  <section class="stats-strip">
    <div class="stat"><strong>70+</strong><span>Pairs in stock</span></div>
    <div class="stat"><strong>100%</strong><span>Original</span></div>
    <div class="stat"><strong>1 of 1</strong><span>Every pair unique</span></div>
    <div class="stat"><strong>Githurai</strong><span>See in person</span></div>
  </section>
'''

html = html.replace('  </section>\n\n  <section id="collection"',
                    '  </section>\n' + ticker_stats + '\n  <section id="collection"', 1)

# 2. Featured shoe card before product-grid
featured = '''    <div class="featured-shoe">
      <div class="featured-image">
        <img src="images/shoe-1.jpg" alt="Air Jordan 12 Retro" loading="eager">
        <span class="featured-badge">★ This week's pick</span>
      </div>
      <div class="featured-content">
        <p class="product-brand">JORDAN</p>
        <h3>Air Jordan 12 Retro — Pink/White</h3>
        <p class="featured-desc">Our most-wanted pair right now. Original mitumba, excellent condition, UK 9. Only 1 available.</p>
        <div class="featured-footer">
          <span class="product-price">Ask price</span>
          <a href="https://wa.me/254740636756?text=Hi%20Au%20Sio%20[SITE]%2C%20I'm%20interested%20in%20the%20Air%20Jordan%2012%20Retro%20(UK%209)" class="btn btn-primary" target="_blank" rel="noopener">Reserve this pair</a>
        </div>
      </div>
    </div>

'''

html = html.replace('    <div class="product-grid" id="productGrid">',
                    featured + '    <div class="product-grid" id="productGrid">', 1)

# 3. Floating WhatsApp button
floating = '''
<a href="https://wa.me/254740636756?text=Hi%20Au%20Sio%20[SITE]%2C%20I%20want%20to%20see%20what's%20available" class="floating-whatsapp" target="_blank" rel="noopener" aria-label="Chat on WhatsApp">
  <svg viewBox="0 0 24 24" width="28" height="28" fill="currentColor"><path d="M20.5 3.5A11.9 11.9 0 0 0 12 0C5.4 0 0 5.4 0 12c0 2.1.5 4.1 1.6 5.9L0 24l6.3-1.6A11.9 11.9 0 0 0 12 24c6.6 0 12-5.4 12-12 0-3.2-1.2-6.2-3.5-8.5zM12 21.8c-1.8 0-3.5-.5-5-1.4l-.4-.2-3.7.9 1-3.6-.2-.4A9.7 9.7 0 0 1 2.2 12C2.2 6.6 6.6 2.2 12 2.2S21.8 6.6 21.8 12s-4.4 9.8-9.8 9.8zm5.4-7.3c-.3-.1-1.7-.9-2-1s-.5-.1-.7.1c-.2.3-.7 1-.9 1.2s-.3.2-.6.1c-.3-.1-1.3-.5-2.4-1.5c-.9-.8-1.5-1.8-1.7-2.1s0-.5.1-.6c.1-.1.3-.4.5-.5.2-.2.2-.3.3-.5s.1-.4 0-.5s-.7-1.6-.9-2.2c-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4s-1 1-1 2.4s1 2.8 1.2 3c.1.2 2 3.1 5 4.3c.7.3 1.2.5 1.7.6c.7.2 1.3.2 1.8.1c.5-.1 1.7-.7 1.9-1.4s.2-1.2.2-1.4s-.2-.3-.4-.4z"/></svg>
</a>
'''

html = html.replace('</body>', floating + '\n</body>', 1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Done. Ticker, stats, featured shoe, floating WhatsApp added.')
