# RANDOM NUMBER STREAMER

A basic django app that exposes a RESTful API endpoint for a random number generator and display a graph using a streaming plot.ly graph.

The project uses Django Rest Framework, Django Channels, Channels API, and Plot.ly.

## Installation

1. Clone this repository: `git clone https://github.com/SteveWaweru/randomstream.git`.
2. `cd` into `randomstream`: `cd randomstream`.
3. Create virualenv from directory: `virtuaenv .`
4. Activate virtualenv: `source bin/activate`
5. `cd` into project `randomstream` file: `cd randomstream`
6. Install project requirements: `pip install -r requirements.txt`
7. Make migrations: `python manage.py makemigrations`
8. Run migrations: `python manage.py migrate`
9. Run application: `python manage.py runserver`
10. Navigate to your browser on localhost: `http://127.0.0.1:8000`

## Executing
Click on Button `Start Stream` when on localhost on browser and random
numbers will be plotted on a plot.ly graph

## Implementation
The approach used for this app is for the websocket to keep track of
updates to a resource. This is instantiated automatically when started
initiating a value with a primary key of 1 and updating value of the
object through each update on the database. This is an expensive operation
as the stream of data is dependant on an operation that requires an update
of a value in the database.

Also, there is some use of ajax to send a signal to the server on when to
update the value when called upon in order to receive a random number.

## Future Explorations
This are features that would need looking further into for improving the
functionality of the streamer
1. 1 WebSocekt per user requiring user to authenticate or tying websocket to a session.
2. Generating a random number without the need of a model.