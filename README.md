# SMS Spam Classifier

A machine learning web app that classifies a text message as **Spam** or **Not Spam**. Built with Python, NLTK, scikit-learn and Streamlit.

**Live demo:** <paste your Streamlit app link here>

---

## Features

- Paste any SMS and get an instant Spam / Not Spam prediction
- Text preprocessing with NLTK (lowercasing, tokenization, stopword removal, stemming)
- TF-IDF features with a Naive Bayes classifier
- Trained on a merged dataset of classic SMS spam and modern smishing (SMS phishing) messages
- Deployed on Streamlit Community Cloud

## How it works

```
Raw SMS -> Preprocessing -> TF-IDF Vectorizer -> Naive Bayes Model -> Spam / Not Spam
```

1. **Preprocessing:** lowercase, tokenize, keep only alphanumeric words, remove stopwords and punctuation, apply Porter stemming.
2. **Vectorization:** `TfidfVectorizer` converts cleaned text into numeric features.
3. **Classification:** a Naive Bayes model predicts spam (1) or not spam (0).

## Dataset

- **SMS Spam Collection** (UCI / Kaggle): about 5,500 labelled messages
- **SMS Phishing (Smishing) Dataset** (Mishra and Soni, Mendeley Data): modern scam-style messages, with "smishing" labels merged into the spam class
- Duplicates removed after merging, giving about 11,000 messages in total

## Results

| Model | Precision (spam) | Recall (spam) | Accuracy |
|-------|------------------|---------------|----------|
| MultinomialNB | _fill in_ | _fill in_ | _fill in_ |
| BernoulliNB | _fill in_ | _fill in_ | _fill in_ |

Recall matters more than accuracy here, because the dataset has far more normal messages than spam.

## Project structure

```
spam-detection/
├── app.py              # Streamlit web app
├── spam.ipynb          # Data analysis, training and evaluation
├── spam.csv            # Dataset
├── model.pkl           # Trained classifier
├── vectorizer.pkl      # Fitted TF-IDF vectorizer
├── requirements.txt    # Python dependencies
└── nltk.txt            # NLTK data needed for deployment
```

## Run locally

```bash
git clone https://github.com/yashvendravyas/spam-detection.git
cd spam-detection
python -m venv .venv
.venv\Scripts\activate        # on Mac/Linux: source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## Known limitations

- Detects **spam and scams only**. It does not detect abusive or rude messages.
- Trained mostly on English text, so it can miss new scam styles and Hinglish messages.
- Uses only message text. It does not look at the sender or link reputation.

## Future improvements

- Compare against Logistic Regression, SVM and XGBoost
- Add character n-grams and features such as link presence and digit count
- Fine-tune a transformer model (DistilBERT) for better understanding of new scams
- Expose the model as a FastAPI endpoint and build an Android app that checks incoming SMS
- Add a "Report spam" feedback loop to collect labelled data for retraining

## Tech stack

Python, Pandas, NumPy, NLTK, scikit-learn, Streamlit, Matplotlib, Seaborn

## Author

**Yashvendra Vyas**
GitHub: [@yashvendravyas](https://github.com/yashvendravyas)
