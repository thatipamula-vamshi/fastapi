from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import csv

app = FastAPI()

security = HTTPBasic()

def authenticate_user(username: str, password: str):
    try:
        with open("user1.csv", "r") as file1:
            rows = csv.DictReader(file1)
            for row in rows:
                print(row)
                if row["username"] == username and row["password"] == password:
                    return True  
        return False  
    except Exception as e:
        return e
    

def authenticate_credentials(credentials= Depends(security)):

    username = credentials.username
    password = credentials.password
    
    is_authenticated = authenticate_user(username, password)
    
    if is_authenticated:
        return username 
    else:
        raise HTTPException(status_code=401, detail="Invalid username or password")

@app.post("/login")
async def login(request: Request, username: str = Depends(authenticate_credentials)):


    headers = dict(request.headers)
    body = await request.body()  # To read the raw body
    query_params = request.query_params
    # print(request.app)
    # print(request.base_url)
    
    # print(f"Headers:", headers)
    # print(f"Body: {body}")
    # print(f"Query Params: {query_params}")
    # print(type(headers))
    return {"message": f"Authentication successful for user {username}!"}
