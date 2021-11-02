
from notion import Notion
from secrets import NOTION_TOKEN

base_id = "deb78b3e30fa4e02a06f499fc15e1faf"

notion_api = Notion(token=NOTION_TOKEN)

notion_api.add_item(db_id=base_id, name="Isso é um teste")