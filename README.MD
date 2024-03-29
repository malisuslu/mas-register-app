<!-- Please update value in the {}  -->

<h1 align="center">Student Register App (Django)</h1>


<div align="center">
  <h3>
    <a href="https://mas-register-app.vercel.app/">
      Demo
    </a>
     | 
    <a href="https://github.com/malisuslu/mas-register-app/">
      Project
    </a>
 
  </h3>
</div>

<!-- TABLE OF CONTENTS -->

## Table of Contents

- [Table of Contents](#table-of-contents)
  - [Built With](#built-with)
- [How To Use](#how-to-use)
- [Acknowledgements](#acknowledgements)
- [Contact](#contact)

<!-- OVERVIEW -->

<!-- ## Overview

![screenshot](todo.PNG) -->

### Built With

<!-- This section should list any major frameworks that you built your project using. Here are a few examples.-->

- HTML
- CSS
- Python
- Django
- Tailwind CSS

## How To Use

<!-- This is an example, please update according to your application -->

To clone and run this application, you'll need [Git](https://git-scm.com) 
```bash
# Clone this repository
$ git clone https://github.com/malisuslu/mas-register-app.git

# Install dependencies
    $ python -m venv env
    > env/Scripts/activate (for win OS)
    $ source env/bin/activate (for macOs/linux OS)
    $ pip install -r requirements.txt
    
# open the file "../mas-register-app/student_project/settings.py", change the "SITE_ID" value from "2" to "1"(if exists) and change the DEBUG value from "False" to "True" and save the file.
    
# Create ".env" file in the main directory "../mas-register-app/"
# Add "SECRET_KEY" in .env file
# In order to use Google Authentication service you must also add some valid "GOOGLE_CLIENT_ID" and "GOOGLE_CLIENT_SECRET"(if needed)

# Run the app
    $ python manage.py runserver
```

## Acknowledgements

- This is my first Django App. Styling made by Tailwind, Crispy_Tailwind for the form. PostgreSQL DB is created on ElephantSQL, and the app deployed to Vercel for page preview... 

## Contact

- GitHub [@malisuslu](https://github.com/malisuslu)
- Linkedin [@malisuslu](https://www.linkedin.com/in/malisuslu/)