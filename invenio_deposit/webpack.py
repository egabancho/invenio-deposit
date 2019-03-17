# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2019 CERN.
#
# Invenio is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Invenio is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307, USA.
#
# In applying this license, CERN does not
# waive the privileges and immunities granted to it by virtue of its status
# as an Intergovernmental Organization or submit itself to any jurisdiction.
"""JS/CSS bundles for deposit.
You include one of the bundles in a page like the example below (using
``base`` bundle as an example):
 .. code-block:: html
    {{ webpack['base.js']}}
"""

from flask_webpackext import WebpackBundle

deposit = WebpackBundle(
    __name__,
    'assets',
    entry={
        'deposit_app': './js/invenio_deposit/app.js',
        'deposit_theme': './scss/invenio_deposit/deposit.scss',
    },
    dependencies={
        'almond': '~0.3.1',
        'angular-animate': '~1.4.8',
        'angular-sanitize': '~1.4.10',
        'angular-schema-form': '~0.8.13',
        'angular-schema-form-ckeditor':
        'git://github.com/webcanvas/angular-schema-form-ckeditor'
        '.git#b213fa934759a18b1436e23bfcbd9f0f730f1296',
        'angular-schema-form-dynamic-select': '~0.13.1',
        'angular-strap': '~2.3.9',
        'angular-translate': '~2.11.0',
        'angular-ui-sortable': '~0.14.3',
        'angular-underscore': '~0.0.3',
        'ckeditor': '~4.5.10',
        'invenio-files-js': '~0.0.2',
        'invenio-records-js': '~0.0.8',
        'jquery': '~3.2.1',
        'jqueryui': '~1.11.1',
        'ng-file-upload': '~12.0.4',
        'objectpath': '~1.2.1',
        'rr-ng-ckeditor': '~0.2.1',
        'tv4': '~1.2.7',
        'ui-select': '~0.18.1',
        'underscore': '~1.8.3',
    })
