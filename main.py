from selenium import webdriver
from selenium.webdriver.common.by import By

# ایجاد یک نسخه از مرورگر Firefox
driver = webdriver.Firefox()

# دامنه و واژه کلیدی مورد نظر را تعیین کنید
domain = "sdata.ir"
keyword = "اس دیتا"

# ترکیب دامنه و واژه کلیدی برای جستجو در گوگل
search_query = keyword

# آدرس صفحه گوگل را باز کنید
driver.get("https://www.google.com/search?q=" + search_query)

# دریافت نتایج جستجو
search_results = driver.find_elements(By.CSS_SELECTOR, ".tF2Cxc")

# شمارنده برای رتبه دامنه
rank = 1

# پیدا کردن دامنه مورد نظر و چاپ رتبه و صفحه آن
for result in search_results:
    # گرفتن عنوان لینک
    link_title = result.find_element(By.CSS_SELECTOR, "h3").text

    # گرفتن آدرس لینک
    link_url = result.find_element(By.CSS_SELECTOR, "a").get_attribute("href")

    # بررسی آیا دامنه مورد نظر در آدرس لینک وجود دارد
    if domain in link_url:
        print(f"score: {rank}")
        print(f"link name: {link_title}")
        print(f":link addres {link_url}\n")

    else:
    #   print(result.text)
        print("didnt find----------------------")
    # اگر رتبه دامنه پیدا شد، می‌توانید از دستور break استفاده کنید تا حلقه خاتمه یابد.
    # if domain in link_url:
    #     break
    rank += 1
# بستن مرورگر بعد از اتمام
driver.quit()