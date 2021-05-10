from datetime import datetime, timedelta

users = [{"name": "Max", "birthday": datetime(year=2021, month=5, day=18)},
         {"name": "Andrew", "birthday": datetime(year=2021, month=5, day=20)},
         {"name":"Anton", "birthday":datetime(year=2021, month=8, day=19)},
         {"name":"Anton", "birthday":datetime(year=2021, month=6, day=5)},
         {"name": "Alexandr", "birthday": datetime(year=2021, month=5, day=22)}]

Monday = []
Tuesday = []
Wednesday = []
Thursday = []
Friday = []

def congratulate(users):
    current_day = datetime.now()
    start_next_week = current_day + timedelta(6 - current_day.weekday())
    stop_next_week = start_next_week + timedelta(7 + start_next_week.weekday())
    
    for user in users:
        if start_next_week <= user["birthday"] <= stop_next_week:
            if user["birthday"].strftime('%A') == 'Monday':
                Monday.append(user['name'])
            elif user["birthday"].strftime('%A') == 'Tuesday':
                Tuesday.append(user['name'])
            elif user["birthday"].strftime('%A') == 'Wednesday':
                Wednesday.append(user['name'])
            elif user["birthday"].strftime('%A') == 'Thursday':
                Thursday.append(user['name'])
            elif user["birthday"].strftime('%A') == 'Friday':
                Friday.append(user['name'])
            elif user["birthday"].strftime('%A') == 'Saturday':
                Monday.append(user['name'])
            elif user["birthday"].strftime('%A') == 'Sunday':
                Monday.append(user['name'])
                
    if len(Monday) > 0:
        print('Monday: ', *Monday)
    if len(Tuesday) > 0:
        print('Tuesday: ', *Tuesday)
    if len(Wednesday) > 0:    
        print('Wednesday: ', *Wednesday)
    if len(Thursday) > 0:
        print('Thursday:', *Thursday)
    if len(Friday) > 0:
        print('Friday:', *Friday)
        
if __name__ == '__main__':       
    congratulate(users)