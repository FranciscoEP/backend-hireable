# Importing necessary libraries

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import settings
import router
import uvicorn

# Initializing the fast API server
app = FastAPI()

origins = [
    
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
    settings.BASE_URL

]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Loading routes
app.include_router(router.api_router)




