
# School API 1


## Student Model
In this assignment we will create a Student Django Model with the following fields

| field            | required |type |example data                    |
| ----------------- | -----|-------|------------- |
| name | True |string | John W. Watson |
| student_email | True | string | johnnyBoy@school.com |
| personal_email | False | string | johnnyBoy@gmail.com |
| locker_number | True |int |137 |
| locker_combination | True |string |37-68-98 |
| good_student | True |boolean | True |


## Django Set Up

Creating and activating VENV

```bash
  #creating venv
  python -m venv <name_of_env>

  #activating venv
  source <name_of_env>/bin/activate
```

Installing Django and starting a project with an app

```bash
    #installing Django
    pip install django

    #creating project
    django-admin startproject school_proj .

    #creating student app
    python manage.py startapp student_app
```

Creating Database

```yaml
# docker-compose.yml
version: '3'
services:
  db:
    image: postgres:15
    environment:
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
      - POSTGRES_DB=school_db
    ports:
      - '5454:5432'
    volumes: 
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```
run:
```bash
docker compose up
```
**Don't forget to add the app under the `INSTALLED_APPS` section in `settings.py` and changing from sqlite to postgresql with a database name!**

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "school_db",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "localhost",  
        "PORT": 5454, # This is the port on the host machine (which will be mapped to 5432 in the container)
    }
}
```

Installing Psycopg3 to speak with PostgreSQL

```bash
  pip install "psycopg[binary]"
```

Once the Student Model is completed makemigrations and migrate to the school_db

```bash
  python manage.py makemigrations
  python manage.py migrate
```

## Running Tests

Replace the `test.py` file inside your app with the `test.py` file already attached to this repository. 

Now you can run the test suite by typing the following

```bash
  python manage.py test
```

- `.` means a test passed
- `E` means an unhandled error populated on a test
- `F` means a test completely failed to run
