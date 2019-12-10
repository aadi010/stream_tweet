# tweet_byju

To Get Started:

1. Install all dependencies [ pip3 install -r requirements.txt ]
2. Run the APP [ python3.7 api.py ]
3. Set the Enironment Variables in .env file
4. Make GET Request for streamming tweets based on UserName [  curl http://localhost:5002/tweets/userName\=<Insert UserName> ]
5. Make GET Request for streamming tweets based on HashTag [ curl http://localhost:5002/tweets/userName\=<Insert HashTag> ]
6. Output of the Stream written to file.
7. To view Output [ tail -f "fileName"]
8. No Test Cases as the APIs don't have a definitive response(Its a stream)