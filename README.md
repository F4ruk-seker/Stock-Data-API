# Financial Stock Tracking Application

This project aims to develop an application for tracking financial stock data. The application is structured using a Django backend and a Vue.js frontend, both of which can be run using Docker for seamless development and deployment.

## Project Structure

```
├── backend/        # Django-based backend project
├── frontend/       # Vue.js-based frontend project
├── README.md       # General information and setup instructions
```

## Phase 1 Overview

In the first phase of development, we focus on setting up the foundational structure of the application. This includes the following:

### Features

- **User Authentication:** Implement user registration and login functionalities.
- **Stock Data Management:** Create models to handle stock data, including stock symbols, prices, and historical data.
- **Basic UI:** Develop a user interface for displaying stock information and charts.

### Technologies Used

- **Backend:** Django REST Framework for API development.
- **Frontend:** Vue.js for creating an interactive user interface.
- **Database:** PostgreSQL for data storage.
- **Containerization:** Docker for easy deployment and environment management.

### Docker Setup

To run the application using Docker, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/F4ruk-seker/Stock-Data-API.git
   cd Stock-Data-API
   ```

2. **Navigate to the backend directory and build the Docker image:**
   ```bash
   cd backend
   docker build -t stock-tracking-backend .
   ```

3. **Navigate to the frontend directory and build the Docker image:**
   ```bash
   cd ../frontend
   docker build -t stock-tracking-frontend .
   ```

4. **Run the Docker containers:**
   - Start the backend service:
     ```bash
     docker run -d -p 8000:8000 stock-tracking-backend
     ```
   - Start the frontend service:
     ```bash
     docker run -d -p 8080:8080 stock-tracking-frontend
     ```

### Accessing the Application

- The backend API will be accessible at `http://localhost:8000/`.
- The frontend application will be accessible at `http://localhost:8080/`.

### Next Steps

In the upcoming phases, we will enhance the application with additional features such as:

- Real-time stock updates.
- User portfolio management.
- Advanced data visualization.

---

Feel free to adjust any sections as needed!

---

### frame

