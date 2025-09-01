Commands to run backend:

1) Create virtual environment to manage install packages seperating by using command:
  python -m venv venv

2) pip install -r requirements.txt

3) python manage.py makemigrations

4) python manage.py migrate







Herierchy


price_optimization_backend/
│── manage.py
│── requirements.txt
│── README.md
│── .env                        # DB credentials, secret keys, API keys
│
│── config/                     # Main project settings
│   ├── __init__.py
│   ├── settings.py             # Installed apps, DB, middleware
│   ├── urls.py                 # Root URL routing
│   ├── wsgi.py
│   └── asgi.py
│
│── apps/                       # Feature-based modular apps
│   │
│   ├── accounts/               # User management (Auth + Roles)
│   │   ├── models.py           # Custom User model (email login, roles)
│   │   ├── serializers.py      # User, Role serializers
│   │   ├── views.py            # Auth endpoints (Register, Login, Verify Email)
│   │   ├── urls.py
│   │   ├── permissions.py      # Role-based permissions
│   │   └── tests.py
│   │
│   ├── products/               # Product Management
│   │   ├── models.py           # Product model (name, category, cost, stock)
│   │   ├── serializers.py      # Product serializer
│   │   ├── views.py            # CRUD API endpoints
│   │   ├── urls.py
│   │   ├── filters.py          # Search + filter logic
│   │   └── tests.py
│   │
│   ├── demand/                 # Demand Forecast module
│   │   ├── models.py           # DemandForecast model (linked to Product)
│   │   ├── serializers.py
│   │   ├── views.py            # API to serve demand forecast data
│   │   ├── urls.py
│   │   └── utils.py            # Forecast calculation logic
│   │
│   ├── pricing/                # Pricing Optimization module
│   │   ├── models.py           # OptimizedPrice model
│   │   ├── serializers.py
│   │   ├── views.py            # Endpoint to return optimized price table
│   │   ├── urls.py
│   │   └── optimizer.py        # Core pricing optimization algorithm
│
│── common/                     # Shared utilities
│   ├── utils.py                # Common helper functions
│   ├── decorators.py           # Custom decorators for roles/permissions
│   ├── pagination.py           # Standard pagination for APIs
│   └── mixins.py
│
│── media/                      # For uploaded files (if needed)
│── static/                     # Static files
│
└── tests/                      # Centralized tests for integration



HTTP Method	URL Pattern (example: /api/products/)	Action in ViewSet
GET	/api/products/	list() → Get all products
POST	/api/products/	create() → Add a new product
GET	/api/products/{id}/	retrieve() → Get single product
PUT	/api/products/{id}/	update()
PATCH	/api/products/{id}/	partial_update()
DELETE	/api/products/{id}/	destroy()
