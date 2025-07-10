# 🤖 SmartCabello IA

**SmartCabello IA** is a lightweight AI-powered tool that estimates hair length and suggests salon pricing based on a single uploaded photo. Built for real-world use at [BB27 Studio](https://bb27studio.com), it's optimized for mobile and integrated directly into the salon's website.

---

## 🚀 Live Demo

👉 [Try it now on BB27Studio.com](https://bb27studio.com/smartcabello-ai)

---

## 📸 What It Does

- Detects if hair is **short**, **medium**, or **long**
- Returns a **confidence score** and price estimate in MXN
- Works instantly — no login, no loading spinner
- Built with TensorFlow and Gradio for a smooth UX
- Fully mobile-responsive for Android/iOS users

---

## 🧠 Tech Stack

| Layer        | Tool / Library      |
| ------------ | ------------------- |
| AI Model     | `TensorFlow`, `NumPy`, `Pillow` |
| Frontend     | `Gradio Interface`  |
| Deployment   | Embedded on `bb27studio.com` via `<iframe>` |
| Data         | Labeled hair-length images (not included in repo) |

---

## 🔧 How It Works

1. User uploads a photo of their hair (any clear angle)
2. The image is preprocessed (resized, normalized)
3. Model classifies into one of three length categories
4. A price is displayed instantly based on the result

---

## 🧪 Example Predictions

| Hair Length | Confidence | Price    |
| ----------- | ---------- | -------- |
| Corto       | 94%        | $850 MXN |
| Medio       | 89%        | $1050 MXN |
| Largo       | 97%        | $1250 MXN |

---

## 🧹 Dataset

The training dataset was built by scraping and curating real-world hair images across three categories: Short (corto), Medium (medio), and Long (largo). I manually cleaned and verified the dataset to ensure clarity, diversity, and balanced distribution — critical for robust classification.

---

## 🛠️ Run Locally

```bash
git clone https://github.com/danielpinto-developer/smartcabello-ai.git
cd smartcabello-ai
pip install -r requirements.txt
python app.py
