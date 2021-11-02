'''Define the richtext object for Notion'''

from pydantic import BaseModel
from enum import Enum

class TypeEnum(str, Enum):
    text = 'text'
    mention = 'mention'
    equation = 'equation'

class Annotations(BaseModel):
    pass

class RichTextObject(BaseModel):
    plain_text:str
    href:str = None
    annotations:Annotations
    type:TypeEnum
    pass