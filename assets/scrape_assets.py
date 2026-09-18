import urllib.request
import re
import os
import json

output_dir = "/Users/kalivibecoding/.gemini/antigravity/scratch/davarus_bell_brand_system/assets/images"
os.makedirs(output_dir, exist_ok=True)

urls_to_scrape = [
    ("linktree", "https://linktr.ee/davarusbell"),
    ("zillow", "https://www.zillow.com/profile/Davarus%20Bell%20Realtor"),
    ("voyagedallas", "http://voyagedallas.com/interview/meet-davarus-bell-of-only-1-realty-group/"),
    ("o1rg_website", "http://davarus.o1rg.com")
]

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

downloaded_files = []

for name, url in urls_to_scrape:
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as response:
            html = response.read().decode('utf-8', errors='ignore')
            
            # Find og:image or twitter:image or img src
            og_images = re.findall(r'property="og:image"\s+content="([^"]+)"', html)
            if not og_images:
                og_images = re.findall(r'name="og:image"\s+content="([^"]+)"', html)
            if not og_images:
                og_images = re.findall(r'content="([^"]+)"\s+property="og:image"', html)
            
            img_urls = og_images + re.findall(r'<img[^>]+src="([^"]+\.(?:jpg|jpeg|png|webp)[^"]*)"', html, re.IGNORECASE)
            
            count = 0
            for img_url in img_urls[:5]:
                if img_url.startswith('//'):
                    img_url = 'https:' + img_url
                elif img_url.startswith('/'):
                    base = '/'.join(url.split('/')[:3])
                    img_url = base + img_url
                
                if not img_url.startswith('http'):
                    continue
                
                try:
                    ext = "jpg"
                    if ".png" in img_url.lower(): ext = "png"
                    elif ".webp" in img_url.lower(): ext = "webp"
                    
                    file_name = f"{name}_asset_{count+1}.{ext}"
                    file_path = os.path.join(output_dir, file_name)
                    
                    img_req = urllib.request.Request(img_url, headers=headers)
                    with urllib.request.urlopen(img_req, timeout=10) as img_resp:
                        with open(file_path, 'wb') as f:
                            f.write(img_resp.read())
                    
                    downloaded_files.append({
                        "source": name,
                        "file_path": file_path,
                        "file_name": file_name,
                        "original_url": img_url
                    })
                    count += 1
                except Exception as e:
                    print(f"Failed downloading {img_url}: {e}")
    except Exception as e:
        print(f"Failed scraping {url}: {e}")

manifest_path = os.path.join(output_dir, "asset_manifest.json")
with open(manifest_path, "w") as f:
    json.dump(downloaded_files, f, indent=2)

print(f"Scraped {len(downloaded_files)} image assets.")
