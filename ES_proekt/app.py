from flask import Flask, render_template, request

app = Flask(__name__)

reviews = [
    {
        'id': 1,
        'text': 'Great product!',
        'rating': 5,
        'date': '2023-06-01',
    },
    {
        'id': 2,
        'text': 'Average product.',
        'rating': 2,
        'date': '2023-06-02',
    },
    {
        'id': 3,
        'text': '',
        'rating': 1,
        'date': '2023-06-13',
    },
    {
        'id': 4,
        'text': 'OK',
        'rating': 3,
        'date': '2023-06-12',
    },
    {
        'id': 5,
        'text': '',
        'rating': 4,
        'date': '2023-06-23',
    }
]
@app.route('/', methods=['GET'])
# def home():
#     return "Welcome to the Review Filtering App."

@app.route('/filter-reviews', methods=['GET'])
def filter_reviews():
    prioritize_text = request.args.get('prioritize_text', 'all')
    sort_rating = request.args.get('sort_rating', 'highest')
    sort_date = request.args.get('sort_date', 'newest')
    min_rating = request.args.get('min_rating', 0, type=int)

    filtered_reviews = reviews

    if min_rating:
        filtered_reviews = [review for review in filtered_reviews if review['rating'] >= min_rating]

    if sort_rating == 'highest':
        filtered_reviews = sorted(filtered_reviews, key=lambda x: x['rating'], reverse=True)
    elif sort_rating == 'lowest':
        filtered_reviews = sorted(filtered_reviews, key=lambda x: x['rating'])

    if sort_date == 'newest':
        filtered_reviews = sorted(filtered_reviews, key=lambda x: x['date'], reverse=True)
    elif sort_date == 'oldest':
        filtered_reviews = sorted(filtered_reviews, key=lambda x: x['date'])

    if prioritize_text != 'all':
        filtered_reviews = [review for review in filtered_reviews if review['text']]

    return render_template('reviews.html', reviews=filtered_reviews, prioritize_text=prioritize_text)

if __name__ == '__main__':
    app.run(debug=True)
