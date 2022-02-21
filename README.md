# Chatbot

This chatbot uses the chatterbot python library and FASTAPI to host an api with an ai Controlled Chatbot. The chatbot can be trained by using train.py or by using the chatbot. You should first create a `.env` file with the following variables: 
- DB: mongodb://"your uri"

If you don't want to use mongodb you can delete the storage adapter and envReader file and it will just use sqlite3. To communicate with the chatbot through the webapi use gunicorn with the following command
```bash
gunicorn -k uvicorn.workers.UvicornWorker main:app
```
That should start a webserver on prt 8080 and by visiting http://127.0.0.1:8080/ you can talk to the chatbot. To add a message you should add the query parameter `message` to the url. Like this:
http://127.0.0.1:8080/?message=hello