import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from libraryapp.models import Book, Library
from libraryapp.models import model_factory
from ..connection import Connection

def get_library(library_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Library)
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT 
            title,
            address
        FROM libraryapp_library 
        WHERE id = ? 
        """, (library_id,))

        return db_cursor.fetchone()

def library_details(request, library_id):
    if request.method =='GET':
        library = get_library(library_id)

        template = 'libraries/detail.html'
        context = {
            'library': library
        }
        return render(request, template, context)