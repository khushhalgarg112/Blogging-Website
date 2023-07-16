from flask import Flask, render_template
import requests



url = 'https://api.jsonbin.io/v3/b/64b43304b89b1e2299bfe277'
headers = {
  'X-Master-Key': '$2b$10$fRUf6vZGQv7PqE2f3F..t.7eWz8eu8PtKuAKhJvlM3oukraVb765C'
}

req = requests.get(url, json=None, headers=headers)
response = req.json()['record']


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", res=response)


@app.route('/post/<int:num>')
def full_post(num):
    blog = None
    for i in response:
        if num == i['id']:
            blog = i
    return render_template("post.html", res= blog)

if __name__ == "__main__":
    app.run(debug=True)
