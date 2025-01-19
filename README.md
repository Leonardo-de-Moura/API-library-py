Flask API for Library Resources

This repository contains a Flask API designed to manage and provide resources related to a library.

Features

search books, and yours authors.

Add, update, and delete library resources (e.g., books, authors).

Lightweight and easy-to-extend structure.

Requirements

Python 3.8+

Flask 2.0+

Installation

Clone this repository:

git clone https://github.com/Leonardo-de-Moura/API-libray-py.git

Navigate to the project directory:

cd API-libray-py

Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate # On Windows, use `venv\Scripts\activate`

Install the dependencies:

pip install -r requirements.txt

Endpoints:

 localhost/livros(GET)- listagem de livros
 localhost/livros/id (GET)- listagem por id
 localhost/livro/id (PUT)- ediçao de 
 localhost/livros (POST)- criaçao de novos livros
 localhost/livro/id (DELETE)- deletar livros

Usage

Run the Flask development server:

flask run

Access the API at localhost and PORT=5000.