from flask import abort, flash, redirect, render_template
from .unique_short import get_unique_short_id
from . import app, db

from .forms import URLMapForm
from .models import URLMap


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLMapForm()
    short = None
    if form.validate_on_submit():
        short = form.custom_id.data or get_unique_short_id()
        url_map = URLMap(
            original=form.original_link.data,
            short=short
        )
        db.session.add(url_map)
        db.session.commit()
        flash('Ссылка успешно создана!')
    url_maps = URLMap.query.all()
    return render_template(
        'index.html',
        form=form,
        url_maps=url_maps,
        short=short
    )


@app.route('/<string:short>')
def redirect_url(short):
    url_map = URLMap.query.filter_by(short=short).first()
    if not url_map:
        abort(404)
    return redirect(url_map.original)
