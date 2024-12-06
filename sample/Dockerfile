# Step 1: Use an official Python runtime as a base image
FROM python:3.10-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the requirements.txt into the container
# (Assuming you have a requirements.txt with FastAPI and Uvicorn)
COPY requirements.txt .

# Step 4: Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the rest of the application files into the container
COPY . .

# Step 6: Expose the port the app runs on (default for Uvicorn is 8000)
EXPOSE 8000

# Step 7: Set the entry point to run your FastAPI app with Uvicorn
CMD ["uvicorn", "sample:app", "--host", "0.0.0.0", "--port", "8000"]
