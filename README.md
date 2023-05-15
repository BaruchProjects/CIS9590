
# CIS 9590 - Beauty Care Anywhere

This goal of the is project is to implement a hair salon reservation system. 




## Features
This project utilizes Bootstrap for the front-end, Django for the back-end, and is deployed on AWS EC2 for deployment.
## Installation
It requires Python 3.8 above. To get started with the project, follow these steps:

1. Clone the project

```bash
git clone https://github.com/BaruchProjects/CIS9590.git
```

2. Go to the project directory

```bash
cd CIS9590
```

3. Create virtual environment and activate

```bash
python -m venv venv
source venv/bin/activate
```

4. Install dependencies
```bash
pip install -r requirements.txt
```

5. Start server

```bash
python src/BeautyCare/manage.py runserver
```


## Usage
- Set up the database: `python manage.py migrate`
- Start the development server: `python manage.py runserver`
- Open your web browser and visit http://localhost:8000