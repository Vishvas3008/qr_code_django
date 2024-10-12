#!/bin/bash

echo "Starting static files collection..."
python3 manage.py collectstatic --noinput
echo "Static files collection completed."
