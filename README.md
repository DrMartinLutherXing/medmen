# MedMen Django Aptitude Test

This repo is a bare django project. We will use it to assess your abilities writing Python code, using the Django framework, and utilizing git.

There is no time limit, but the time taken is considered when we evaluate your code.

## Requirements

* Python 2.7 or greater
* Django 1.9 or greater

## Tasks

1. Implement a contact page
    1. Write code for after form validation
        * Send an email or write email to file
        * Implement a thanks page
            * Refactor the success_url so that it is future-proof
    1. Add a model for storing contact form submissions (Implement using your own schema design)
    1. Add a view for listing contact form submissions
1. Create a customer app
    1. Add a model for storing customer info with the following schema:
        * First Name
        * Last Name
        * Email
        * Phone Number
    1. Update contact page functionality to automatically create new Customer model objects on successful form submission
    1. Add a view for listing all Customers
    1. Add a view for viewing/editing/deleting a customer
1. Add any other improvements you can think of
1. Write tests
