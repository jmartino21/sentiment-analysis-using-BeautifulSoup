# Sentiment Analysis Using TextBlob and DistilBERT

## Overview
This project compares sentiment analysis performance between a **lexicon-based model** (TextBlob) and a **transformer model** (DistilBERT) on news headlines related to ChatGPT and Diffusion Models.

## Features
- **TextBlob Sentiment Analysis**: Uses a lexicon-based approach to assign polarity scores (-1 to 1).
- **DistilBERT Sentiment Analysis**: Uses a transformer model to classify sentiment probabilities for negative and positive sentiment.
- **Web Scraping**: Collects news headlines from Google News using **BeautifulSoup**.

## Installation
### Prerequisites
```bash
pip install requests beautifulsoup4 textblob torch transformers pandas openpyxl
```

## Dataset
This project collects real-time **Google News headlines** based on the keywords:
- "ChatGPT"
- "Diffusion models"

## Usage
### Running the Script
Execute the script using:
```bash
python sentiment_analysis_textblob_distilbert.py
```

### Steps Performed
1. Scrapes **Google News** for headlines matching specific keywords.
2. Runs sentiment analysis using **TextBlob** and **DistilBERT**.
3. Saves the results to an **Excel file (sentiment_scores.xlsx)**.

## Output
- **TextBlob Scores**: Direct polarity scores for each article.
- **DistilBERT Scores**: Predicted probabilities for positive and negative sentiment.
- **Excel File**: `sentiment_scores.xlsx` containing all results.

## Findings
- **TextBlob struggled with nuanced sentiment** and assigned neutral scores frequently.
- **DistilBERT provided more accurate sentiment predictions** based on context.
- Certain articles showed **contradictory sentiment ratings** between models, demonstrating the impact of different approaches to sentiment analysis.

## License
This project is open-source and available for modification and use.
