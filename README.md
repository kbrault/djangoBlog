# Django Blog Boilerplate

This is a simple Django blog boilerplate project that uses Docker for easy setup and deployment. It features a basic blog interface, with posts created through the default Django admin interface. Ideal for quick deployment and development, this boilerplate provides a straightforward blogging platform that you can easily extend and customize.

![djangoblog](https://raw.githubusercontent.com/kbrault/djangoBlog/refs/heads/main/djangoblog.png)


> **Work in progress**
```
TODO :
- Security
- Markdown support
- Comments
- Others pages
- SEO
```

## Features

- Basic blog setup using Django
- Default Django admin interface for creating and managing posts
- Dockerized environment for simple, consistent setup
- Easy deployment with Docker Compose

## Quick Start

### Prerequisites

Make sure you have the following installed on your machine:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/django-blog-boilerplate.git
   cd django-blog-boilerplate
    ```

2. **Modify the .env file:**
    ```bash
    nano .env
    ```
    By default, the superuser is set to root/root, you must modify it : 
    - ``SECRET_KEY`` This is used to provide cryptographic signing, and should be set to a unique, unpredictable value.
    - ``SUPER_USER_NAME`` Login of the superuser
    - ``SUPER_USER_PASSWORD`` Password of the superuser
    - ``SUPER_USER_EMAIL`` Email of the superuser

3. **Build the project:**
    ```bash
    docker compose up -d
    ```
    It automaticaly :
    - Runs ``makemigration`` to creates new migrations based on changes you've made to your Django models.
    - Runs ``migration`` to applies migrations to the database, executing SQL commands to update the database schema.
    - Runs ``collectstatic`` gathers all static files (CSS, JavaScript, images) from your app and places them in a single directory, specified in ``STATIC_ROOT``.

4. **Access the application:**

    - The blog should be accessible at ``http://0.0.0.0:8000``.
    - The Django admin interface is available at ``http://0.0.0.0:8000/admin``.

### Docker Services
This boilerplate contains the following Docker services:

- ``django_gunicorn``: The main Django application server running on Gunicorn.
- ``nginx``: NGINX serves as a reverse proxy for the application.

### External Services
This boilerplate contains the following Docker services:

- ``Bootstrap css``: Bootstrap CSS is a front-end framework that simplifies web development by providing responsive design, pre-built components, and a customizable grid system.

### Volumes

Persistent data is stored in the following Docker volumes:

- ``djangoblog_static:`` Stores static files.
- ``djangoblog_db``: Stores database data.

### License

This project is licensed under the MIT License. See the LICENSE file for details.

### Contributing

Feel free to submit issues or pull requests. Contributions are welcome!