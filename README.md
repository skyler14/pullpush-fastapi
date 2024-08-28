# PullPush Reddit API Wrapper

This project provides a Python wrapper for the PullPush Reddit API using FastAPI. It offers a convenient way to interact with the PullPush Reddit API and includes interactive documentation.

## Features

- Easy-to-use wrapper for PullPush Reddit API
- Interactive API documentation using Swagger UI
- Endpoints for:
  - Searching comments
  - Searching submissions
  - Getting comment IDs
- Can be used as a standalone server or integrated into other Python applications

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn
- Pydantic

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/pullpush-api-wrapper.git
   cd pullpush-api-wrapper
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

### As a Standalone Server

To run the API wrapper as a standalone server:

```
uvicorn pullpushapi:app --reload
```

The server will start at `http://localhost:8000`. You can access the interactive documentation by navigating to `http://localhost:8000/docs` in your web browser.

### In Your Python Application

To use the API wrapper in your Python application:

1. Copy the `main.py` file to your project directory.

2. Import the necessary components in your script:

```python
from main import app, search_comments, search_submissions, get_comment_ids
from fastapi import FastAPI
from fastapi.testclient import TestClient

# Create a test client
client = TestClient(app)

# Now you can use the API functions directly
def get_top_comments(subreddit, limit=10):
    response = client.get(f"/reddit/search/comment/?q=&subreddit={subreddit}&size={limit}&sort=desc")
    return response.json()

# Example usage
top_comments = get_top_comments("AskReddit")
for comment in top_comments['data']:
    print(f"Author: {comment['author']}, Score: {comment['score']}")
```

This approach allows you to use the API wrapper functions directly in your code, making requests to the real PullPush Reddit API.

## API Endpoints

The API wrapper provides the following endpoints:

- `GET /reddit/search/comment/`: Search for comments
- `GET /reddit/search/submission/`: Search for submissions
- `GET /reddit/comment/ids/`: Get comment IDs for a submission

Each endpoint corresponds to a function in the `main.py` file that you can use directly in your code.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

[MIT License](LICENSE)

## Future Improvements

In future releases, we plan to:
- Add asynchronous support for better handling of concurrent requests

## Disclaimer

This project is not affiliated with or endorsed by Reddit, Inc. It is an unofficial wrapper for the PullPush Reddit API. Use responsibly and in accordance with PullPush's terms of service.