import os
import sqlite3
import uuid
from pydantic import BaseModel, Field
from typing import List

class NotFound(Exception):
    pass

class Todo(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4())) 
    title: str
    description: str
    is_done: bool

    @classmethod
    def get_by_id(cls, todo_id: str):
        con = sqlite3.connect(os.getenv("DATABASE_NAME","database.db"))
        con.row_factory = sqlite3.Row

        cur = con.cursor()
        cur.execute("SELECT * FROM todos WHERE id=?", (todo_id,))

        record = cur.fetchone()

        if record is None:
            raise NotFound

        todo_entry = cls(**record)
        con.close()

        return todo_entry

    @classmethod
    def get_by_title(cls, todo_title: str):
        con = sqlite3.connect(os.getenv("DATABASE_NAME","database.db"))
        con.row_factory = sqlite3.Row

        cur = con.cursor()
        cur.execute("SELECT * FROM todos WHERE title=?", (todo_title,))

        record = cur.fetchone()

        if record is None:
            raise NotFound

        todo_entry = cls(**record)
        con.close()

        return todo_entry

    @classmethod
    def flip_is_done_by_id(cls, todo_id) -> bool:
        con = sqlite3.connect(os.getenv("DATABASE_NAME", "database.db"))
        con.row_factory = sqlite3.Row

        cur = con.cursor()
        record = cur.execute("SELECT * FROM todos WHERE id=?", (todo_id,)).fetchone()
        todo = cls(**record)
        is_done = (not todo.is_done)
        cur.execute("UPDATE todos SET is_done=? WHERE id=?", (is_done, todo_id))
        con.commit()

        return is_done


    @classmethod
    def list(cls) -> List['Todo']:
        con = sqlite3.connect(os.getenv("DATABASE_NAME", "database.db"))
        con.row_factory = sqlite3.Row

        cur = con.cursor()
        cur.execute("SELECT * FROM todos")

        records = cur.fetchall()
        todos = [cls(**record) for record in records]
        con.close()

        return todos

    def save(self) -> "Todo":
        with sqlite3.connect(os.getenv("DATABASE_NAME","database.db")) as con:
            cur = con.cursor()
            cur.execute(
                "INSERT INTO todos (id,title,description,is_done) VALUES(?,?,?,?)",
                (self.id,self.title,self.description,self.is_done)
            )
            con.commit()
        return self

    @classmethod
    def create_table(cls, database_name="database.db"):
        conn = sqlite3.connect(database_name)

        conn.execute(
            """CREATE TABLE IF NOT EXISTS todos (id TEXT, title TEXT, description TEXT, is_done BOOLEAN NOT NULL CHECK (is_done IN (0,1)));
            """    
            )
        conn.close()
