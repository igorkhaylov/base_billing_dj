CKEDITOR_UPLOAD_PATH = "uploads/"

CKEDITOR_CONFIGS = {
    'default': {
        # 'skin': 'moono',
        # 'skin': 'office2013',
        'toolbar_Basic': [
            ['Source', '-', 'Bold', 'Italic']
        ],
        'toolbar_YourCustomToolbarConfig': [
            {'name': 'document', 'items': ['Source', '-', 'Save', 'NewPage', 'Print', '-', 'Templates']},
            {'name': 'basicstyles',
             'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
            {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll']},
            {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
            '/',
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
                       'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl']},
            {'name': 'yourcustomtools', 'items': [
                # put the name of your editor.ui.addButton here
                'Preview',
                'Maximize',
            ]},
            {'name': 'insert',
             'items': ['Image', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe']},
            '/',
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            # {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']}, # put this to force next toolbar on new line
        ],
        'toolbar': 'YourCustomToolbarConfig',  # put selected toolbar config here
        # 'toolbarGroups': [{ 'name': 'document', 'groups': [ 'mode', 'document', 'doctools' ] }],
        # 'height': 291,
        # 'width': '100%',
        # 'filebrowserWindowHeight': 725,
        # 'filebrowserWindowWidth': 940,
        # 'toolbarCanCollapse': True,
        # 'mathJaxLib': '//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML',
        'tabSpaces': 4,
        'extraPlugins': ','.join([
            'uploadimage',  # the upload image feature
            # your extra plugins here
            'div',
            'autolink',
            'autoembed',
            'embedsemantic',
            'autogrow',
            # 'devtools',
            'widget',
            'lineutils',
            'clipboard',
            'dialog',
            'dialogui',
            'elementspath',
        ]),
    },
    'list_description': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['BulletedList', 'Source'],
        ],
    },
    'my_config': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ["Source", "Templates", 'Format', 'Font', 'FontSize', 'Maximize', 'ShowBlocks'], '/',
            ['Image', 'Youtube', 'Table', 'Bold', 'Italic', 'Underline', 'Strike', 'Indent', 'Outdent',
             'HorizontalRule'],
            ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', 'Blockquote', 'NumberedList'],
            ['BulletedList', 'TextColor', 'BGColor', 'Link', 'Smiley', 'SpecialChar'], '/',
            ['Find', 'Subscript', 'Superscript'], '/',
            [], '/',
            [], '/',
        ],
        'extraPlugins': ','.join([
            'uploadimage',
            'youtube',
        ]),
    },
    'for_church': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ["Source", 'Font', 'FontSize', 'Maximize', 'ShowBlocks'], '/',
            ['Image', 'Youtube', 'Table', 'Bold', 'Italic', 'Underline', 'Strike', 'Indent', 'Outdent',
             'HorizontalRule'],
            ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', 'Blockquote', 'NumberedList'],
            ['BulletedList', 'TextColor', 'BGColor', 'Link', 'Anchor', 'Smiley', 'SpecialChar'], '/',
            ['Find', 'Subscript', 'Superscript'], '/',
            [], '/',
            [], '/',
        ],
        'extraPlugins': ','.join([
            # 'uploadimage',
            # 'youtube',
        ]),
    },
    'schedule': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Font', 'Maximize'], '/',
            ['Table', 'Bold', 'Italic', 'Underline',
             'HorizontalRule'],
            ['BulletedList', 'TextColor', 'BGColor', 'Link', 'Smiley', 'SpecialChar'], '/',
            ['Find', 'Subscript', 'Superscript'], '/',
            [], '/',
            [], '/',
        ],
    },
    'radiants_description': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['NumberedList', 'Source'], '/',
            ['Image', 'TextColor', 'BGColor', 'Link', 'Anchor',],
        ],
    }
}
