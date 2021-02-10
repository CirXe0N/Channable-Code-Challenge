## Channable - Code Challenge

This is a project based on an assignment given by [Channable](https://www.channable.com/).
The assignment description can be found [here](#assignment-description).

### Table of contents:
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Assignment Description](#assignment-description)

### Prerequisites
* [Python 3.7](https://www.python.org/downloads/)

### Usage
1. Make sure `Python` is installed and running properly.
1. Open the terminal and go to the directory of this project.
1. Run the following command to run the application.
    ```
    $ python3 main.py
    ```

### Assignment Description
Channable is an online tool that imports products from its users' eCommerceplatforms (e.g. WooCommerce) every day,
processes those products, and sends updates for those products to marketing channels (e.g. Amazon or eBay).
Technically speaking, Channable sends create, update, and delete operations for these products. Every day when
Channable imports the products from the eCommerce platform, Channable needs to decide which operation it needs
to send to the marketing channel:

  - Create: the product wasn’t imported from the eCommerce system yesterday,
    but it was imported today. This means we have to send a create operation
    to the eCommerce platform

  - Update: the product was imported yesterday and is also imported today,
    however, one of the values for the products has changed (e.g. the price of
    the product). This means we have to send an update operation to the
    marketing channel

  - Delete: the product was imported yesterday, but was not imported today.
    This means we have to send a delete operation to the marketing channel


#### General:
In this assignment you are asked to make a basic implementation of the logic described above. You should have
received two CSV files to resemble the data that is imported from the eCommerce system:

  - product_inventory_before.csv (resembles the product data that was imported yesterday)
  - product_inventory_after.csv (resembles the product data that was imported today)

For this assignment you need to build a program that compares the product data between the `before CSV` and
the `after CSV`. The `id` column can be assumed to be a unique identifier for the products in both CSVs. The
output should give the create, update, and delete operations that should be sent to the marketing channel.


#### Requirements:
  - The program should be a single .py file (no compressed files, such as .zip, .rar, etc.)
  - The program should be written in python 3.7, using only python’s built-in libraries.
  - You have to implement the `ProductDiffer` class below and specifically its entry point called `main`.
  - The `ProductStreamProcessor` should not be changed.
  - The output of main is a sequence of operations in the form of triples that contain:
        1. the operation type
        2. the product id
        3. either a dictionary with the product data where the keys are the column names from the
           CSV files or a `None`


#### Notes:
The assignment is consciously kept a bit basic to make sure you don’t have to spend hours and hours on this
assignment. However, even though the assignment itself is quite basic, we would like you to show us how you
would structure your code to make it easily readable, so others can trust it works as intended.
