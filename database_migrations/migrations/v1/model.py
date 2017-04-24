# -*- coding: utf-8 -*-
from datetime import datetime
from uuid import UUID, uuid4
from pony.orm import *
from luckydonaldUtils.logger import logging

from secrets import POSTGRES_HOST, POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB


__author__ = 'luckydonald'
__all__ = ["Test", "User", "Tag"]
logger = logging.getLogger(__name__)

# https://editor.ponyorm.com/user/luckydonald/Tags_14

def register_database(db):
    class Test(db.Entity):
        emoji = Required(unicode, index=True)
        text = Optional(str, nullable=True)
        modified = Required(datetime, sql_default="NOW()", volatile=True)
        first_seen = Required(datetime, sql_default='NOW()')


    class User(db.Entity):
        id = PrimaryKey(int)
        name_first = Optional(str, nullable=True)
        name_last = Optional(str, nullable=True)

    class Tag(db.Entity):
        id = PrimaryKey(int, auto=True)
        user = Required(User, column='user_id')
        message_id = Optional(int)  # Of the message with the text, the tag. None means it got added via web gui.
        string = Required(unicode, index=True)
