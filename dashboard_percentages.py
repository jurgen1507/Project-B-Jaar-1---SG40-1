total_percentage = 0
total_percentage_angle = 0
def achievement_percentage(globalachievements):
    percentage = []

    for x in globalachievements[0]['achievementpercentages']['achievements']:
        percentage.append(x['percent'])

    global total_percentage
    if len(percentage) > 0:
        total_percentage = sum(percentage) / len(percentage)
    global total_percentage_angle
    total_percentage_angle = total_percentage * 3.6

if __name__ == '__main__':
    achievement_percentage()







