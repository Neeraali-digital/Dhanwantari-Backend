# Dhanwantari Backend

A Django REST API backend for a hospital management system.

## Features

- **Appointment Management**: Schedule and manage patient appointments.
- **Blog System**: Publish and manage blog posts.
- **Contact Form**: Handle user contact messages.
- **Doctor Profiles**: Manage doctor information and profiles.
- **Image Gallery**: Upload and display gallery images.
- **Health Packages**: Define and manage health service packages.
- **Pharmacy Inventory**: Manage pharmacy items and stock.
- **Services**: List hospital services.
- **User Authentication**: JWT-based authentication with registration and profile management.
- **Admin Panel**: Django admin interface for data management.
- **API Documentation**: Swagger and Redoc documentation.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd Dhanwantari-Backend
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser (optional):
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

The API will be available at `http://127.0.0.1:8000/`.

## API Endpoints

### Authentication
- `POST /api/token/`: Obtain JWT token (login)
- `POST /api/token/refresh/`: Refresh JWT token
- `POST /api/register/`: Register a new user
- `GET/PUT /api/profile/`: Get/update user profile

### Data Endpoints (Require Authentication)
- `/api/appointments/`: Appointment management
- `/api/blogposts/`: Blog post management
- `/api/contactmessages/`: Contact message management
- `/api/doctors/`: Doctor profile management
- `/api/galleryimages/`: Image gallery management
- `/api/healthpackages/`: Health package management
- `/api/pharmacyitems/`: Pharmacy item management
- `/api/services/`: Service management

### Documentation
- Swagger UI: `http://127.0.0.1:8000/swagger/`
- Redoc: `http://127.0.0.1:8000/redoc/`

### Admin Panel
- `http://127.0.0.1:8000/admin/`

## Usage

1. Register a new user via `POST /api/register/`.
2. Obtain a JWT token via `POST /api/token/`.
3. Use the token in the `Authorization` header as `Bearer <token>` for authenticated requests.
4. Access the API endpoints as needed.

## Technologies Used

- Django
- Django REST Framework
- Simple JWT
- DRF Yasg (for API documentation)
- SQLite (database)

## Contributing

1. Fork the repository.
2. Create a feature branch.
3. Make your changes.
4. Submit a pull request.

## License

This project is licensed under the BSD License.
