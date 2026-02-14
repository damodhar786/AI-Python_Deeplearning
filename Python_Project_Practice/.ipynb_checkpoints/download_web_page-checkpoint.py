import requests

url = input("Provide a URL to download: ")
print("Downloading..................")

try:
    response = requests.get(url, timeout=10)
    if response.status_code == 200:
        with open("downloaded_page.html", "w", encoding="utf-8") as file:
            file.write(response.text)
            print("Page copied as HTML")
except requests.exceptions.RequestException:
    print("Failed to download the web page. Please check the URL.")
