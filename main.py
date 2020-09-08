from flask import Flask, jsonify
from flask import render_template
from utils import blob_store

app = Flask(__name__)


@app.route('/')
def hello():    
    return render_template("index.html")


@app.route('/file_upload')
def file_upload():    
    return render_template("file_upload.html")


@app.route('/file_uploaded')
def file_uploaded():
    return render_template("file_upload.html")


@app.route('/get_upload_url')
def derp():
    policy = blob_store.get_upload_url({
        'referral_id': 111,
        'user_id': 222
    }, 'http://localhost:8080/file_uploaded')
    policy_fields = {
        key: value.decode('utf-8') if type(value) == bytes else value
        for key, value in policy['fields'].items()
    }
    return jsonify({
        'url': policy['url'],
        'policy_fields': policy_fields
    })


if __name__ == '__main__':
    # only runs locally, not in GCP
    app.run(host='127.0.0.1', port=8080, debug=True)