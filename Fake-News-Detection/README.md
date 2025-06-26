# 📰 Fake News Detection

## ✅ Objective
Build a machine learning model that can classify whether a news article is **fake** or **real**, using NLP techniques like TF-IDF vectorization and a Passive Aggressive Classifier.

---

## 💻 Technologies Used
- Python
- Pandas, NumPy
- Scikit-learn
- TF-IDF Vectorizer
- Passive Aggressive Classifier
- Seaborn & Matplotlib (for visuals)

---

## 📁 Dataset
Used the [Fake and Real News Dataset](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset)

- `Fake.csv`: contains fake news articles
- `True.csv`: contains real news articles
- Combined inside the notebook and labeled as `fake` and `real`

---

## 🔧 How It Works
1. Combine fake and real news datasets
2. Preprocess the text data (remove stopwords, vectorize)
3. Split into training and test sets
4. Train a **Passive Aggressive Classifier**
5. Evaluate with accuracy, classification report, and confusion matrix

---

## 📊 Model Performance
- ✅ Accuracy: ~**93–96%**
- ✅ High precision & recall on both classes

---

## 📸 Screenshots

### 🧾 Dataset Preview + Label Counts

![Dataset Preview](./screenshots/01_dataset_preview.png)

---

### 🎯 Accuracy & Classification Report

![Model Accuracy](./screenshots/02_model_accuracy.png)

---

### 📉 Confusion Matrix Heatmap

![Confusion Matrix](./screenshots/03_confusion_matrix.png)