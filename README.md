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
2. Open a terminal window in the project root directory.
3. Create a virtual environment and install the project dependencies:
    ```bash
      python -m venv env
      .\env\Scripts\activate
      pip install -r requirements.txt
      cd .\Chatrom_project\
   ```

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

## Testing
1. Run the Server.
2. Open multiple browsers.
3. Enter Same room name with different User Names

## Features
- Real-time messaging
- Multiple chat rooms
- Display of connected users

## Assumptions
- Enter the Chat room with your username and the chatroom created by other device.
- If the Chat room with that name already exists then the user will be joined in that chat-room. But if the room with that name is not present then a new room will be created and others can join the room.
- The moment someone joins the room the connected users list will be updated in real time same will happen if someone leaves the room.
- I have not added Create user functionality Due to time constraint Rather the user gets created as soon as use Enter the user name and hit submit on the landing screen.

## Built With
- [Django](https://www.djangoproject.com/) - The web framework used
- [Django Channels](https://channels.readthedocs.io/en/latest/) - For handling WebSockets and async communication

## Made By 
- Amit Kumar

## Screenshopts 
![image](https://github.com/user-attachments/assets/2c166837-a5f8-46bc-9553-ea90f27de7bb)

Inside the Room
![image](https://github.com/user-attachments/assets/cc2b84b1-2532-4b07-91ea-a233a3853470)


