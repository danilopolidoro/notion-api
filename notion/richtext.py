'''Define the richtext object for Notion'''

from pydantic import BaseModel
from enum import Enum

class TypeEnum(str, Enum):
    text = 'text'
    mention = 'mention'
    equation = 'equation'

class ColorEnum(str, Enum):
    default = 'default'
    brown = 'brown'
    yellow = 'yellow'
    blue = 'blue'
    pink = 'pink'
    gray = 'gray'
    orange = 'orange'
    green = 'green'
    purple = 'purple'
    red = 'red'
    gray_background = 'gray_background'
    brown_background = 'brown_background'
    orange_background = 'orange_background'
    yellow_background = 'yellow_background'
    green_background = 'green_background'
    blue_background = 'blue_background'
    purple_background = 'purple_background'
    pink_background = 'pink_background'
    red_background = 'red_background'

class MentionEnum(str, Enum):
    user = 'user'
    page = 'page'
    database = 'database'
    date = 'date'

class Annotations(BaseModel):
    bold:bool
    italic:bool
    strikethrough:bool
    underline:bool
    code:bool
    color:ColorEnum = ColorEnum.default

class LinkObject(BaseModel):
    type:str = 'url'
    url:str

class TextObject(BaseModel):
    content:str
    link:LinkObject = None

class MentionObject(BaseModel):
    type:MentionEnum

class EquationObject(BaseModel):
    expression:str

class RichTextObject(BaseModel):
    plain_text:str
    href:str = None
    annotations:Annotations
    type:TypeEnum
