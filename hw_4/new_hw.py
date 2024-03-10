from flask import Flask
from webargs.flaskparser import use_kwargs
from connection_db import execute_query
from webargs import fields


app = Flask(__name__)


@app.route('/order-price')
@use_kwargs({
    'country': fields.Str(
        missing=None
    )
},  location='query')
def order_price(country: str):
    if country:
        query = 'SELECT sum(UnitPrice * Quantity) FROM invoice_items JOIN invoices ON invoices.InvoiceId = invoice_items.InvoiceId WHERE BillingCountry = ?'
        result = execute_query(query=query, args=(country,))
    else:
        query = 'SELECT sum(UnitPrice * Quantity) FROM invoice_items JOIN invoices ON invoices.InvoiceId = invoice_items.InvoiceId'
        result = execute_query(query=query)
    return result


@app.route('/info-about-track')
@use_kwargs({
    'id': fields.Int(
        missing=1
    )
}, location='query')
def get_all_info_about_track(id: int):
    query = ('SELECT tracks.Name, Composer, genres.Name, artists.Name, albums.Title, media_types.Name '
             ' FROM tracks JOIN albums ON tracks.AlbumId = albums.AlbumId JOIN genres ON tracks.GenreId = genres.GenreId'
             ' JOIN artists ON albums.ArtistId = artists.ArtistId JOIN main.media_types ON tracks.MediaTypeId = media_types.MediaTypeId WHERE TrackId = ?')
    result = execute_query(query=query, args=(id,))
    return result


@app.route('/time-track')
def get_time_track():
    query = ('SELECT sum(Milliseconds) FROM tracks')
    result_query = execute_query(query=query)
    result = (((result_query[0][0]) / 1000) / 60) / 60
    return f"<p>{result} hours</p>"


if __name__ == '__main__':
    app.run(debug=True, port=7000)
