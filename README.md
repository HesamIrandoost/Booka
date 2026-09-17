# 📚 Booka

> A Goodreads / IMDb-inspired platform for discovering books, sharing reviews, rating books, and building personal collections.

**Booka** is a backend-focused book platform built with **Django and Django REST Framework**.

The goal of this project is to build a realistic REST API where users can discover books, explore authors and genres, rate and review books, reply to reviews, like reviews, and create personal book collections.

---

## 🚀 Project Status

> 🟡 **In Development**

Booka is being developed step by step as a real-world Django REST API project.

### Current

* [x] Custom User Model
* [x] Author model
* [x] Book model
* [x] Genre model
* [x] Review system
* [x] Review replies
* [x] Book rating calculation
* [x] User collections
* [x] Public / private collections
* [x] Seed data command
* [x] Book serializer
* [x] All Books API
* [x] Pagination

### Coming Soon

* [ ] Book detail API
* [ ] Search
* [ ] Filtering
* [ ] Ordering
* [ ] Review API
* [ ] Review likes
* [ ] Collection API
* [ ] Authentication
* [ ] Permissions
* [ ] User profile API
* [ ] API documentation
* [ ] Automated tests
* [ ] Query optimization
* [ ] Docker
* [ ] Production deployment

---

# ✨ Features

## 📖 Books

Users will be able to:

* Browse books
* View detailed book information
* Explore authors
* Explore genres
* Search books
* Filter books
* Sort books
* View book ratings

Each book contains information such as:

* Title
* Slug
* Cover
* Author
* Genres
* Description
* Summary
* Number of pages
* Publisher
* Publication date
* Average rating

---

## 👤 Users

Booka uses a custom Django User model.

Users will eventually be able to:

* Register
* Login
* Manage their profile
* Review books
* Rate books
* Create collections
* Like reviews
* Reply to reviews

---

## ⭐ Reviews & Ratings

Users can review books and give them a rating from **1 to 5 stars**.

Reviews support:

* Subject
* Text
* Star rating
* Likes
* Replies
* Creation date
* Active / inactive status

Book ratings are calculated from the ratings of the main reviews.

Replies are **not included** in the book's average rating.

---

## 💬 Review Replies

Reviews support self-referencing replies.

Example:

```text
Review
│
├── Reply
├── Reply
└── Reply
```

This allows users to have discussions around a book review.

---

## 📚 Collections

Users can create their own book collections.

Examples:

```text
My Favorite Books
Books I Want to Read
Best Classics
My Favorite Fantasy Books
Books That Changed My Perspective
```

Collections support:

* Title
* Description
* Cover
* Books
* Owner
* Public / private visibility
* Creation date

---

# 🏗️ Project Architecture

The project follows Django's application-based architecture.

```text
Booka/
│
├── core/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── book/
│   ├── migrations/
│   ├── management/
│   │   └── commands/
│   │       └── seed_data.py
│   │
│   ├── admin.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── pagination.py
│   ├── urls.py
│   └── ...
│
├── account/
│   └── ...
│
├── manage.py
├── requirements.txt
└── README.md
```

---

# 🗄️ Data Model

The core relationships currently look like this:

```text
                         ┌─────────────┐
                         │    User     │
                         └──────┬──────┘
                                │
              ┌─────────────────┼─────────────────┐
              │                 │                 │
              ▼                 ▼                 ▼
          Reviews          Collections         Profile
              │                 │
              │                 │
              ▼                 ▼
            Book ◄──────────── Books
              │
       ┌──────┴──────┐
       │             │
       ▼             ▼
    Author         Genre
```

### Review relationships

```text
Book
 │
 ├── Review
 │    ├── Reply
 │    ├── Reply
 │    └── Reply
 │
 └── Review
```

---

# 🔌 API

The API is built using **Django REST Framework**.

### Books

```http
GET /api/books/
```

Returns a paginated list of books.

Example:

```http
GET /api/books/?page=1
```

Pagination currently uses **10 books per page**.

Example response:

```json
{
    "count": 15,
    "next": "http://127.0.0.1:8000/api/books/?page=2",
    "previous": null,
    "results": [
        {
            "id": 1,
            "title": "1984",
            "slug": "1984",
            "star": 4.3
        }
    ]
}
```