```dir
+---backend
|   |   .env.example
|   |   .gitignore
|   |   celerybeat-schedule.bak
|   |   celerybeat-schedule.dat
|   |   celerybeat-schedule.dir
|   |   check_requirements.py
|   |   docker-compose.yml
|   |   Dockerfile
|   |   git-config.ini
|   |   LICENSE
|   |   manage.py
|   |   manage_product.py
|   |   manage_test.py
|   |   rabitmq-test.py
|   |   README.md
|   |   requirements.txt
|   |   requirements_backup.txt
|   |   requirements_docker.txt
|   |   task_results.txt
|   |   testdata.json
|   |   trash.py
|   |   
|   +---api
|   |       urls.py
|   |       
|   +---asset
|   |   |   admin.py
|   |   |   apps.py
|   |   |   views.py
|   |   |   __init__.py
|   |   |   
|   |   +---api
|   |   |   |   urls.py
|   |   |   |   
|   |   |   +---serializers
|   |   |   |       active_public_asset_serializer.py
|   |   |   |       assets_only_code_name_serializer.py
|   |   |   |       asset_detail_serializer.py
|   |   |   |       asset_ownership_serializer.py
|   |   |   |       asset_price_flow_serializer.py
|   |   |   |       asset_serializer.py
|   |   |   |       favorite_serializer.py
|   |   |   |       slot_serializer.py
|   |   |   |       __init__.py
|   |   |   |       
|   |   |   \---views
|   |   |           active_public_asset_bulk_create_update_view.py
|   |   |           assets_list_view.py
|   |   |           assets_summary_list_view.py
|   |   |           asset_bulk__create_update_view.py
|   |   |           asset_detail_view.py
|   |   |           asset_owner_list_view.py
|   |   |           favorite_asset_add_remove_view.py
|   |   |           favorite_asset_view.py
|   |   |           slot_create_view.py
|   |   |           slot_retrieve_update_destroy_view.py
|   |   |           __init__.py
|   |   |           
|   |   +---management
|   |   |   \---commands
|   |   |           load_asset_data.py
|   |   |           
|   |   +---migrations
|   |   |       0001_initial.py
|   |   |       __init__.py
|   |   |       
|   |   +---models
|   |   |   |   active_public_asseting_model.py
|   |   |   |   asset_model.py
|   |   |   |   asset_ownership_model.py
|   |   |   |   favorite_asset_model.py
|   |   |   |   slot_model.py
|   |   |   |   __init__.py
|   |   |   |   
|   |   |   \---utils
|   |   |           parse_percentage.py
|   |   |           price_parser.py
|   |   |           __init__.py
|   |   |           
|   |   +---signals
|   |   |       active_public_asseting_signals.py
|   |   |       asset_model_signal.py
|   |   |       __init__.py
|   |   |       
|   |   +---tasks
|   |   |       asset_scraper_task.py
|   |   |       public_asset_scraper_task.py
|   |   |       send_new_active_public_asset_alert.py
|   |   |       __init__.py
|   |   |       
|   |   \---tests
|   |           asset_create_update_test.py
|   |           favorites_retrieve_create_destroy_test.py
|   |           public_asset_create_test.py
|   |           slot_create_test.py
|   |           __init__.py
|   |           
|   +---config
|   |   |   admin.py
|   |   |   asgi.py
|   |   |   celery_config.py
|   |   |   tasks.py
|   |   |   urls.py
|   |   |   wsgi.py
|   |   |   __init__.py
|   |   |   
|   |   +---celery-runners
|   |   |       celery-runner-for-beat.py
|   |   |       celery-runner-for-worker.py
|   |   |       runner.py
|   |   |       __init__.py
|   |   |       
|   |   \---settings
|   |           base.py
|   |           develop.py
|   |           product.py
|   |           test.py
|   |           
|   +---models
|   |       active_public_offer_model.py
|   |       api_model.py
|   |       offer_model.py
|   |       task_model.py
|   |       __init__.py
|   |       
|   +---scrapers
|   |       active_public_offers_scraper.py
|   |       offer_scraper.py
|   |       scraper.py
|   |       __init__.py
|   |       
|   +---templates
|   |       email_template.html
|   |       
|   \---user
|       |   admin.py
|       |   apps.py
|       |   models.py
|       |   tests.py
|       |   views.py
|       |   __init__.py
|       |   
|       \---migrations
|               0001_initial.py
|               __init__.py
|               
\---frontend
    |   .browserslistrc
    |   .eslintrc.js
    |   .gitignore
    |   babel.config.js
    |   jsconfig.json
    |   package-lock.json
    |   package.json
    |   postcss.config.js
    |   README.md
    |   tailwind.config.js
    |   vue.config.js
    |   
    +---public
    |   |   favicon.ico
    |   |   index.html
    |   |   robots.txt
    |   |   
    |   \---img
    |       \---icons
    |               android-chrome-192x192.png
    |               android-chrome-512x512.png
    |               android-chrome-maskable-192x192.png
    |               android-chrome-maskable-512x512.png
    |               apple-touch-icon-120x120.png
    |               apple-touch-icon-152x152.png
    |               apple-touch-icon-180x180.png
    |               apple-touch-icon-60x60.png
    |               apple-touch-icon-76x76.png
    |               apple-touch-icon.png
    |               favicon-16x16.png
    |               favicon-32x32.png
    |               msapplication-icon-144x144.png
    |               mstile-150x150.png
    |               safari-pinned-tab.svg
    |               
    \---src
        |   App.vue
        |   main.js
        |   registerServiceWorker.js
        |   
        +---assets
        |       app-bg.jpg
        |       logo.png
        |       style.css
        |       
        +---components
        |       AppHeader.vue
        |       HelloWorld.vue
        |       
        +---router
        |       index.js
        |       
        +---store
        |       index.js
        |       
        \---views
            |   AboutView.vue
            |   HomeView.vue
            |   
            \---layouts
                    AppLayouts.vue
```
