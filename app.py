{\rtf1\ansi\ansicpg1252\cocoartf2761
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import tkinter as tk\
from tkinter import messagebox\
import requests\
\
def fetch_book_info(isbn):\
    api_key = 'AIzaSyAziGvWZatFc81XTPteFeMopPD2gYZrH8E'\
    url = f'https://www.googleapis.com/books/v1/volumes?q=isbn:\{isbn\}&key=\{api_key\}'\
    response = requests.get(url)\
    data = response.json()\
    try:\
        book_info = data['items'][0]['volumeInfo']\
        return book_info\
    except KeyError:\
        messagebox.showerror("Error", "No book found with that ISBN")\
        return None\
\
def add_book():\
    isbn = isbn_entry.get()\
    book_info = fetch_book_info(isbn)\
    if book_info:\
        # Here you would save the book data to your database\
        print(book_info)  # Example to show the book data\
\
app = tk.Tk()\
app.title("Book Catalog")\
\
isbn_entry = tk.Entry(app)\
isbn_entry.pack()\
\
fetch_button = tk.Button(app, text="Fetch Book Info", command=add_book)\
fetch_button.pack()\
\
app.mainloop()\
}