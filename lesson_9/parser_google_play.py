from google_play_scraper import Sort, reviews
import pandas as pd
import os


def scrape(app_name, count=100, field_names=None):
    result = reviews(
        app_name,
        lang='ru',
        country='ru',
        sort=Sort.NEWEST,
        count=count
    )
    df = pd.DataFrame(result[0])[field_names]
    df.to_csv(f'{"_".join(app_name.split("."))}_temp.csv', index=False, encoding='utf-8')
    return f'{"_".join(app_name.split("."))}_temp.csv'


def new_reviews(old_csv, new_csv):

    with open(old_csv, 'r', encoding='utf-8') as old, \
            open(new_csv, 'r', encoding='utf-8') as new:
        file_old = old.readlines()
        file_new = new.readlines()

    with open(f'{old_csv[:-4]}_update.csv', 'w', encoding='utf-8') as update_file:
        for line in file_new:
            if line not in file_old:
                update_file.write(line)
    os.remove(new_csv)


def init_parser():
    fieldnames = ['userName', 'content', 'score',
                  'thumbsUpCount', 'reviewCreatedVersion', 'at']
    app_name = 'ru.homecredit.mycredit'

    new_csv = scrape(app_name, field_names=fieldnames)

    print("Writing complete")
    new_reviews(old_csv='homecredit_reviews.csv', new_csv=new_csv)