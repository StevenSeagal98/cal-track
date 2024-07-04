preferences_content = {
    'title': 'Preferences',
    'widgets': [
        {'type': 'label', 'text': 'Preferences'}
    ]
}

def format_key_to_str(key):
    parts = key.split('_')
    return ' '.join(part.capitalize() for part in parts)

def update(content_obj):
    import globals
    if len(content_obj['widgets']) > 1:
        content_obj['widgets'] = content_obj['widgets'][:1]
    print('Preferences in update: ', globals.preferences)
    try:
        for key in globals.preferences:
            content_obj['widgets'].append({
                'type': 'label',
                'text': f"{format_key_to_str(key)}: {globals.preferences[key]}"
            })
    except Exception as e:
        print('Error initializing preferences content: ', e)

preferences_content['update'] = lambda: update(preferences_content)
