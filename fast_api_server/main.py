import schedule

from fastapi import FastAPI
from utils import get_db_connection

app = FastAPI()


def get_user_list():
    conn, cur = get_db_connection()
    cur.execute("SELECT * FROM user_entity")
    user_list = [row[1] for row in cur.fetchall()]
    cur.close()
    conn.close()
    return user_list


def update_meta(username):
    pass


def update_media(username):
    pass


def update():
    # 실행할 함수 내용을 여기에 작성합니다.
    user_list = get_user_list()
    for username in user_list:
        update_meta(username)
        update_media(username)


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
