import os
import time
import random
import requests
from tqdm import tqdm
from PIL import Image
from io import BytesIO
from bs4 import BeautifulSoup
from urllib.parse import quote

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Mozilla/5.0 (X11; Linux x86_64)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X)",
    "Mozilla/5.0 (iPad; CPU OS 13_5 like Mac OS X)"
]

def is_valid_image(img):
    return img.width > 100 and img.height > 100 and img.mode == "RGB"

def fetch_bing_image_urls(query, needed=100):
    image_urls = []
    offset = 0
    print(f"🔍 Fetching Bing URLs for: {query}")

    while len(image_urls) < needed:
        headers = {"User-Agent": random.choice(USER_AGENTS)}
        url = f"https://www.bing.com/images/async?q={quote(query)}&first={offset}&count=35"

        try:
            res = requests.get(url, headers=headers, timeout=10)
            print(f"🔁 Status code: {res.status_code} (offset {offset})")

            if res.status_code != 200:
                print("❌ Blocked or failed. Try switching VPN.")
                break

            soup = BeautifulSoup(res.text, "html.parser")
            tags = soup.find_all("a", class_="iusc")
            if not tags:
                print("⚠️ No more Bing results.")
                break

            for tag in tags:
                try:
                    m = eval(tag.get("m"))
                    title = m.get("t", "").lower()
                    if "hair" not in title:
                        continue
                    url = m["murl"]
                    if url not in image_urls:
                        image_urls.append(url)
                    if len(image_urls) >= needed:
                        break
                except:
                    continue

            offset += 35
            time.sleep(2)

        except Exception as e:
            print(f"❌ Error: {e}")
            break

    print(f"✅ Got {len(image_urls)} image URLs\n")
    return image_urls

def download_images(image_urls, output_dir, prefix, target_count=100):
    os.makedirs(output_dir, exist_ok=True)
    count = 0
    index = len(os.listdir(output_dir)) + 1
    bar = tqdm(total=target_count, desc=f"🖼️ Saving {prefix}", ncols=100)

    for url in image_urls:
        if count >= target_count:
            break
        try:
            res = requests.get(url, timeout=5)
            img = Image.open(BytesIO(res.content)).convert("RGB")
            if not is_valid_image(img):
                continue
            img.save(os.path.join(output_dir, f"{prefix}_{index}.jpg"))
            index += 1
            count += 1
            bar.update(1)
        except Exception:
            continue

    bar.close()
    print(f"✅ Done! {count} images saved to: {output_dir}\n")

def main():
    query = "waist length women hair back view"
    output_dir = "hair_dataset/long"
    image_urls = fetch_bing_image_urls(query, needed=100)
    download_images(image_urls, output_dir, prefix="long", target_count=100)

if __name__ == "__main__":
    main()
