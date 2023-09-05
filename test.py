import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Create an instance of the Firefox web browser
driver = webdriver.Firefox()

# Define the domain and keyword you want to search for
domain = "sdata.ir"
keyword = "شرکت تحلیل داده"

# Formulate the search query by combining the domain and keyword
search_query = keyword

# Initialize the rank counter for the domain


# Specify the number of pages to check (5 pages in this example)
pages_to_check = 5

# Initialize the page number to 0
page = 0
rank=0
while page < pages_to_check:
    # Increment the page number before opening the page


    # Open the Google search page with the formulated search query
    driver.get(f"https://www.google.com/search?q={search_query}&start={(page - 1) * 10}")
    page += 1
    # Find and store the search results on the page using a CSS selector
    search_results = driver.find_elements(By.CSS_SELECTOR, ".tF2Cxc")

    found = False
    rank = 0

    # Iterate through the search results to find the domain and print its rank and details
    for result in search_results:
        rank += 1

        link_title = result.find_element(By.CSS_SELECTOR, "h3").text
        link_url = result.find_element(By.CSS_SELECTOR, "a").get_attribute("href")

        if domain in link_url:
            print(f"Rank: {rank}")
            print(f"Link name: {link_title}")
            print(f"Link address: {link_url}")
            print(f"page : {page}\n")
            found = True

    if not found:
        print(f"Domain not found on page {page}.")

    # Increment the rank counter

# Close the web browser when done
driver.quit()