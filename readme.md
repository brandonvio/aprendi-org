# Aprendi.org - Multi-Organization Course Enrollment System

![Banner Image](https://aprendi.org/aprendi-logo.jpg)

Welcome to **Aprendi.org**, a cutting-edge system tailored for the administration and management of students, teachers, courses, and enrollments across multiple organizations.

---

### Table of Contents

- [Aprendi.org - Multi-Organization Course Enrollment System](#aprendiorg---multi-organization-course-enrollment-system)
    - [Table of Contents](#table-of-contents)
    - [Features](#features)
    - [Architecture Overview](#architecture-overview)
    - [Getting Started (not actual setup instructions... I'll update this soon to represent actual setup process...)](#getting-started-not-actual-setup-instructions-ill-update-this-soon-to-represent-actual-setup-process)
    - [Usage \& Endpoints](#usage--endpoints)
    - [Development \& Contributing](#development--contributing)
    - [License \& Credits](#license--credits)

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

![System Architecture Diagram](https://aprendi.org/aprendi-arch.png)

---

### Getting Started (not actual setup instructions... I'll update this soon to represent actual setup process...)

1. **Clone the Repository**
    ```bash
    git clone https://github.com/brandonvio/aprendi-org.git
    ```

2. **Setup the Infrastructure**
    Navigate to the Terraform directory and initialize + apply the configurations:
    ```bash
    cd terraform
    terraform init
    terraform apply
    ```

3. **Seed Data**
    Navigate to the Python seeder directory and run the seeding script:
    ```bash
    cd python_seeder
    python seeder.py
    ```

4. **Run the Admin App Locally**
    Navigate to the React application directory, install dependencies and start the development server:
    ```bash
    cd react_admin
    npm install
    npm start
    ```

---

### Usage & Endpoints

API documentation is extensively covered using Swagger. Get to know the API better by exploring the interactive documentation:

📖 [Aprendi API Docs](https://api.aprendi.org/docs/index.html)

---

### Development & Contributing

We're always open to feedback and contributions. Here's how you can contribute:

1. **Fork the Repository** - Create your own copy of `aprendi-org` on GitHub.

2. **Clone Your Fork** - Get your fork onto your local machine.

3. **Branch Out** - Create a new branch where you'll make your changes.

4. **Commit & Push** - Commit your changes and push to your fork.

5. **Create a Pull Request** - Once you're satisfied with your changes, create a PR against the main repository.

For more details on setting up the development environment and the contribution process, please see the [CONTRIBUTING.md](./CONTRIBUTING.md) file.

---

### License & Credits

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

Designed and developed with ❤️ by [Brandon Vicedomini](https://github.com/brandonvio).

---

Thank you for exploring **Aprendi.org**. We believe in the power of education, and we hope this system makes administration a little easier, and learning a lot more accessible.
