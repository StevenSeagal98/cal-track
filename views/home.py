home_content = {
    'title': 'Home',
    'widgets': [
        {'type': 'label', 'text': 'Home'},
        {'type': 'calendar'}
    ]
}

def create_cards(tracker_data):
    calorie_tracker_cards = []
    for day in tracker_data:
        date = day['date']
        total_calories = day['calories_total']
        calorie_tracker_cards.append({
            'type': 'calorie_tracker_card',
            'date': date,
            'children': [
                {'type': 'label', 'text': date},
                {'type': 'label', 'text': f"Total Calories: {total_calories}"}
            ]
        })
    return calorie_tracker_cards

def init():
    import globals
    calorie_tracker_data = globals.calorie_tracker_data
    if(len(calorie_tracker_data) > 0):
        calorie_tracker_cards = create_cards(calorie_tracker_data)
        home_content['widgets'] += calorie_tracker_cards

def update():
    home_content['widgets'] = home_content['widgets'][:2]
    init()

home_content['update'] = update
