import json


def get_image(xCoords, yCoords):
    data = {'xCoords': xCoords, 'yCoords': yCoords}

    try:
        with open('./data/thumbs_up.json', mode='w', encoding='utf-8') as output:
            entry = data
            output.append(entry)
            json.dump(feeds, feedsjson)
    except FileNotFoundError or TypeError or UnicodeEncodeError as e:
        return "[ERR] " + e