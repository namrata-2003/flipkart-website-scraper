# Flipkart Smart Watches Web Scraper (Selenium)

## 📌 Project Overview
This project demonstrates web scraping of smart watch product data from Flipkart using **Selenium WebDriver** and **Python**.

The scraper attempts to extract:
- Watch Name
- Current Price
- MRP Price
- Discount
- Star Rating
- Ratings Count
- Reviews Count

The extracted data is saved into a CSV file using **Pandas**.

---

## ⚙️ Technologies Used
- Python
- Selenium
- Pandas
- WebDriver Manager (Chrome)
- XPath

---

## 🚧 Current Status
⚠️ **Work in Progress**

Due to Flipkart's dynamic UI changes, login popups, and frequently changing class names, the current version may not consistently scrape data without modification.

This repository is intended to:
- Demonstrate Selenium scraping logic
- Show pagination handling
- Showcase exception handling for missing elements
- Reflect real-world scraping challenges

---

## 🧠 Key Learning Points
- Handling dynamic web pages using Selenium
- Pagination automation
- Use of XPath selectors
- Exception handling for missing elements
- Limitations of scraping modern e-commerce websites

---

## 🔧 Future Improvements
- Replace `time.sleep()` with `WebDriverWait`
- Improve XPath stability
- Handle Flipkart login popups more reliably
- Modularize code using functions/classes
- Add headless mode
- Clean and normalize scraped price data

---

## ⚠️ Disclaimer
This project is for **educational purposes only**.  
Flipkart’s website may restrict scraping as per their Terms of Service.
