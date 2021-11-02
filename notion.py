'''This file will abstract all interactions with Notion by defining a Notion class.'''

import requests as re

class Notion:
    __base_url = "https://api.notion.com"
    def __init__(self, token:str) -> None:
        self.__token = token

    def add_item(self, db_id:str, name:str):
        req_body = {
            "parent": {
                "database_id": db_id
            },
            "properties": {
                "title": {
                    "title": [
                        {
                            "text": {
                                "content": name
                            }
                        }
                    ] 
                }
            }
        }

        req_header = {
            "Authorization": f"Bearer {self.__token}",
            "Content-Type": "application/json",
            "Notion-Version": "2021-08-16"
        }

        req_url = self.__base_url + "/v1/pages"

        resp = re.post(url=req_url, json=req_body, headers=req_header)
        return resp




