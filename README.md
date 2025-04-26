# TCMB Currency Rates Viewer

This project is a Django-based web application that allows users to fetch and display Turkish Central Bank (TCMB) currency exchange rates.

## Features

- Fetches current exchange rates from TCMB's **today.xml**.
- Fetches historical exchange rates based on user-selected date.
- Allows users to:
  - Filter currencies by specific codes (e.g., USD, EUR, GBP).
  - Select a specific historical date by entering day, month, and year separately.
- Displays results in a clean, minimal, and mobile-friendly table layout.

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use: env\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Fetch the latest data (optional):**
   ```bash
   python manage.py fetch_data
   ```

6. **Run the server:**
   ```bash
   python manage.py runserver
   ```

7. Open your browser and go to `http://127.0.0.1:8000/` to use the application.

## Requirements

- Python 3.8+
- Django
- requests
- xmltodict

*(All dependencies are listed in `requirements.txt`.)*

## Notes

- Users must enter currency codes separated by commas (e.g., USD, TRY, EUR).
- Day, month, and year are selected through separate input fields to ensure correct date formatting.
- If no currency codes are entered, the system displays all available rates for the selected date.

## Future Improvements

In future versions, users will be able to generate dynamic graphs of selected currency rates over custom date ranges.

---
