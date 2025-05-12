import requests
from bs4 import BeautifulSoup
import urllib.parse
class ScrapeAmzonReview:
    # Function to search for product on Amazon and get the first product URL
    def search_amazon_product(self ,product_name):
        search_query = urllib.parse.quote_plus(product_name)  # Convert product name to a URL-friendly string
        url = f"https://www.amazon.in/s?k={search_query}"

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
        }

        # Send a GET request to the search URL
        response = requests.get(url, headers=headers)
        # response = requests.get(url)

        
        
        # run coroutine from server to client 
        
        if response.status_code != 200:
            print(f"Failed to retrieve search results. Status code: {response.status_code}")
            return None

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the first product's link using the correct class name
        first_product = soup.find('a', {'class': 'a-link-normal s-line-clamp-2 s-link-style a-text-normal'})
        if first_product:
            product_url = "https://www.amazon.in" + first_product['href']
            return product_url

        return None

    # Function to fetch and scrape reviews from Amazon product page
    def scrape_amazon_reviews(self ,url):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
        }

        # Send a GET request to the product URL with the headers
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            print(f"Failed to retrieve the page. Status code: {response.status_code}")
            return []

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        reviews = []

        # Find all review containers
        review_elements = soup.find_all('div', class_='reviewText')
        for review in review_elements:
            # Extract the review text from the span tag inside the nested div
            comment = review.find('span')
            if comment:
                # print("ELEMENTS :   " , comment.get_text(strip=True))
                review_data = {
                    'comment': comment.get_text(strip=True)
                }
                reviews.append(comment.get_text(strip=True))

        return reviews

# Example usage
if __name__ == "__main__":
    product_name = input("Enter the product name: ")

    # Step 1: Search for the product by name on Amazon
    obj = ScrapeAmzonReview()
    product_url = obj.search_amazon_product(product_name)
    
    if product_url:
        print(f"Product URL: {product_url}")
        
        # Step 2: Scrape reviews from the found product URL
        reviews = obj.scrape_amazon_reviews(product_url)

        if reviews:
            for idx, review in enumerate(reviews, 1):
                print(f"Review {idx}:")
                print(f"Comment: {review['comment']}")
                print("-" * 50)
        else:
            print("No reviews found.")
    else:
        print("Product not found.")
