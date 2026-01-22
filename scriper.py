import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

# Chrome setup
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=chrome_options
)

driver.maximize_window()
driver.get("https://www.flipkart.com/q/smart-watches")
time.sleep(3)

# Lists
watch_name = []
current_price = []
mrp_price = []
discount = []
stars = []
rating = []
review = []

# Loop through pages
for page in range(1, 11):

    # Loop through products
    for i in range(2, 26):

        try:
            watch_name.append(
                driver.find_element(
                    'xpath', f'(//div[@data-id])[{i}]//div[@class="_4rR01T"]'
                ).text
            )
        except:
            watch_name.append("")

        try:
            current_price.append(
                driver.find_element(
                    'xpath', f'(//div[@data-id])[{i}]//div[@class="_30jeq3 _1_WHN1"]'
                ).text
            )
        except:
            current_price.append("")

        try:
            mrp_price.append(
                driver.find_element(
                    'xpath', f'(//div[@data-id])[{i}]//div[@class="_3I9_wc _27UcVY"]'
                ).text
            )
        except:
            mrp_price.append("")

        try:
            discount.append(
                driver.find_element(
                    'xpath', f'(//div[@data-id])[{i}]//div[@class="_3Ay6Sb"]'
                ).text
            )
        except:
            discount.append("")

        try:
            stars.append(
                driver.find_element(
                    'xpath', f'(//div[@data-id])[{i}]//div[@class="_3LWZlK"]'
                ).text
            )
        except:
            stars.append("")

        try:
            rating.append(
                driver.find_element(
                    'xpath', f'(//div[@data-id])[{i}]//span[contains(text(),"Ratings")]'
                ).text
            )
        except:
            rating.append("")

        try:
            review.append(
                driver.find_element(
                    'xpath', f'(//div[@data-id])[{i}]//span[contains(text(),"Reviews")]'
                ).text
            )
        except:
            review.append("")

    # Pagination handling
    if page < 10:
        try:
            if page == 1:
                next_button = driver.find_element(
                    'xpath',
                    '/html/body/div/div/div[3]/div[1]/div[2]/div[26]/div/div/nav/a[11]/span'
                )
            else:
                next_button = driver.find_element(
                    'xpath',
                    '/html/body/div/div/div[3]/div[1]/div[2]/div[26]/div/div/nav/a[12]/span'
                )

            next_button.click()
            time.sleep(3)

        except:
            print("Next button not found. Stopping.")
            break

# Save data
data_records = {
    'Watch_Name': watch_name,
    'Current_Price': current_price,
    'MRP_Price': mrp_price,
    'Discount': discount,
    'Stars': stars,
    'Rating': rating,
    'Review': review
}

df = pd.DataFrame(data_records)
df.to_csv("Output_records.csv", index=False)

driver.quit()

