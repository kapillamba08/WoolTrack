# WoolTrack - Wool Supply Chain Monitoring System

A Django application for monitoring the journey of wool from farm to fabric, ensuring transparency and quality control across the supply chain.

## Features

- **Farm Registration**: Register and manage wool farms with owner details, location, and certifications
- **Batch Tracking**: Track wool batches from shearing through delivery with unique batch IDs
- **Processing Stages**: Monitor processing stages (Scouring, Carding, Spinning, Dyeing, Weaving, Finishing)
- **Distribution Events**: Track shipments, receipts, warehouse movements, and retail distribution
- **Analytics Dashboard**: Real-time overview with statistics and charts
- **Admin Panel**: Full Django admin interface for data management

## Quick Start

### 1. Activate Virtual Environment
```bash
source .venv/bin/activate
```

### 2. Run Migrations (if needed)
```bash
python manage.py migrate
```

### 3. Create Superuser (if needed)
```bash
python manage.py createsuperuser
```
Default credentials:
- Username: `admin`
- Password: `admin123`

### 4. Start Development Server
```bash
python manage.py runserver
```

### 5. Create Users & Assign Roles
- Visit http://127.0.0.1:8000/accounts/register/ for end-user access (view-only).
- Run `python manage.py createsuperuser` to create staff/admin accounts; only `is_staff` users can add or edit farms, batches, processing stages, and logistics events.
- Use http://127.0.0.1:8000/accounts/login/ to sign in and reach the dashboard.

### 6. Access the Application

- **Dashboard**: http://127.0.0.1:8000/
- **Farms**: http://127.0.0.1:8000/farms/
- **Batches**: http://127.0.0.1:8000/batches/
- **Processing**: http://127.0.0.1:8000/processing/
- **Logistics**: http://127.0.0.1:8000/logistics/
- **Admin Panel**: http://127.0.0.1:8000/admin/

## Project Structure

```
DjangoProject/
├── farms/          # Farm registration and management
├── batches/        # Wool batch tracking
├── processing/     # Processing stage monitoring
├── logistics/      # Distribution and logistics tracking
├── dashboard/      # Analytics and overview dashboard
└── wooltrack/      # Main project configuration
```

## Usage Workflow

1. **Register Farms**: Start by registering farms that produce wool
2. **Create Batches**: Create wool batches linked to farms with shearing dates and quality grades
3. **Track Processing**: Add processing stages as batches move through different facilities
4. **Monitor Distribution**: Record distribution events as batches move through the supply chain
5. **View Dashboard**: Monitor overall statistics and analytics on the dashboard

## Technologies

- Django 4.2.26
- SQLite (default database)
- Pico CSS (for styling)
- Chart.js (for analytics charts)

## License

This project is created for educational/assignment purposes.



