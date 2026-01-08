from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Initial book list with count
books = [
    {'title': 'Python Basics', 'author': 'John Doe', 'count': 5},
    {'title': 'Java Fundamentals', 'author': 'Jane Smith', 'count': 3},
    {'title': 'C++ Programming', 'author': 'Alice Brown', 'count': 4},
]

@app.route('/')
def role():
    return render_template('role.html')

# ADMIN: Add books
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        books.append({
            'title': request.form['title'],
            'author': request.form['author'],
            'count': int(request.form['count'])
        })
        return redirect('/admin')
    return render_template('admin.html', books=books)

# USER: Show books page
@app.route('/books')
def books_page():
    return render_template('books.html', books=books)

# ISSUE book
@app.route('/issue/<int:index>')
def issue(index):
    if books[index]['count'] > 0:
        books[index]['count'] -= 1
    return redirect('/books')

# RETURN book
@app.route('/return/<int:index>')
def return_book(index):
    books[index]['count'] += 1
    return redirect('/books')

if __name__ == '__main__':
    app.run(debug=True)
