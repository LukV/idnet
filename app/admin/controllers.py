from flask import Blueprint, render_template, request, g, redirect, url_for
from flask_login import login_required
from flask_babel import gettext
from app.admin import admin

@admin.route('/')
@admin.route('/index')
def index():
	if g.user is not None and not g.user.is_administrator():
		return '<h1>No go zone for the unauthorized. Sorry.</h1>', 403

	return render_template('admin/index.html', 
		title=gettext('Admin'))
