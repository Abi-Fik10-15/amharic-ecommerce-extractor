from extractor.scraper import scrape_products
from extractor.cleaner import clean_data
import pandas as pd

if __name__ == "__main__":
    raw_data = scrape_products()
    cleaned_data = clean_data(raw_data)
    df = pd.DataFrame(cleaned_data)
    df.to_csv("data/cleaned/cleaned_data.csv", index=False)
    print("Pipeline completed. Cleaned data saved.")