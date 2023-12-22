
## Getting Started

Make sure you have installed Python3.

1. Install pip if not exist

   ```bash
   python -m pip install --upgrade pip
   ```

2. Install virtualenv if not exist

   ```bash
   python -m pip install virtualenv
   ```

3. Clone Backend Django Repository

   ```bash
   git clone https://github.com/Abdalla991/BE-Journey.git
   cd BE-Journey
   cd be_drf
   ```

4. Create virtual environment with name (env)

   ```bash
   python -m venv env
   ```

5. Activating a virtual environment

   | Windows                | Linux                   |
   | ---------------------- | ----------------------- |
   | .\env\Scripts\activate | source env/bin/activate |

6. Install Requirements

   ```bash
   pip install -r requirements.txt
   ```

7. Build your database (sqlite for local).
   ```bash
   python manage.py migrate
   ```

8. Start Django Server and browse localhost:8000
   ```bash
   python manage.py runserver
   ```



