# Blimp Backend
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-cc0000?style=for-the-badge&logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)


This is the backend for the **Blimp** application, built with Flask with sqlalchemy orm connecting to mysql, containerized using Docker. For the frontend part, please take a look at [Blimp frontend](https://github.com/SreeHarshan/Blimp-frontend).

---

## 📦 Features

- Clean Flask code with blueprints
- SqlAlchemy ORM
- Dockerized for consistent deployment

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/SreeHarshan/Blimp-backend
cd Blimp-backend
```

---

### 2. Build and Run

```bash
docker build -t blimp-backend .
docker run -d -p 8004:8004 --name blimp-flask blimp-backend
```
**Note**
- The server runs on port 8004 and ip of 0.0.0.0, if you want to change the port or ip of server you can pass the port, ip as an env variable to docker by adding `docker run -e PORT=xxxx HOST=xxx.xxx.x.x ...`.
  

Thank you for a taking a look at this 😊
---
