# Aprendi.org - Multi-Organization Course Enrollment System

![Banner Image](https://aprendi.org/aprendi-logo.jpg)

Welcome to **Aprendi.org**, a cutting-edge system tailored for the administration and management of students, teachers, courses, and enrollments across multiple organizations.

---

### Table of Contents

- [Aprendi.org - Multi-Organization Course Enrollment System](#aprendiorg---multi-organization-course-enrollment-system)
    - [Table of Contents](#table-of-contents)
    - [Features](#features)
    - [Architecture Overview](#architecture-overview)
    - [Getting Started](#getting-started)
    - [Usage \& Endpoints](#usage--endpoints)

---

### Features

🔧 **Gin API on AWS Lambda** - Enjoy the performance benefits of the Gin framework, coupled with the scalability of AWS Lambda for all API requests.

🔷 **Single Table DynamoDB Design** - A streamlined database design for efficient read and write operations, minimizing costs and maximizing scalability.

⚙️ **CI/CD & GitHub Actions** - Continuous Integration and Continuous Deployment directly from GitHub, ensuring the latest and greatest version is always deployed after passing tests.

🌍 **100% Infrastructure in Terraform** - Complete IaC (Infrastructure as Code) principles have been embraced. Terraform scripts make it a breeze to set up or tear down the entire infrastructure.

🐍 **Python Application** - For seeding initial data and validating access patterns, ensuring the system is always populated and functional as expected.

⚛️ **React-Redux Admin Application** - A robust frontend designed in React with Redux for state management, offering administrators a seamless experience.

---

### Architecture Overview

The system is primarily hosted on AWS, utilizing services such as Lambda for serverless compute and DynamoDB for database management. Everything from the infrastructure to the application layer has been defined with precision, scalability, and robustness in mind.

---

### Getting Started

1. **Clone the Repository**
    ```bash
    git clone https://github.com/brandonvio/aprendi-org.git
    ```
---

### Usage & Endpoints

API documentation is extensively covered using Swagger. Get to know the API better by exploring the interactive documentation:

📖 [Aprendi API Docs](https://api.aprendi.org/docs/index.html)

---
Thank you for exploring **Aprendi.org**. We believe in the power of education, and we hope this system makes administration a little easier, and learning a lot more accessible.
