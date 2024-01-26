```console
pip install fastapi
pip install "uvicorn[standard]"
pip install python-multipart sqlalchemy jinja2

uvicorn app:app --reload
```

## About FastAPI

FastAPI is a modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints. The key features of FastAPI include:

- **Fast to run**: High performance, on par with NodeJS and Go (thanks to Starlette and Pydantic).
- **Fast to code**: Great editor support. Completion everywhere. Less time debugging.
- **Robust**: Get production-ready code with automatic interactive documentation.

## `/docs` - Interactive API Documentation

One of the standout features of FastAPI is its automatic generation of interactive API documentation using Swagger UI. Accessible via the `/docs` endpoint, this documentation provides a detailed overview of all the API routes, expected request formats, and potential responses.

### How to Use `/docs`

To access the interactive documentation, simply run your FastAPI To-Do application and navigate to `/docs` in your web browser. For example, if your application is running on `localhost` at port `8000`, the URL to access the documentation would be:                     
# http://localhost:8000/docs



### Features of `/docs`

- **Interactive**: Test your API directly from the browser. No need for separate tools to send requests.
 ![image](https://github.com/KarthikGowdaRamakrishna/flaskVfastapiVdjango-/assets/144963620/1b26ec36-01bd-46ea-86e3-8bb9c36688ce)
- **Self-Updating**: Documentation updates automatically as you make changes to your API.
- **Try Out Requests**: Execute requests with custom parameters and see responses in real-time.
![image](https://github.com/KarthikGowdaRamakrishna/flaskVfastapiVdjango-/assets/144963620/c5dbb821-62c2-4208-9bcb-029a8df30927)
- **Schema Visualization**: View the request and response schemas for each API endpoint.
![image](https://github.com/KarthikGowdaRamakrishna/flaskVfastapiVdjango-/assets/144963620/1dc7996d-4cdb-4993-a6d4-ba66ecd0f6ed)


### Navigating `/docs`

Within the `/docs` page, you will find:

- **A list of all API routes**: Each route is expandable to show detailed information, including HTTP method, path, expected request body, query parameters, and response models.
- **"Try it out" feature**: Allows you to send real requests to your API, customize the request payload, and see the response directly in the documentation.
- **Authentication and Authorization**: If implemented, you can authenticate directly through the `/docs` interface to test routes that require security.

## Conclusion

The `/docs` feature of FastAPI is an invaluable tool for developers and users alike, providing a clear, interactive, and up-to-date view of the API's capabilities. Whether you're debugging, developing new features, or demonstrating the API to stakeholders, the `/docs` endpoint is your go-to resource for understanding and interacting with the FastAPI To-Do application.

For more information on FastAPI, visit the [official FastAPI documentation](https://fastapi.tiangolo.com/).


