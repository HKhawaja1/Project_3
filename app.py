from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Get form data
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        phone = request.form['phone']
        email = request.form['email']
        message = request.form['message']
        
        # Process the form data (save it or send an email, etc.)

        # Redirect to thank you page
        return redirect(url_for('thank_you'))
    
    return render_template('contact.html')

@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/shop')
def shop():
    # Veggie meals data
    meals = [
        {
            'name': 'Veggie Delight',
            'price': '8.99',
            'description': 'Fresh vegetables cooked to perfection with a touch of spice.',
            'image': 'assets/Veggie_1.jpg'
        },
        {
            'name': 'Quinoa Bowl',
            'price': '10.99',
            'description': 'A nourishing bowl of quinoa, avocado, and fresh vegetables.',
            'image': 'assets/Veggie_2.jpg'
        },
        {
            'name': 'Grilled Veggie Salad',
            'price': '9.99',
            'description': 'Grilled seasonal vegetables served with a light dressing.',
            'image': 'assets/Veggie_3.jpg'
        }
    ]

    # Meat meals data
    meat_meals = [
        {
            'name': 'Grilled Chicken',
            'price': '12.99',
            'description': 'Juicy grilled chicken served with a side of roasted vegetables.',
            'image': 'assets/Meat_1.jpg'
        },
        {
            'name': 'Steak Peppercorn',
            'price': '15.99',
            'description': 'Tender steak in a peppercorn sauce served with mashed potatoes.',
            'image': 'assets/Meat_2.jpg'
        },
        {
            'name': 'BBQ Ribs',
            'price': '14.99',
            'description': 'Slow-cooked BBQ ribs smothered in a tangy sauce, served with fries.',
            'image': 'assets/Meat_3.jpg'
        }
    ]

    # Pescatarian meals data
    pescatarian_meals = [
        {
            'name': 'Grilled Salmon',
            'price': '16.99',
            'description': 'Grilled salmon served with a side of asparagus and lemon butter sauce.',
            'image': 'assets/Pescatarian_1.jpg'
        },
        {
            'name': 'Shrimp Scampi',
            'price': '14.99',
            'description': 'Sautéed shrimp in a garlic butter sauce served over linguine.',
            'image': 'assets/Pescatarian_2.jpg'
        },
        {
            'name': 'Tuna Poke Bowl',
            'price': '13.99',
            'description': 'Fresh ahi tuna with avocado, seaweed, and sesame served over rice.',
            'image': 'assets/Pescatarian_3.jpg'
        }
    ]

    return render_template('shop.html', meals=meals, meat_meals=meat_meals, pescatarian_meals=pescatarian_meals)

# Route to handle newsletter subscription
@app.route('/subscribe', methods=['POST'])
def subscribe():
    if request.method == 'POST':
        email = request.form.get('email')
        # You can add logic to save the email or perform other actions
        if email:
            return redirect(url_for('thank_you'))
        else:
            return render_template('error.html', message="Please provide a valid email address.")

if __name__ == '__main__':
    app.run(debug=True)
