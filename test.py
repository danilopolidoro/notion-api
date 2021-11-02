from notion.richtext import *

test = RichTextObject(
    type=TypeEnum.text,
    plain_text="Bom dia gente!"
)
test.annotations.color = ColorEnum.pink


print(test.json())