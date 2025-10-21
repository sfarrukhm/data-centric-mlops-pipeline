FROM python:3.12-slim

# install uv for reproduceible dependency management
RUN pip install uv==0.7.13 

# set working directory
WORKDIR /app

# copy dependency filess
COPY pyproject.toml uv.lock ./

# install dependencies deterministically
RUN uv sync --frozen --no-dev

# Copy code
COPY src/ ./src/

# Expose FastAPI app port (for serving)
EXPOSE 8080

# Default command for serving API

CMD ["uv", "run", "unicorn", "main:app", "--host","0.0.0.0","--port","8080"]