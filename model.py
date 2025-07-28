import pandas as pd
import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from hazm import Normalizer, word_tokenize, Stemmer
import emoji
import joblib
import os

normalizer = Normalizer()
stemmer = Stemmer()


def clean_text(text):
    # removing emojies
    text = emoji.replace_emoji(text, replace="")
    
    #normalization
    text = normalizer.normalize(text)
    
    # removing texts that not persian and noises
    text = re.sub(r'[^\u0600-\u06FF\s]', '', text)
    
    #tokenize and find the root of word
    tokens = word_tokenize(text)
    stemmed = [stemmer.stem(token) for token in tokens]
    
    return ' '.join(stemmed)
    

df = pd.read_csv("compeletDS.csv")

df = df[df['label'].isin(['happy','sad'])].copy()

df['clean_text'] = df['text'].apply(clean_text)

label_map = {'happy': 0, 'sad': 1}
inv_map = {0: 'happy', 1: 'sad'}
df['label'] = df['label'].map(label_map)

vectorizer = TfidfVectorizer(
max_df = 0.9,
min_df = 5,
max_features=5000
)

X = vectorizer.fit_transform(df['clean_text'])
y = df['label']


X_train, X_test, y_train, y_test = train_test_split(
X, y, test_size = 0.2, random_state=42, stratify=y
)



clf = RandomForestClassifier(
n_estimators=200,
max_depth=30,
random_state=42,
n_jobs=-1
)

clf.fit(X_train,y_train)

y_pred = clf.predict(X_test)

print("confusion_matrix:")
print(confusion_matrix(y_test,y_pred))
print("\nClassification Report:")
print(classification_report(y_test,y_pred))



y_pred = clf.predict(X_train)

print("confusion_matrix:")
print(confusion_matrix(y_train,y_pred))
print("\nClassification Report:")
print(classification_report(y_train,y_pred))


#os.makedirs("model", exist_ok=True)

# ذخیره مدل
#joblib.dump(clf, "model/sentiment_model.pkl")

# ذخیره TF-IDF
#joblib.dump(vectorizer, "model/tfidf_vectorizer.pkl")