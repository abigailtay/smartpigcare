# app.py
# This is the main Flask application file.
# It serves the dashboard page and loads pig data from a local JSON file.
# Note: Make sure VS Code is set to use the Python interpreter from your virtual environment:
#       Ctrl+Shift+P (Cmd+Shift+P on Mac) -> Python: Select Interpreter -> Choose venv interpreter path

from flask import Flask, render_template
import json
import os