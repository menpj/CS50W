
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': 'db',
        'PORT': 5432,
    }
}


CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
CMD ["./wait-for-it.sh", "db:5432", "--", "python3", "manage.py", "runserver", "0.0.0.0:8000"]   


version: '3'

services:
    db:
       
        
        
        image:  postgres
        environment:
            POSTGRES_DB: postgres
            POSTGRES_USER: postgres
            POSTGRES_PASSWORD: password



        
    web:
        tty: true
        command: python3 manage.py runserver 0.0.0.0:8000
        build:  .
        volumes:
            - .:/usr/src/app
        ports:
            - "8000:8000"

        
        networks:
          - internal_network

        environment:
            POSTGRES_USER: postgres
            POSTGRES_PASSWORD: password
            POSTGRES_HOST: db
        depends_on:
            - db
            - migration
