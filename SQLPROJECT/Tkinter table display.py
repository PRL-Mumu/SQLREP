import tkinter as tk
from dbhelper import DBhelper

db=DBhelper()
open_this=db.execute("SELECT * FROM USER")

for dt in open_this:
    print(dt)
