FROM python:3.11-slim

# set working directory in the container
WORKDIR /app

# 1️⃣ Copy project metadata to the container
COPY pyproject.toml ./
COPY poetry.lock* ./         

# 2️⃣ Install Poetry & deps
RUN pip install --no-cache-dir poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

# 3️⃣ Copy the rest of the source code
COPY . .


# inform docker which port the app uses 
EXPOSE 8000

# define the command that runs the app 
CMD ["uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
