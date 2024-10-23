import requests
from bs4 import BeautifulSoup


def get_products(search_query):
    url = f"https://www.instacart.com/store/s?k={search_query}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception(f"Failed to load page {response.status_code}")

    soup = BeautifulSoup(response.text, 'html.parser')

    products = []
    for item in soup.find_all('div', class_='product-item'):
        name = item.find('h3').get_text()
        price = item.find('span', class_='price').get_text()
        rating = item.find('span', class_='rating').get_text() if item.find('span', class_='rating') else None

        product_info = {
            'name': name,
            'price': price,
            'rating': rating
        }

        products.append(product_info)

    return products


# Example usage
search_query = "milk"
products = get_products(search_query)
print(products)
for product in products:
    print(product)
