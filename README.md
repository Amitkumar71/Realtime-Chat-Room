# Real-Time Chat Application
This is a real-time chat application built with Django and Django Channels.

## Getting Started
Follow these steps to set up and run the project on your local machine.

### Prerequisites
- Python 3.x
- pip (Python package manager)

### Installation
1. Clone the repository 
   OR download and extract the ZIP file.

2. Navigate to the project directory:
   <button class="copy-button" data-clipboard-target="#cd-command"></button>
   <pre><code id="cd-command">cd .\Chatrom_project\</code></pre>

3. Install the required dependencies:
   <button class="copy-button" data-clipboard-target="#pip-install-command">Copy</button>
   <pre><code id="pip-install-command">pip install -r requirements.txt</code></pre>

### Running the Application
1. Apply database migrations:
   <button class="copy-button" data-clipboard-target="#makemigrations-command">Copy</button>
   <pre><code id="makemigrations-command">python manage.py makemigrations</code></pre>
   
   <button class="copy-button" data-clipboard-target="#migrate-command">Copy</button>
   <pre><code id="migrate-command">python manage.py migrate</code></pre>

2. Start the Django development server:
   <button class="copy-button" data-clipboard-target="#runserver-command">Copy</button>
   <pre><code id="runserver-command">python manage.py runserver</code></pre>

3. Open a web browser and go to `http://127.0.0.1:8000/` to access the application.

## Usage
1. On the home page, enter your username and the name of the chat room you want to join.
2. Start chatting in real-time with other users in the same room.
3. You can see the list of connected users in the room.

## Features
- Real-time messaging
- Multiple chat rooms
- Display of connected users

## Built With
- [Django](https://www.djangoproject.com/) - The web framework used
- [Django Channels](https://channels.readthedocs.io/en/latest/) - For handling WebSockets and async communication

## Made By 
- Amit Kumar
