from fastapi import FastAPI, Depends # type: ignore
from pydantic import BaseModel, EmailStr 


app = FastAPI()

class UserSignUp(BaseModel):
    username: str
    email: EmailStr
    password: str

class Settings(BaseModel):
    app_name: str = "Hillarious Rift"
    admin_email: EmailStr = "admin.ravinandan@gmail.com"

def get_Settings():
    return Settings()

@app.post('/signup')
def signup(user: UserSignUp):
    return f"message: {user.username} is signed up sucessfully!"

@app.post('/settings')
def get_settings_endpoint(settings: Settings = Depends(get_Settings)): # Depends lets FastAPI provide a value—such as settings—to an endpoint.
# Depends(get_Settings) tells FastAPI to call get_Settings() and pass its result into the settings parameter.
    return settings

#################### DEMO USE ##########################

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)

# Run this file, then open http://127.0.0.1:8000/docs to try the endpoints.
# For /signup, send:
# {"username": "sam", "email": "sam@example.com", "password": "secret"}
# For /settings, send an empty JSON object: {}.