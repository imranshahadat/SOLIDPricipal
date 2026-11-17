
FROM python:3.13-slim

WORKDIR /app

# Install uv
COPY --from=ghcr.io/astral-sh/uv:0.13.8 /uv /uvx /bin/

# Configure uv
ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy
ENV PYTHONUNBUFFERED=1

# Copy dependency files
COPY pyproject.toml uv.lock ./

# Install dependencies
RUN uv sync --frozen --no-install-project

# Copy source code
COPY src ./src

# Install the project
RUN uv sync --frozen

# Add virtual environment to PATH
ENV PATH="/app/.venv/bin:$PATH"

# Run your application
CMD ["python", "-m", "learning.CPD.main"]
