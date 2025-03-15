# BookFinder

BookFinder is a professional-grade web application built with Django, designed to help users search for books, view detailed information, and manage their personal collections.

## Features

- Search for books by title, author, or genre
- View comprehensive book details
- Add books to a personal collection
- User authentication and account management
- Responsive and modern UI with Bootstrap
- Deployed on Railway for scalability

## Technologies Used

- Django (Python framework)
- PostgreSQL&#x20;
- Bootstrap (for responsive design)

## Installation

### Prerequisites

- Python (managed with Pyenv)
- Poetry (for dependency management)
- PostgreSQL (for production, optional for local development)

### Setup

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/bookfinder.git
   cd bookfinder
   ```

2. Set up the virtual environment and install dependencies:

   ```sh
   poetry install
   ```

3. Configure the environment variables:

   ```sh
   cp .env.example .env
   ```

   Update `.env` with your database credentials and API keys.

4. Apply migrations:

   ```sh
   poetry run python manage.py migrate
   ```

5. Create a superuser to access the admin panel:

   ```sh
   poetry run python manage.py createsuperuser
   ```

6. Run the development server:

   ```sh
   poetry run python manage.py runserver
   ```

7. Access the application at `http://127.0.0.1:8000/`.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with improvements or feature requests.

## License

This project is licensed under the MIT License.

## Contact

For any inquiries, contact [mouradanilo061@gmail.com](mailto\:your-email@example.com) or visit the repository at [GitHub Link](https://github.com/DaniDMoura).

