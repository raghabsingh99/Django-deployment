import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')


import django
django.setup()



import random
from first_app.models import AccessREcord, Webpage, Topic
from faker import Faker

fakegen = Faker()
topics = ['Search','Social','Marketplace','News','Games']


def add_topic():
    
    # topic = random.choice(topics)
    # print('-------', topic)
    # try:
    #     t = Topic.objects.get(top_name=topic)
    # except:
    #     t = Topic.objects.create(top_name=topic)
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entery in range(N):
        top = add_topic()
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        webpg = Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]


        acc_rec= AccessREcord.objects.get_or_create(name=webpg,date=fake_date, count=3)[0]


if __name__ =='__main__':
    print("populating script!")
    populate(20)
    print("populating complete!")
