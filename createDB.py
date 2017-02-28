import json
from courses.models import Course

def load(file):
    def convert(input):
        if isinstance(input, dict):
            return {convert(key): convert(value) for key, value in input.iteritems()}
        elif isinstance(input, list):
            return [convert(element) for element in input]
        elif isinstance(input, unicode):
            return input.encode('utf-8')
        else:
            return input
    dict_unicode = json.loads(open(file).read())
    return convert(dict_unicode)

courses = load('courses.json')

for i in courses:
    item = courses[i]
    c = Course.objects.create(id=item['id'], name=item['name'], grades=item['grades'], prereq=item['prereq'],credits=int(item['credits']),rating=item['rating'],syllabus=item['syllabus'])
