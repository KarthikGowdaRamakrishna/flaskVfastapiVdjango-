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

