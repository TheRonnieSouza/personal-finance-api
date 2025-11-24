# 💰 Personal Finance API

> A modern FastAPI-based REST API for personal financial management, built with Python 3.12, SQLAlchemy, and PostgreSQL.

[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.114.0-009688.svg)](https://fastapi.tiangolo.com)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-13+-336791.svg)](https://www.postgresql.org)
[![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED.svg)](https://www.docker.com)

## 📋 Features

- ✅ **Transaction Management** - Create and retrieve financial transactions
- ✅ **Categories & Types** - Organize transactions by category (debit/credit)
- ✅ **PostgreSQL Integration** - Persistent data storage with SQLAlchemy ORM
- ✅ **FastAPI Framework** - Auto-generated OpenAPI documentation
- ✅ **Docker Support** - Containerized deployment ready
- ✅ **Environment Configuration** - Secure configuration with python-dotenv

## 🚀 Quick Start

### Prerequisites

- Python 3.12+
- PostgreSQL database
- Poetry
- Docker 

### 🛠️ Local Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/TheRonnieSouza/personal-finance-api.git
   cd personal-finance-api
   ```

2. **Install dependencies with Poetry**
   ```bash
   poetry install
   ```

3. **Configure environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your database connection string
   ```

4. **Activate virtual environment and run**
   ```bash
   poetry shell
   uvicorn src.financial_manager.main:app --reload
   ```

5. **Access the API**
   - API: http://localhost:8000
   - Documentation: http://localhost:8000/docs

### 🐳 Docker Deployment

1. **Build the image**
   ```bash
   docker build -t financial-api .
   ```

2. **Run the container**
   ```bash
   docker run -p 8000:8000 financial-api
   ```

## 📊 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Health check |
| `GET` | `/v1/transactions` | List all transactions |
| `POST` | `/v1/transactions` | Create new transaction |

### 📝 Transaction Schema

```json
{
  "date": "2025-10-15",
  "amount": 25.50,
  "currency": "BRL",
  "type": "debito",
  "category": "Mercado",
  "description": "Compras da semana"
}
```

## 🏗️ Project Structure

```
personal-finance-api/
├── src/
│   └── financial_manager/
│       └── main.py              # FastAPI application
├── Dockerfile                   # Container configuration
├── pyproject.toml              # Poetry dependencies
├── poetry.lock                 # Locked dependencies
├── .env                        # Environment variables
└── README.md                   # Project documentation
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
STRING_CONNECTION=postgresql+psycopg2://user:password@host:port/database
```

### Database Schema

The API automatically creates the following table:

```sql
CREATE TABLE app_transactions (
    id SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    amount NUMERIC(12,2) NOT NULL,
    currency VARCHAR(3) DEFAULT 'BRL',
    type VARCHAR(10) NOT NULL,
    description VARCHAR(255),
    category VARCHAR(50) NOT NULL
);
```
## 📚 Dependencies

- **FastAPI** - Modern web framework for APIs
- **SQLAlchemy** - SQL toolkit and ORM
- **psycopg2-binary** - PostgreSQL adapter
- **python-dotenv** - Environment variable loader
- **Uvicorn** - ASGI server for FastAPI


## 👨‍💻 Author

**Ronnie Souza**
- GitHub: [@TheRonnieSouza](https://github.com/TheRonnieSouza)

---

⭐ Star this repository if you find it helpful!

