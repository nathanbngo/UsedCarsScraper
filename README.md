
# **Used Cars Scraper**

A Python project for scraping and analyzing used car market data from websites like **CarGurus** or **AutoTrader**.

---

## **Features**
- Extracts car details such as:
  - **Brand**
  - **Year**
  - **Price**
  - **Mileage**
- Saves the data to an **Excel file** for easy viewing.
- Generates scatter plots for trend analysis (e.g., **Price vs. Mileage**).

---

## **Project Structure**
```
UsedCarsScraper/
├── data/                 # Folder for output Excel files
├── scripts/              # Python scripts for scraping and analysis
│   ├── scraper.py        # Main script for Tkinter desktop UI
│   ├── utils.py          # Utility functions for scraping and visualization
│   └── requirements.txt  # List of required Python libraries
├── web/                  # Flask-based web UI
│   ├── app.py            # Flask application entry point
│   └── templates/        # HTML templates for the web interface
└── chromedriver/         # ChromeDriver executable (required for Selenium)
```

---
