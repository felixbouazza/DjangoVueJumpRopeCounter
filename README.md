# DjangoVueJumpRopeCounter

## Install Work Environment

- [x] Create a virtual environment and activate it
- [x] Install Django and librairies
  - [x] Djoser ( Authentification library )
  - [x] Django Rest Framework ( Building API )
  - [x] Django Cors Headers ( Handling the server headers Cross-Origin Resource Sharing )
- [x] Create a new Django Project
- [x] Configure the project
- [x] Add Djoser urls to the urls file

- [x] Install Vue CLI
- [x] Create a new Vue project
- [x] Install axios ( Easy talking with the backend )

#### Django

```bash
virtualenv env
source env/bin/activate
pip install django djoser django-rest-framework django-cors-headers
django-admin startproject backend
```

###### backend/backend/settings.py

```python
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",
    "http://127.0.0.1:8000"
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication'
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated'
    )
}

INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework.authtoken',

    'djoser',
    'corsheaders'
]


MIDDLEWARE = [
    ...
    'django.middleware.common.CommonMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]
```

###### backend/backend/urls.py

```python
...
from django.urls import path, include

urlpatterns = [
    ...
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken'))
]
```

###### Database migration

```bash
python manage.py migrate
python manage.py runserver
```

#### Vue

```bash
sudo npm install -g @vue/cli
vue create frontend
cd frontend
npm install axios
```

###### frontend/src/main.js

```javascript
...
import axios from "axios";

axios.defaults.baseURL = "http://127.0.0.1:8000";

createApp(App).use(store).use(router, axios).mount("#app");
```
