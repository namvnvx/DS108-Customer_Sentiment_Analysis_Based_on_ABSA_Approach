# 📊 Customer Sentiment Analysis Using the ABSA Approach  

## 📂 Project Files  

- **`Data_scraped.csv`**  
  - Raw dataset obtained after executing `Scraping.py`.  

- **`Final_data.csv`**  
  - Extracted **'text'** field from `Data_scraped.csv`.  
  - Preprocessed by splitting text into smaller sentences.  
  - Labeled and structured for sentiment classification.  

- **`Model_Build_TensorFlow.ipynb`**  
  - Implements a sentiment analysis model using **TensorFlow’s Vectorizer**.  

- **`Model_Build_CountVectorizer.ipynb`**  
  - Builds a sentiment classification model using **Count Vectorizer** from `sklearn.feature_extraction.text`.  

- **`Model_Hand_Made.ipynb`**  
  - Develops a **custom sentiment model** utilizing a **modified TF-IDF approach**.  
