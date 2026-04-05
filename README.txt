# Finance Data Processing & Access Control Backend

## Overview

This project is a backend system for a finance dashboard that manages financial records, enforces 
role-based access control, and provides analytical insights.

It demonstrates backend architecture, API design, data modeling, and secure access handling.

---

## Tech Stack

Python
Django
Django REST Framework
JWT Authentication
SQLite (can be replaced with PostgreSQL)

---

## Features

### User & Role Management

* Custom User Model with roles:

  * **Viewer** → Read-only access
  * **Analyst** → Read + analytics access
  * **Admin** → Full access (CRUD + user management)
* User activation and status handling
* Role-based restrictions enforced at API level

---

### Financial Records Management

* CRUD operations for financial entries
* Fields:

  * Amount
  * Type (Income / Expense)
  * Category
  * Date
  * Notes
* Filtering:

  * By type
  * By category
  * By date
* Records are user-specific for security

---

### Analytics APIs

#### Dashboard Summary

* Total Income
* Total Expenses
* Net Balance

#### Category-wise Summary

* Aggregated totals by category

#### Monthly Trends (Advanced Feature)

* Monthly aggregation of income and expenses
* Useful for chart visualization in frontend dashboards

---

### Role-Based Access Control

| Role    | Create | Read | Update | Delete |
| ------- | ------ | ---- | ------ | ------ |
| Viewer  | NO      | YES    | NO      | NO      |
| Analyst | NO      | YES    | NO      | NO      |
| Admin   | YES      | YES    | YES      | YES      |

---

### Validation & Error Handling

* Input validation via serializers
* Proper HTTP status codes
* Clear error messages

---

## Authentication

JWT-based authentication using:

* `POST /api/token/` → Obtain access token
* `POST /api/token/refresh/` → Refresh token

---

## API Endpoints

### Users (Admin only)

* GET `/api/users/`
* POST `/api/users/`

---

### Financial Records

* GET `/api/records/`
* POST `/api/records/`
* PATCH `/api/records/{id}/`
* DELETE `/api/records/{id}/`

---

### Analytics

* GET `/api/dashboard/`
* GET `/api/category-summary/`
* GET `/api/monthly-trends/`

---

## Setup Instructions

```bash
git clone https://github.com/parmarshobhit91/finance_dashboard
cd finance_dashboard

pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser

python manage.py runserver
```

---

## Dummy Credentials

| Role    | Username | Password   |
| ------- | -------- | ---------- |
| Admin   | admin1    | hello@123   |
| Analyst | analyst  | hello@456 |
| Viewer  | viewer   | hello@789  |

---

## Sample Data

Includes:

* Salary income
* Freelance income
* Rent expense
* Food expense

---

## Design Decisions

* Used **Django REST Framework ViewSets** for scalability
* Implemented **custom permission classes** for RBAC
* Used **Django ORM aggregation functions** for analytics
* Structured project into modular apps:

  * users
  * finance
  * analytics
  * core

---

## Assumptions

* Each record belongs to a specific user
* Admin has full control over system data
* Analysts and viewers have restricted capabilities

---

## Future Improvements

* Pagination support
* Swagger API documentation
* Unit & integration tests
* Soft delete functionality

---

## Conclusion

This project focuses on building a clean, maintainable, and secure backend system with real-world architecture and proper access control.

---

Developed by: Shobhit Parmar
