# 🔗 URL Shortener

A simple and efficient **URL Shortener** web application developed using **Python**, **Flask**, and **SQLite**. The application converts long URLs into short, unique, and easy-to-share links while providing fast redirection to the original URL.

---

## 📌 Project Overview

Long URLs are difficult to share, remember, and manage. This project provides a lightweight solution by generating unique short URLs and storing their mappings in a SQLite database. Users can access the original website by simply opening the generated short URL.

---

## ✨ Features

- Generate unique short URLs
- URL validation before processing
- Automatic URL redirection
- SQLite database integration
- Fast and lightweight application
- Simple and responsive user interface
- Error handling for invalid URLs

---

## 🛠️ Technologies Used

- Python 3.x
- Flask
- SQLite
- HTML5
- CSS3
- Jinja2 Templates
- Validators Library

---

## 📂 Project Structure

```
URL-Shortener/
│
├── app.py
├── urls.db
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── screenshots/
    ├── home.png
    ├── short_url.png
    └── redirect.png
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/upskillcampus.git
```

### Navigate to the Project

```bash
cd upskillcampus
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000/
```

---

## 🚀 How It Works

1. Enter a valid long URL.
2. Click the **Shorten URL** button.
3. The system validates the URL.
4. A unique short code is generated.
5. The mapping is stored in the SQLite database.
6. A shortened URL is displayed.
7. Opening the short URL redirects the user to the original website.

---

## 🗄️ Database

SQLite database stores the following information:

| Field | Description |
|--------|-------------|
| id | Primary Key |
| original_url | Original Long URL |
| short_code | Generated Unique Code |

---

## 🧪 Testing

The application has been tested for:

- Valid URL generation
- Invalid URL handling
- Database storage
- URL redirection
- Multiple URL generation
- Performance and reliability

---

## 📈 Future Enhancements

- User Login & Authentication
- Custom Short URLs
- QR Code Generation
- Click Analytics
- Link Expiration
- REST API Support
- Cloud Deployment
- Admin Dashboard
- Enhanced Security

---

## 👨‍💻 Author

**Aditya Kumar**

Python Internship Project

upskill Campus

---

## 📚 References

- Python Documentation – https://docs.python.org/3/
- Flask Documentation – https://flask.palletsprojects.com/
- SQLite Documentation – https://www.sqlite.org/
- MDN Web Docs – https://developer.mozilla.org/

---

## 📄 License

This project is developed for **educational and internship purposes** under the **Python Internship Program** conducted by **upskill Campus**.
