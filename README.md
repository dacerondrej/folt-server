# folt-server
Server has been created for the final project in PV207 Businnes Process Management course taught at Faculty of Informatics, Masaryk University, Brno.

Technologies used: Python Django, PostgreSQL, Docker in deployment

## To run the project follow instructions below
1. Create virtual environment: `python3 -m venv <CUSTOM_ENV_NAME>`
2. Run virtual environment: `source ./<CUSTOM_ENV_NAME>/bin/activate`
3. Clone this repository
4. Move to it: `cd folt/`
5. Change database settings in `folt/settings.py` according to your PostgreSQL DB:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '<YOUR_DB_NAME>',
        'USER': '<YOUR_DB_USER>',
        'PASSWORD': '<YOUR_DB_USER_PASSWORD>',
        'HOST': os.environ.get('POSTGRES_HOST', 'localhost'),
        'PORT': os.environ['POSTGRES_PORT'] if 'POSTGRES_PORT' in os.environ else '',
        'USE_TZ': None,
    }
}
```
6. Make migrations to your DB: `python3 manage.py makemigrations`
7. Migrate to your DB: `python3 manage.py migrate`
8. Create super user: `python3 manage.py createsuperuser`
9. Run the server: `python3 manage.py runserver`

Exit the environment by running: `deactivate` 

## Endpoints
- `/folt/last-offer`
- `/folt/couriers`
- `/folt/pickups`
- `/folt/ntr/checkSubject`
