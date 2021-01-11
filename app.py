from flask import Flask

app = Flask(__name__)

print("hello")

# Store answers in this list (ex ['Yes', 'No', 'Less than $10,000', 'Yes'])
responses = []