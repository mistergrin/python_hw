from flask import Flask
from webargs.flaskparser import use_kwargs
from connection_sql import execute_query
from webargs import fields

app = Flask(__name__)


@app.route('/most-popular-music-style')
@use_kwargs({
    'genre': fields.Str(
        missing=None
    )
},  location='query')
def most_popular_music_style(genre: str):
    if genre:
        query = 'SELECT BillingCity, genres.Name  FROM invoices JOIN invoice_items ON invoices.InvoiceId = invoice_items.InvoiceId JOIN tracks ON invoice_items.TrackId = tracks.TrackId JOIN genres ON tracks.GenreId = genres.GenreId  WHERE genres.Name=? GROUP BY invoices.BillingCity ORDER BY  COUNT(*) DESC LIMIT 1'
        result = execute_query(query=query, args=(genre,))
    else:
        raise ValueError('print genre!')
    return result


if __name__ == '__main__':
    app.run(port=7000, debug=True)
