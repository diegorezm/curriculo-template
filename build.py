import markdown
import sys
import json
from weasyprint import HTML

md_file, pdf_file = sys.argv[1], sys.argv[2]
config_file = sys.argv[3] if len(sys.argv) > 3 else "config.json"

with open(config_file, 'r', encoding='utf-8') as f:
    config = json.load(f)

with open(md_file, 'r', encoding='utf-8') as f:
    content = f.read()

html = markdown.markdown(content)

contact_links = []
for contact in config['contacts']:
    link_html = f'''<a href="{contact['url']}" class="text-center">
        <img src="{contact['icon']}" class="icon"/> {contact['display']}
      </a>'''
    contact_links.append(link_html)

contacts_html = '<span class="separator">·</span>'.join(contact_links)

full_html = f"""
<html>
  <head><link rel="stylesheet" href="style.css"></head>
  <body>
    <header>
      <h1>{config['name']}</h1>
      <div class="contact">
        {contacts_html}
      </div>
    </header> 
    <main>
        {html}
    </main>
  </body>
</html>
"""

HTML(string=full_html, base_url=".").write_pdf(pdf_file)
print(f"PDF gerado com sucesso: {pdf_file}")
