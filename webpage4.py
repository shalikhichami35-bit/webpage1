from flask import Flask
app = Flask(__name__)
@app.route('/product/<product_name>/<int:price>/<category>')
def product(product_name, price, category):
    discount=price*0.10
    subtotal=price-discount
    gst=subtotal*0.18
    final_price=subtotal+gst
    return f"""
        <h1>Product information</h1>
        <hr>
        <b>Product name:</b>{product_name}<br><br>
        <b>Category:</b>{category}<br><br>
        <b>Discount(10%):</b>&{discount}<br><br>
        <b>GST(18%):</b>&{gst}<br><br>
        <h2>Final price":&{final_price:2f}</h2>
    """
if __name__ =='__main__':
    app.run(debug=True)