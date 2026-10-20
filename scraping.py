from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup

from config_reader import load_config


def main():
    config = load_config()
    request = Request(config["url"], headers={"User-Agent": "Mozilla/5.0"})

    try:
        with urlopen(request, timeout=10) as response:
            html = response.read().decode(response.headers.get_content_charset() or "utf-8")
    except HTTPError as error:
        print(f"El sitio respondió con un error HTTP: {error.code}")
        return
    except URLError as error:
        print(f"No se pudo conectar con el sitio: {error.reason}")
        return

    soup = BeautifulSoup(html, "html.parser")
    quotes = soup.select(".quote")

    if not quotes:
        print("No se encontraron citas en la página.")
        return

    for quote in quotes:
        text = quote.select_one(".text").get_text(strip=True)
        author = quote.select_one(".author").get_text(strip=True)
        print(f"{text} — {author}")


if __name__ == "__main__":
    main()