> More endpoints will be documented here as the API grows.

---

# 🧪 Development Data

Booka includes a custom Django management command for generating development data.

The seed command creates:

* 20 users
* Real-world book titles
* Real-world authors
* Genres
* Reviews
* Review replies
* Book ratings
* User collections

Run:

```bash
python manage.py seed_data
```

All generated users use:

```text
Password: Test12345
```

> The seed command is intended for development and testing only.

---

# 🛠️ Tech Stack

| Technology            | Purpose                     |
| --------------------- | --------------------------- |
| Python                | Programming language        |
| Django                | Web framework               |
| Django REST Framework | REST API                    |
| SQLite / PostgreSQL   | Database                    |
| Pillow                | Image processing            |
| Faker                 | Development data generation |
| Git                   | Version control             |

More technologies will be added as the project evolves.

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone <repository-url>
cd Booka
```

## 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

### Linux / macOS

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 4. Run migrations

```bash
python manage.py migrate
```

## 5. Create a superuser

```bash
python manage.py createsuperuser
```

## 6. Generate development data

```bash
python manage.py seed_data
```

## 7. Start the development server

```bash
python manage.py runserver
```

The API will be available at:

```text
http://127.0.0.1:8000/
```

---

# 🔐 Authentication

Authentication will be implemented using JWT.

Planned endpoints:

```text
POST /api/auth/register/
POST /api/auth/login/
POST /api/auth/refresh/
GET  /api/auth/me/
```

Authentication and authorization will be expanded as the project develops.

---

# 🔎 Planned API

The planned API structure is approximately:

```text
/api/
│
├── auth/
│   ├── register/
│   ├── login/
│   ├── refresh/
│   └── me/
│
├── books/
│   ├── GET /
│   ├── GET /<slug>/
│   ├── search/
│   └── filters/
│
├── authors/
│   ├── GET /
│   └── GET /<id>/
│
├── genres/
│   ├── GET /
│   └── GET /<id>/
│
├── reviews/
│   ├── GET /
│   ├── POST /
│   ├── PATCH /<id>/
│   └── DELETE /<id>/
│
└── collections/
    ├── GET /
    ├── POST /
    ├── PATCH /<id>/
    └── DELETE /<id>/
```

This structure may change during development.

---

# 📈 Development Roadmap

Booka is being developed progressively.

### Phase 1 — Core Models

* [x] User
* [x] Author
* [x] Book
* [x] Genre
* [x] Review
* [x] Collection

### Phase 2 — Basic API

* [x] Serializers
* [x] All Books endpoint
* [x] Pagination
* [ ] Book detail
* [ ] Author endpoints
* [ ] Genre endpoints

### Phase 3 — Discovery

* [ ] Search
* [ ] Filtering
* [ ] Ordering
* [ ] Advanced ORM queries
* [ ] Aggregations
* [ ] Annotations

### Phase 4 — User Interaction

* [ ] Authentication
* [ ] Permissions
* [ ] Create reviews
* [ ] Update reviews
* [ ] Delete reviews
* [ ] Review likes
* [ ] Replies
* [ ] Collections

### Phase 5 — Production Features

* [ ] PostgreSQL
* [ ] Redis
* [ ] Caching
* [ ] Celery
* [ ] API documentation
* [ ] Automated tests
* [ ] Query optimization
* [ ] Docker
* [ ] Nginx
* [ ] Deployment

---

# 🧠 Learning Goals

Booka is also a practical backend project for exploring professional Django development.

The project focuses on:

* Django ORM
* Django REST Framework
* Relational database design
* ForeignKey relationships
* Many-to-Many relationships
* Self-referencing relationships
* Serializers
* Generic API views
* Pagination
* Filtering
* Searching
* Permissions
* Authentication
* Signals
* Aggregation
* Annotation
* Query optimization
* Testing
* API architecture
* Production deployment

---

# 📌 Project Philosophy

Booka is intentionally being developed incrementally.

Instead of implementing every feature at once, each part of the API is built, tested, reviewed, and then expanded.

The goal is not only to make the application work, but to understand **why the architecture works** and how the same concepts apply to larger Django applications.

---

# 📄 License

This project is currently for educational and portfolio purposes.

