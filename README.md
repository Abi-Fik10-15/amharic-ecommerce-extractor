# Amharic E-commerce Data Extractor

This tool scrapes product listings from Amharic e-commerce sites, cleans the data, and stores it in CSV.

## Setup
```bash
pip install -r requirements.txt
python main.py
```

## Folder Structure
```
amharic-ecommerce-extractor/
├── data/
│   ├── raw/
│   └── cleaned/
├── extractor/
│   ├── config.py
│   ├── scraper.py
│   ├── cleaner.py
│   └── utils.py
├── main.py
├── requirements.txt
└── README.md
```

## Output
Cleaned product data saved to `data/cleaned/cleaned_data.csv`"# amharic-ecommerce-extractor" 
