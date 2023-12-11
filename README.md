# San Francisco Food Trucks Locator

The San Francisco Food Trucks Locator project allows users to find the five nearest food trucks in San Francisco based on their current location or manually entered geographical data.

## Requirements

- Python 3.11
- pip
- Virtualenv (optional)

## Installation

1. Clone the repository:

```sh
git clone https://github.com/pf-github-pl/P1-django-take-home-assignment.git
cd P1-django-take-home-assignment
```

2. (Optional) Create and activate a virtual environment:

```sh
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install the required dependencies:

```sh
pip install -r requirements/local.txt
```

## Running the Project

1. Prepare the database:

```sh
python manage.py migrate
```

2. Load the food trucks data:

```sh
python manage.py loaddata main/fixtures/food_trucks.json
```

3. Start the development server:

```sh
python manage.py runserver
```

Now, the application should be accessible at [http://localhost:8000](http://localhost:8000).

## If I had more time...
1. I would have added tests to the project. I would have used pytest and pytest-django to write unit tests for the models and views. I would have also used Selenium to write integration tests for the frontend.
2. I would have added a map to the frontend. I would have used Google Maps API to display the food trucks on a map.
3. I would Dockerize the project. I would have used Docker Compose to run the project in a containerized environment.
4. I would have added a CI/CD pipeline to the project. I would have used GitHub Actions to run the tests and build the Docker image.
