from datetime import date 

def get_weekday():
    return date.today().strftime('%A')

def create_new_post(post, weekday=get_weekday()):
    post_copy = post.copy()
    post_copy['create_on_weekday'] = weekday
    return post_copy

intial_post = { 
    'id' : 12,
    'author' : 'Arslan',
}

post_with_weekday = create_new_post(intial_post, 'Monday')
print(post_with_weekday)