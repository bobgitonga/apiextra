 Features
CRUD Operations for Movies, Showtimes, and Bookings.
Relationships:
Movies have multiple Showtimes.
Showtimes can have multiple Bookings.
Filtering and Searching: Filter movies by title, genre, and showtimes.
Pagination: Paginated responses for list endpoints.
Secure API Endpoints: User authentication can be added if needed.
 Setup and Installation
 1. Clone the Repository
bash
Copy code
git clone <repo_url>
cd movie_booking
 2. Create a Virtual Environment and Install Dependencies
bash
Copy code
python -m venv venv
source venv/bin/activate  # On MacOS/Linux
venv\Scripts\activate     # On Windows

pip install django djangorestframework
 3. Apply Migrations
bash
Copy code
python manage.py makemigrations
python manage.py migrate 4. Create a Superuser (Optional)
bash
Copy code
python manage.py createsuperuser
 5. Run the Development Server
bash
Copy code
python manage.py runserver
Visit http://127.0.0.1:8000/api/ in your browser.

 API Endpoints
 Movies
Method	Endpoint	Description
GET	/api/movies/	List all movies
GET	/api/movies/{id}/	Retrieve a movie
POST	/api/movies/	Create a new movie
PUT	/api/movies/{id}/	Update a movie
DELETE	/api/movies/{id}/	Delete a movie
 Showtimes
Method	Endpoint	Description
GET	/api/showtimes/	List all showtimes
GET	/api/showtimes/{id}/	Retrieve a showtime
POST	/api/showtimes/	Create a new showtime
PUT	/api/showtimes/{id}/	Update a showtime
DELETE	/api/showtimes/{id}/	Delete a showtime
 Bookings
Method	Endpoint	Description
GET	/api/bookings/	List all bookings
GET	/api/bookings/{id}/	Retrieve a booking
POST	/api/bookings/	Create a new booking
PUT	/api/bookings/{id}/	Update a booking
DELETE	/api/bookings/{id}/	Delete a booking
⚙ Project Structure
bash
Copy code
movie_booking/
│
├── bookings/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py        # Admin configurations
│   ├── apps.py         # App configurations
│   ├── models.py       # Data models
│   ├── serializers.py  # API serializers
│   ├── views.py        # API viewsets
│   ├── urls.py         # App-level routing
│   └── tests.py        # Unit tests
│
├── movie_booking/
│   ├── __init__.py
│   ├── settings.py     # Project settings
│   ├── urls.py         # Root-level routing
│   ├── wsgi.py         # Deployment entry point
│
├── db.sqlite3          # Database (Development)
├── manage.py           # Django management tool
├── README.md           # Documentation
└── requirements.txt    # Dependencies
 Environment Variables
Create a .env file in the project root directory and add:

env
Copy code
SECRET_KEY='your-secret-key'
DEBUG=True
 Testing the API
Using curl
bash
Copy code
curl http://127.0.0.1:8000/api/movies/
Using Postman
Import the API endpoints into Postman.
Test each CRUD operation.
 Pagination and Filtering
Pagination: Enabled by default with 10 items per page.
Filtering: Use query parameters, e.g.,
/api/movies/?search=action
/api/showtimes/?search=hall1
 Running Tests
Run unit tests to ensure everything is working:

bash
Copy code
python manage.py test
 Deployment
Configure ALLOWED_HOSTS in settings.py.
Use Gunicorn and nginx for deployment:
bash
Copy code
pip install gunicorn
gunicorn movie_booking.wsgi:application --bind 0.0.0.0:8000
 Contributing
Fork the repository.
Create a new branch: git checkout -b feature-new
Commit your changes: git commit -m "Add new feature"
Push to the branch: git push origin feature-new
Open a Pull Request.
 License
This project is licensed under the MIT License.

Contact
Author: Robert Waitere Gitonga
