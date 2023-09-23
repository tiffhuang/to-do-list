# to-do-list
Help organize things that needs to be done.

# Set-up Instructions
The setup for this repo is intentionally bad for instructional purposes.
This readme will be updated with an improved installation method.

Make sure python3 and pip3 are installed.

Run the following to make sure we have the necessary dependencies installed.
Yes, we should be running a virtual env. But we are doing this locally first
to understand why a virtual env is benefitial in the first place.

pip3 install SQLAlchemy
pip3 install Flask

Later we will set up a virtual environtment and a runtime script which will ensure we have the latest packages installed. For now we will deal with the inconvinience.

# Run Instructions
To run our api start our fask app (make sure ur at the project root directory):

python3 app/flask.py

On your web browser you can go to:

http://127.0.0.1:5000/

to use the API