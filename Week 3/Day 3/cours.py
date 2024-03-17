# import time
# import os
# begin = time.time()
# def create_directories():
#     for week_num in range(1, 6):
#         week_dir = f'week{week_num}'
#         time.sleep(1)
#         os.makedirs(week_dir, exist_ok=True)
#         for day_num in range(1, 6):
#             day_dir = os.path.join(week_dir, f'day{day_num}')
#             os.makedirs(day_dir, exist_ok=True)
#             lesson_dir = os.path.join(day_dir, 'lesson')
#             homework_dir = os.path.join(day_dir, 'homework')
#             os.makedirs(lesson_dir, exist_ok=True)
#             os.makedirs(homework_dir, exist_ok=True)
#     print("Directories created successfully!")
# after = time.time()
# if __name__ == "__main__":
#     create_directories()
# print(f"It took {after - begin} seconds to execute")

# import datetime

# today_date = datetime.date.today()
# actual_datetime = datetime.datetime.now()
# in_15_hours = actual_datetime + datetime.timedelta(hours=15, minutes=10)

# print(f"Today is the {today_date.strftime("%d/%m")}")
# print(f"In 15 hours and 10 minutes it will be the {in_15_hours.strftime("%d/%m")}")

from datetime import datetime

def countdown_to_birthday():
    # Date de mon anniversaire
    birthday = datetime(2024, 10, 24)
    
    # Date actuelle
    today = datetime.now()

    # Calcul du nombre de jours restants
    days_remaining = (birthday - today).days

    # Calcul du temps restant dans heures, minutes et secondes
    seconds_remaining = (birthday - today).total_seconds()
    hours_remaining = int(seconds_remaining // 3600)
    minutes_remaining = int((seconds_remaining % 3600) // 60)
    seconds_remaining = int(seconds_remaining % 60)

    # Affichage du compte à rebours
    print(f"Mon anniversaire est dans {days_remaining} jours, et {hours_remaining:02d}:{minutes_remaining:02d}:{seconds_remaining:02d}")

if __name__ == "__main__":
    countdown_to_birthday()
