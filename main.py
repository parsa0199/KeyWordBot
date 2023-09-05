import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl
from datetime import datetime
from selenium.webdriver.firefox.options import Options


options = webdriver.FirefoxOptions()
options.add_argument('-headless')



# Create an instance of the Firefox web browser

driver = webdriver.Firefox(options=options)

# Define the domain and keyword you want to search for
domain = "sdata.ir"
# Define the list of keywords you want to search for
keywords = ["شرکت تحلیل داده", "شرکت فناوری اطلاعات", "اس دیتا","بیگ دیتا","تحلیل داده"]



# Specify the number of pages to check (5 pages in this example)
pages_to_check = 7


# Create a new Excel workbook and add a worksheet
workbook = openpyxl.Workbook()
worksheet = workbook.active
worksheet.title = "Search Results"

# Add headers to the worksheet
worksheet["A1"] = "Keyword"
worksheet["B1"] = "Page"
worksheet["C1"] = "Rank"
worksheet["D1"] = "Link Address"
worksheet["E1"] = "Link TITLE"

# Set column widths (adjust the values as needed)
worksheet.column_dimensions['A'].width = 30  # Column A width
worksheet.column_dimensions['B'].width = 5  # Column B width
worksheet.column_dimensions['C'].width = 5  # Column C width
worksheet.column_dimensions['D'].width = 60  # Column D width
worksheet.column_dimensions['E'].width = 40  # Column D width
# Initialize the page number to 0
page = 0
rank=0

# Get the current date and time
current_date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
for keyword in keywords:
    page = 0  # Reset page to 0 for each keyword search
    not_found_pages = 0  # Initialize the variable for counting not found pages for each keyword

    while page < pages_to_check:
        # Increment the page number before opening the page

        # Open the Google search page with the formulated search query
        driver.get(f"https://www.google.com/search?q={keyword}&start={(page - 1) * 10}")
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
                print(f"page : {page}")
                print(f"Rank: {rank}")
                # print(f"Link name: {link_title}")
                print(f"Link address: {link_url}\n")
                found = True
                row = [keyword,page ,rank,link_url,link_title ]
                worksheet.append(row)

        if not found:
            print(f"Domain not found on page {page}.")
            not_found_pages += 1

        # اگر کلمه کلیدی در تمام 5 صفحه پیدا نشده باشد، یک رکورد خالی به اکسل اضافه کنید
        if not_found_pages == pages_to_check:
            print(f"Keyword '{keyword}' not found on any page.")
            row = [keyword, "یافت نشد", "", ""]
            worksheet.append(row)
workbook.save(f"search_results{keyword}-{current_date}.xlsx")

    # Increment the rank counter

# Close the web browser when done
driver.quit()