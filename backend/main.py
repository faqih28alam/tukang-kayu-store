from fastapi import FastAPI

app = FastAPI()

# Define a Simple Route
@app.get("/")
def root():
    return {"message": "Hello World!"}

#
@app.get("/name")
def root(name: str="Budi"):
    return{"message": f"Selamat datang di toko kami, kak {name}!"}