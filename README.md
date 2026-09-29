# AI BlogNest API

A simple and beginner-friendly REST API for managing blogs, built using **Python, FastAPI, and SQLite**. The project also includes an AI-powered blog summarization feature.

## Project Overview

**AI BlogNest API** is a backend application that allows users to create, view, update, delete, and manage blog posts through REST API endpoints.

The project also provides an AI summary feature that generates a short summary from blog content and calculates the total word count.

## Features

* Create a new blog
* View all blogs
* View a single blog
* Update an existing blog
* Delete a blog
* AI-powered blog summarization
* Word count for blog content
* SQLite database
* Interactive Swagger API documentation
* Health check endpoint

## Technologies Used

* Python
* FastAPI
* SQLAlchemy
* SQLite
* Pydantic
* Uvicorn
* Git
* GitHub

## Project Structure

```text
AI BLOGNEST API/
│
├── main.py
├── database.py
├── models.py
├── ai.py
├── .gitignore
└── README.md
```

## API Endpoints

### Home

```http
GET /
```

Returns a welcome message.

### Health Check

```http
GET /health
```

Checks whether the API is running.

### Create Blog

```http
POST /blogs
```

Creates a new blog.

Example request:

```json
{
  "title": "AI BlogNest",
  "content": "Artificial intelligence is helping developers build modern applications.",
  "author": "Shahira",
  "category": "Technology"
}
```

### Get All Blogs

```http
GET /blogs
```

Returns all available blogs.

### Get Single Blog

```http
GET /blogs/{blog_id}
```

Returns a specific blog using its ID.

Example:

```http
GET /blogs/1
```

### Update Blog

```http
PUT /blogs/{blog_id}
```

Updates an existing blog.

### Delete Blog

```http
DELETE /blogs/{blog_id}
```

Deletes a blog using its ID.

## AI Feature

### Blog Summarization

```http
POST /ai/summarize
```

This endpoint processes blog content and generates a short summary along with the word count.

Example request:

```json
{
  "content": "Artificial intelligence is changing the way people create software. AI tools help developers write code, analyze information, automate tasks, and build applications faster."
}
```

Example response:

```json
{
  "summary": "Artificial intelligence is changing the way people create software. AI tools help developers write code, analyze information, automate tasks, and build applications faster.",
  "word_count": 23,
  "message": "Blog summary generated successfully"
}
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/24bca018-byte/AI-BLOGNEST-API.git
```

### 2. Open the project folder

```bash
cd AI-BLOGNEST-API
```

### 3. Install required packages

```bash
python -m pip install fastapi uvicorn sqlalchemy pydantic
```

## Running the Application

Start the FastAPI server using:

```bash
python -m uvicorn main:app --reload
```

The application will run at:

```text
http://127.0.0.1:8000
```

## Swagger API Documentation

FastAPI provides interactive API documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

From Swagger UI, you can test all available API endpoints.

## Database

The project uses **SQLite** as the database.

The database file is created automatically when the application starts.

Database:

```text
blognest.db
```

## Testing

The following features were tested successfully:

* Home endpoint
* Health check
* Create blog
* Get all blogs
* Get single blog
* Update blog
* Delete blog
* AI blog summarization
* Word count

## Future Enhancements

The project can be extended with:

* User authentication
* JWT login
* Blog comments
* Blog likes
* Advanced search
* Categories and tags
* Real AI/LLM integration
* Image upload
* Cloud database
* Deployment to a cloud platform

## Project Information

**Project Name:** AI BlogNest API

**Course:** AI Augmented Backend Development - A & S

**Program:** BCA

**College:** Mohamad Sathak College of Arts and Science

## Author

**Shahira Banu**

---

## Conclusion

AI BlogNest API demonstrates how a modern backend application can be developed using Python and FastAPI. It provides RESTful blog management operations, database integration, interactive API documentation, and an AI-based content summarization feature.
