# mozio

## Instructions for Running the project locally

Create a .env file in the root directory, or re-name the .env.example file
Run "make up". This will start a container for the Database, one for the API and a last one for running migrations on the db.

The api container is configured to run on port 8100, so it'll be accessible on http://localhost:8100

API docs can be accessed in http://localhost:8100/docs and http://localhost:8100/redoc

The file "mozio.postman_collection.json" in the root directory contains requests examples that can imported to Postman for testing the apis.