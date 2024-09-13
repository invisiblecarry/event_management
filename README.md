```markdown
# Event Management API

## Project Description

This is a REST API for managing events, allowing users to create, view, update, and delete events, as well as register users for events.

### Installation

1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Apply migrations:
   ```bash
   python manage.py migrate
   ```
4. Run the development server:
   ```bash
   python manage.py runserver
   ```

### Using Docker

1. Build and run the Docker container:
   ```bash
   docker-compose up --build
   ```

### API Endpoints

- `GET /events/` - Retrieve a list of events.
- `POST /events/` - Create a new event.
- `PUT /events/{id}/` - Update an existing event.
- `DELETE /events/{id}/` - Delete an event.
- `POST /registrations/` - Register a user for an event.

### Authorization

Authorization is handled using JWT tokens.

### API Documentation

For API documentation, you can use tools like Postman or Swagger UI, and the API should return a well-structured JSON response.
```

This version is concise and provides all necessary instructions in English. Let me know if you need any more changes!