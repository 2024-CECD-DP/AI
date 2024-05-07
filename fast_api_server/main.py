import requests
import schedule

from config import GraphAPIConfig
from datetime import datetime
from fastapi import FastAPI
from utils import get_db_connection

app = FastAPI()


def get_user_list():
    conn, cur = get_db_connection()
    cur.execute("SELECT * FROM influencer")
    user_list = [row[2] for row in cur.fetchall()]
    cur.close()
    conn.close()
    return user_list


def update_meta(username):
    pass


def update_media(insta_name):
    conn, cur = get_db_connection()
    cur.execute("SELECT * FROM influencer WHERE insta_name=%s", (insta_name,))
    user_id = cur.fetchall()[0][0]

    api_url = (
        f"https://graph.facebook.com/v19.0/{GraphAPIConfig.user_id}"
        f"?fields=business_discovery.username({insta_name})"
        f"{{biography,name,username,follows_count,profile_picture_url,"
        f"website,ig_id,followers_count,media_count,media.limit(40)"
        f"{{caption,comments_count,id,children{{media_url,media_type}},"
        f"like_count,media_product_type,media_type,media_url,owner,permalink,timestamp,username}}}}"
        f"&access_token={GraphAPIConfig.access_token}"
    )

    response_json = requests.get(api_url).json()
    media_list = response_json["business_discovery"]["media"]["data"]

    for media in media_list:
        try:
            data = {
                "collected_date": datetime.today().strftime("%Y-%m-%d"),
                "comment_cnt": media["comments_count"],
                "creation_date": media["timestamp"][:10],
                "like_cnt": media["like_count"],
                "user_id": user_id,
                "caption": media["caption"].replace("\n", " "),
                "insta_media_id": media["id"],
            }

            print(data)

            insert_query = """
                INSERT INTO media (collected_date, comment_cnt, creation_date, like_cnt, user_id, caption, insta_media_id)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """

            cur.execute(insert_query, (
                data["collected_date"],
                data["comment_cnt"],
                data["creation_date"],
                data["like_cnt"],
                data["user_id"],
                data["caption"],
                data["insta_media_id"]
            ))

            conn.commit()
        except:
            continue

    cur.close()
    conn.close()


@app.get("/update")
async def update():
    user_list = get_user_list()
    for username in user_list:
        update_meta(username)
        update_media(username)


schedule.every().day.at("01:00").do(update)

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
#
#
# @app.get("/hello/{name}")
# async def say_hello(name: str):
#     return {"message": f"Hello {name}"}
