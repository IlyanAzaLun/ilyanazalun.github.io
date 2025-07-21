import instaloader
import json

USERNAME = "ilyanazalun"
# IG_USERNAME = "ilyanazalun"
# IG_PASSWORD = "$Mak65yousmil65"

L = instaloader.Instaloader()
# L.login(IG_USERNAME, IG_PASSWORD)
profile = instaloader.Profile.from_username(L.context, USERNAME)

posts_data = []
for post in profile.get_posts():
    posts_data.append({
        "image_url": post.url,
        "caption": post.caption,
        "link": f"https://www.instagram.com/p/{post.shortcode}/"
    })

with open("_data/instagram.json", "w") as f:
    json.dump(posts_data, f, ensure_ascii=False, indent=2)

print("Scraping selesai, data tersimpan di _data/instagram.json")