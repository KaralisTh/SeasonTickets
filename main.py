from fastapi import FastAPI
from controllers.ticketsController import router

app = FastAPI()
app.include_router(router,prefix="/ticket")


def main():
    print("Start")


if __name__ == '__main__':
    main()

# uvicorn main:app --port 1111 --reload
