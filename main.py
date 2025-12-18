from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Auth Service")

# Allow frontend domain
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://libinrahman.cloud"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/login")
def login():
    return {"message": "Login endpoint working"}

@app.post("/logout")
def logout():
    return {"message": "Logout endpoint working"}
