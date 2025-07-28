# Persian Sentiment Analysis using Random Forest

## ✨ Overview
This project is a **Sentiment Analysis** system for **Persian text**, built using classical **Machine Learning (Random Forest)** methods. The model is trained to classify Persian sentences into two main emotions: `happy` and `sad`.

The purpose of this project is to demonstrate practical skills in **NLP preprocessing**, **model development**, **evaluation**, and **deployment readiness**, and it is designed to be part of a personal portfolio for job/internship applications in **data science** or **machine learning** roles.

---

## 🔧 Features
- **Support for Persian (Farsi) language** with custom preprocessing
- **Binary classification** (`happy`, `sad`) using Random Forest
- Cleaned emoji and unnecessary characters
- Evaluation using `confusion matrix`, `precision`, `recall`, and `f1-score`
- Model serialized and ready for deployment (Flask/Django compatible)

---

## 📊 Results
- **Accuracy** on test set: ~83%
- **Accuracy** on training set: ~87%
- No significant overfitting
- Balanced performance between classes

Confusion Matrix (Test):
```
[[5317 1642]
 [ 699 5971]]
```

Classification Report (Test):
```
              precision    recall  f1-score   support

    happy       0.88      0.76      0.82      6959
      sad       0.78      0.90      0.84      6670

  accuracy                           0.83     13629
 macro avg       0.83      0.83      0.83     13629
weighted avg     0.84      0.83      0.83     13629
```

---

## 🧳 Tech Stack
- Python 3.10
- Pandas, NumPy
- scikit-learn
- hazm (Persian NLP)
- emoji (cleaning)

---

## 📚 Dataset
Due to limitations, the dataset was curated from multiple sources and cleaned manually. Only two main classes (`happy`, `sad`) were used for training. Emojis were removed in preprocessing.

---

## ⚙️ How to Run
```bash
# Install dependencies
pip install -r requirements.txt

# Run the model training (includes evaluation)
python main.py
```

Trained model will be saved as a pickle file and can be reused in a web backend like Flask or Django.

---

## 📊 Future Improvements
- Add more sentiment classes (e.g., angry, surprise, fear) using fine-tuning
- Use deep learning models (e.g., ParsBERT)
- Create REST API with Flask or Django
- Add a web interface for real-time sentiment detection

---

## 🌟 About Me
I’m an aspiring **machine learning developer** looking for internship opportunities. This project is part of my personal learning journey and portfolio. I’m passionate about building real-world applications using AI/NLP.

---

## 📅 Project Status
✅ Completed (first version) — Actively improving

Feel free to fork, star, or open issues. Feedback is always welcome!

---

# تحلیل احساسات متون فارسی با استفاده از الگوریتم Random Forest

## ✨ معرفی
این پروژه یک سیستم **تحلیل احساسات** برای متون فارسی است که با استفاده از الگوریتم **یادگیری ماشین کلاسیک (Random Forest)** توسعه داده شده است. مدل آموزش‌دیده توانایی طبقه‌بندی جملات فارسی به دو احساس اصلی `شاد` و `غمگین` را دارد.

هدف از این پروژه، نمایش مهارت‌های عملی در زمینه‌ی **پیش‌پردازش زبان طبیعی (NLP)**، **توسعه مدل**، **ارزیابی مدل** و **آماده‌سازی برای استقرار** است. این پروژه برای استفاده در رزومه و یافتن فرصت کارآموزی در زمینه‌ی **دیتا ساینس** یا **یادگیری ماشین** طراحی شده است.

---

## 🔧 ویژگی‌ها
- پشتیبانی کامل از زبان فارسی با پیش‌پردازش اختصاصی
- طبقه‌بندی دوتایی (`شاد`، `غمگین`) با استفاده از Random Forest
- پاک‌سازی ایموجی‌ها و کاراکترهای غیرضروری
- ارزیابی مدل با استفاده از ماتریس آشفتگی، precision، recall و f1-score
- ذخیره مدل به صورت فایل Pickle برای استفاده در بک‌اند وب (مانند Flask یا Django)

---

## 📊 نتایج
- دقت مدل روی داده‌های تست: حدود ۸۳٪
- دقت مدل روی داده‌های آموزش: حدود ۸۷٪
- مدل دچار بیش‌برازش نیست
- عملکرد متوازن بین کلاس‌ها

ماتریس آشفتگی (داده‌های تست):
```
[[5317 1642]
 [ 699 5971]]
```

گزارش ارزیابی (داده‌های تست):
```
              precision    recall  f1-score   support

    happy       0.88      0.76      0.82      6959
      sad       0.78      0.90      0.84      6670

  accuracy                           0.83     13629
 macro avg       0.83      0.83      0.83     13629
weighted avg     0.84      0.83      0.83     13629
```

---

## 🧳 فناوری‌های مورد استفاده
- Python 3.10
- Pandas، NumPy
- scikit-learn
- hazm (پردازش زبان طبیعی فارسی)
- emoji (برای پاک‌سازی ایموجی‌ها)

---

## 📚 دیتاست
به دلیل محدودیت‌ها، دیتاست از منابع مختلف گردآوری و به صورت دستی پاک‌سازی شده است. فقط دو کلاس اصلی (`شاد`، `غمگین`) برای آموزش استفاده شده‌اند. ایموجی‌ها در مرحله پیش‌پردازش حذف شده‌اند.

---

## ⚙️ نحوه اجرا
```bash
# نصب وابستگی‌ها
pip install -r requirements.txt

# اجرای آموزش مدل (شامل ارزیابی)
python main.py
```

مدل آموزش‌دیده به صورت فایل pickle ذخیره خواهد شد و می‌توان آن را در بک‌اندهای وب مانند Flask یا Django استفاده کرد.

---

## 📊 بهبودهای آینده
- افزودن کلاس‌های احساسی بیشتر (مانند: عصبانیت، شگفتی، ترس)
- استفاده از مدل‌های یادگیری عمیق مانند ParsBERT
- ایجاد API با Flask یا Django
- طراحی رابط کاربری وب برای تحلیل احساسات در لحظه

---

## 🌟 درباره من
من یک **توسعه‌دهنده علاقه‌مند به یادگیری ماشین** هستم که به دنبال فرصت‌های کارآموزی هستم. این پروژه بخشی از مسیر یادگیری و رزومه شخصی من است. علاقه‌مند به ساخت برنامه‌های کاربردی واقعی با استفاده از AI/NLP هستم.

---

## 📅 وضعیت پروژه
✅ نسخه اول کامل شده — در حال بهبود مداوم

خوشحال می‌شوم پروژه را fork کنید، ستاره بزنید یا بازخورد بدهید!

