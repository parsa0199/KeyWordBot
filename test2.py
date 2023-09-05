import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Create an instance of the Firefox web browser
driver = webdriver.Firefox()

# Define the domain and keyword you want to search for
domain = "sdata.ir"
keyword = "تحلیل داده"

# Formulate the search query by combining the domain and keyword
search_query =keyword

# Initialize the rank counter for the domain
rank = 1

while True:
    # Open the Google search page with the formulated search query
    driver.get(f"https://www.google.com/search?q={search_query}&start={(rank - 1) * 10}")

    # Find and store the search results on the page using a CSS selector
    search_results = driver.find_elements(By.CSS_SELECTOR, ".tF2Cxc")

    found = False

    # Iterate through the search results to find the domain and print its rank and details
    for result in search_results:
        link_title = result.find_element(By.CSS_SELECTOR, "h3").text
        link_url = result.find_element(By.CSS_SELECTOR, "a").get_attribute("href")

        if domain in link_url:
            print(f"Rank: {rank}")
            print(f"Link name: {link_title}")
            print(f"Link address: {link_url}\n")
            found = True

    if not found:
        print("Domain not found on this page.")

    # Check if there is a "Next" button and click it to move to the next page
    try:
        next_button = driver.find_element(By.ID, "pnnext")
        next_button.click()

    except Exception as e:
        print("No more pages found.")
        break

    # Increment the rank counter
    rank += 1

# Close the web browser when done
driver.quit()