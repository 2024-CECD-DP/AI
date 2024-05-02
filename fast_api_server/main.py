from fastapi import FastAPI
import schedule

app = FastAPI()


def update():
    # 실행할 함수 내용을 여기에 작성합니다.
    pass


# 스케줄링할 작업을 추가합니다. 매일 새벽 1시에 job 함수를 실행하도록 예약합니다.
schedule.every().day.at("01:00").do(update)

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
#
#
# @app.get("/hello/{name}")
# async def say_hello(name: str):
#     return {"message": f"Hello {name}"}
