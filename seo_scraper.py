import urllib.request
import urllib.error
import re
import json

def fetch_html(url):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            return response.read().decode('utf-8')
    except Exception as e:
        return str(e)

def extract_seo(html):
    data = {}
    
    # Title
    title_match = re.search(r'<title[^>]*>(.*?)</title>', html, re.IGNORECASE | re.DOTALL)
    data['title'] = title_match.group(1).strip() if title_match else None
    
    # Meta description
    meta_desc_match = re.search(r'<meta[^>]*name=["\']description["\'][^>]*content=["\'](.*?)["\']', html, re.IGNORECASE)
    data['meta_description'] = meta_desc_match.group(1).strip() if meta_desc_match else None
    
    # Headings
    for i in range(1, 4):
        matches = re.findall(rf'<h{i}[^>]*>(.*?)</h{i}>', html, re.IGNORECASE | re.DOTALL)
        data[f'h{i}'] = [re.sub(r'<[^>]+>', '', m).strip() for m in matches]
        
    # Images
    img_matches = re.findall(r'<img\s+([^>]+)>', html, re.IGNORECASE)
    data['images'] = []
    for img in img_matches:
        src = re.search(r'src=["\'](.*?)["\']', img, re.IGNORECASE)
        alt = re.search(r'alt=["\'](.*?)["\']', img, re.IGNORECASE)
        title = re.search(r'title=["\'](.*?)["\']', img, re.IGNORECASE)
        data['images'].append({
            'src': src.group(1) if src else None,
            'alt': alt.group(1) if alt else None,
            'title': title.group(1) if title else None
        })
        
    # Links
    link_matches = re.findall(r'<a[^>]+href=["\'](.*?)["\']', html, re.IGNORECASE)
    data['links'] = [l for l in link_matches if not l.startswith('javascript')]
    
    # Word count estimation (strip all tags)
    text = re.sub(r'<script.*?</script>', '', html, flags=re.IGNORECASE|re.DOTALL)
    text = re.sub(r'<style.*?</style>', '', text, flags=re.IGNORECASE|re.DOTALL)
    text = re.sub(r'<[^>]+>', ' ', text)
    words = [w for w in text.split() if w.strip()]
    data['word_count'] = len(words)
    
    return data

url = "https://www.wiretelecom.fr/"
html = fetch_html(url)
seo_data = extract_seo(html)

robots = fetch_html(url + "robots.txt")
sitemap = fetch_html(url + "sitemap.xml")

with open('seo_data.json', 'w', encoding='utf-8') as f:
    json.dump({
        'homepage_seo': seo_data,
        'robots_txt': robots[:500],
        'sitemap_xml': sitemap[:1000]
    }, f, indent=2)

print("Scraping complete.")
