#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask, send_file
import os

app = Flask(__name__)

@app.route("/")
def hello():
    print("init app")
    message = "¡Hola judador !"
    static_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static')
    index_path = os.path.join(static_dir, 'index.html')

    with open(index_path, 'r') as file:
        content = file.read()
        modified_content = content.replace('{{ message }}', message)

    with open('index.html', 'w') as modified_file:
        modified_file.write(modified_content)

    return send_file('index.html')
