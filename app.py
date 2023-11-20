from flask import Flask, render_template_string
app = Flask(__name__)
@app.route('/')
def home():
    html_content = '**SERVER RUNNING**'
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(debug=False)