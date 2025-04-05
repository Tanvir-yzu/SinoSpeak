# SinoSpeak

SinoSpeak is a Django-based project designed to provide a robust platform for language learning and interaction.

## Features
- Admin panel styled with Jazzmin.
- Core application for managing the main functionality.
- Extended utilities with `django_extensions`.

## Requirements
- Python 3.8+
- Django 5.1.7
- SQLite (default database)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd SinoSpeak
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. Run the development server:
   ```bash
   python manage.py runserver_plus
   ```
6. Language configuration

   - In the `settings.py` file, set the `LANGUAGE_CODE` to your desired language code
   ```bash
   python manage.py makemessages -l zh_Hans
   ```
   ```bash
   python manage.py compilemessages
   ```
   ```bash
   {% trans "版权所有。" %}
   ```
   ```bash
   black list
   ```
## Usage

- Access the application at `http://127.0.0.1:8000/`.
- Use the Django admin panel at `http://127.0.0.1:8000/admin/`.

## Development

To start developing, ensure `DEBUG` is set to `True` in `settings.py`. For production, set `DEBUG` to `False` and configure `ALLOWED_HOSTS`.

## Contributing

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.