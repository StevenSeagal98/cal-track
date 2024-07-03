import globals
calorie_tracker_data = globals.calorie_tracker_data

home_content = {
    'title': 'Home',
    'widgets': [
        {'type': 'label', 'text': 'Home'}
    ]
}

def create_cards(tracker_data):
    calorie_tracker_cards = []
    for day in tracker_data:
        print('Day: ', day)
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
    if(len(calorie_tracker_data) > 0):
        calorie_tracker_cards = create_cards(calorie_tracker_data)
        home_content['widgets'] += calorie_tracker_cards

init()