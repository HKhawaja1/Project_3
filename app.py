from flask import Flask, render_template

app = Flask(__name__)

# Home Page Route (index.html)
@app.route("/")
def home():
    return render_template('index.html')

# About Page Route (about.html)
@app.route("/about")
def about():
    return render_template('about.html')

# Blog Page Route (blog.html)
@app.route("/blog")
def blog():
    return render_template('blog.html')

# Contact Page Route (contact.html)
@app.route("/contact")
def contact():
    return render_template('contact.html')

# Shop Page Route (shop.html)
@app.route("/shop")
def shop():
    return render_template('shop.html')

if __name__ == "__main__":
    app.run(debug=True)
