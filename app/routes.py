from flask import render_template, url_for, flash, redirect, request
from app import app, db
from app.models import Item

@app.route('/')
@app.route('/home')
def home():
    items = Item.query.all()
    return render_template('index.html', items=items)

@app.route('/add', methods=['POST'])
def add_item():
    item_name = request.form.get('name')
    if item_name:
        new_item = Item(name=item_name)
        db.session.add(new_item)
        db.session.commit()
        flash('Item added successfully!', 'success')
    return redirect(url_for('home'))

@app.route('/delete/<int:item_id>')
def delete_item(item_id):
    item = Item.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    flash('Item deleted successfully!', 'success')
    return redirect(url_for('home'))
