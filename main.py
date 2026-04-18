class URLShortener:
    def __init__(self):
        self.url_map = {}

    def generate_short_url(self, original_url):
        import uuid
        short_url = str(uuid.uuid4())[:6]
        self.url_map[short_url] = original_url
        return f"http://short.url/{short_url}"

    def get_original_url(self, short_url):
        return self.url_map.get(short_url.split('/')[-1])

url_shortener = URLShortener()

# Misol:
original_url = "https://www.example.com/long-url"
short_url = url_shortener.generate_short_url(original_url)
print(f"Original URL: {original_url}")
print(f"Short URL: {short_url}")

original_url_from_short = url_shortener.get_original_url(short_url)
print(f"Original URL from Short URL: {original_url_from_short}")
```

Kodda quyidagilar qo'llangan:

- URL qisqartiruvchi funksiyalari uchun `uuid` kutubxonasidan foydalanilgan.
- URL qisqartiruvchi funksiyalari uchun `dict` ma'lumotlar bazasi ishlatilgan.
- URL qisqartiruvchi funksiyalari uchun `str` va `split` funksiyalari ishlatilgan.
- URL qisqartiruvchi funksiyalari uchun `get` metodi ishlatilgan.
