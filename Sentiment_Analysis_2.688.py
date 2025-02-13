import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
import torch
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
import pandas as pd

# Scrape news headlines
def scrape_news_headlines(keywords, limit=10):
    article_list = []
    for term in keywords:
        url = f'https://news.google.com/search?q={term}'
        content = requests.get(url)
        soup = BeautifulSoup(content.text, 'html.parser')
        for title in soup.find_all('h3', class_="ipQwMb ekueJc RD0gLb", limit=limit):
            article_list.append(title.text.lower())
    return article_list

# Perform sentiment analysis using TextBlob
def analyze_sentiment_textblob(articles):
    return [TextBlob(title).sentiment.polarity for title in articles]

# Perform sentiment analysis using DistilBERT
def analyze_sentiment_distilbert(articles):
    tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')
    model = DistilBertForSequenceClassification.from_pretrained('distilbert-base-uncased')
    
    tokenized_articles = tokenizer.batch_encode_plus(
        articles, max_length=128, padding='max_length', truncation=True, return_tensors='pt'
    )
    
    model.eval()
    with torch.no_grad():
        inputs = {
            'input_ids': tokenized_articles['input_ids'],
            'attention_mask': tokenized_articles['attention_mask']
        }
        outputs = model(**inputs)
        logits = outputs.logits
        return torch.softmax(logits, dim=-1).tolist()

# Main execution
if __name__ == "__main__":
    keywords = ['ChatGPT', 'Diffusion models']
    articles = scrape_news_headlines(keywords)
    
    textblob_scores = analyze_sentiment_textblob(articles)
    distilbert_scores = analyze_sentiment_distilbert(articles)
    
    df_sentiment_scores = pd.DataFrame({
        'Article': articles,
        'TextBlob Sentiment Scores': textblob_scores,
        'DistilBERT Sentiment Scores': distilbert_scores
    })
    
    df_sentiment_scores.to_excel("sentiment_scores.xlsx", index=False)
    print("Sentiment analysis complete. Results saved to 'sentiment_scores.xlsx'.")
