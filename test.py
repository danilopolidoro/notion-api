from notion.richtext import *

test = RichTextObject(
    type=Types.text,
    plain_text="Bom dia gente!"
)
test.annotations.color = Colors.pink


print(test.json())