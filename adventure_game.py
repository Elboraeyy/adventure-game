# بعض المكتبات المستخدمه لانشاء اللعبه
import sys
import time
import random


# هتان الدالتان تستخدم لإعطاء تأثير الطباعة البطيئة أثناء تشغيل البرنامج مع
# تاخير ثانيه بين طباعة كل امرين
def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()


def print_slow_and_sleep(text, sleep_time=1):
    print_slow(text)
    time.sleep(sleep_time)


# هذه الدالة تأخذ متغير 'points' وتطبع عدد النقاط الحالية للمستخدم
def print_points(points):
    print_slow_and_sleep(f"your points now are {points}")


# هذه الدالة تقوم بتحديد حالة الطقس عشوائية
def random_weather():
    weather = random.choice(['cloudy', 'rainy', 'stormy'])
    print_slow_and_sleep(f"today's weather : {weather}")


# هذه الدالة تقوم باختيار عدد عشوائي من النقاط
def random_points():
    points = random.choice([5, 10, 15, 20, 25, 30])
    return points


# هذه الدالة تستمر في طلب إدخال جديد حتى يدخل المستخدم
# خيارًا صحيحًا من القائمة المحددة
def get_choice(prompt, valid_choices):
    choice = input(prompt).lower()
    while choice not in valid_choices:
        choice = input("Please enter only "
                       "{}: ".format(" or ".join(valid_choices))).lower()
    return choice


# هذه الدالة تبدأ لعبة المغامرة حيث يجب
# على اللاعب الحصول على 30 نقطة للفوز والعودة إلى المنزل.
# تقوم هذه الدالة بطباعة مقدمة اللعبة وحالة الطقس العشوائية،
# ومن ثم تطلب من اللاعب اختيار أحد المسارات المحدده
def start_game():
    points = 0
    print_slow_and_sleep("You find yourself in a strange place you "
                         "don't know and need to get back to your home.")
    print_slow_and_sleep("You need to get 30 points to win "
                         "the game and return home.")
    random_weather()
    print_points(points)
    choice = get_choice("You face four paths: forest (enter 1), dark cave "
                        "(enter 2), abandoned house (enter 3), random event "
                        "(enter 4). Choose the path: ", ['1', '2', '3', '4'])

    if choice == '1':
        points += 5
        print_slow_and_sleep("your got 5 points")
        print_points(points)
        forest_path(points)
    elif choice == '2':
        points += 5
        print_slow_and_sleep("your got 5 points")
        print_points(points)
        cave_path(points)
    elif choice == '3':
        points += 5
        print_slow_and_sleep("your got 5 points")
        print_points(points)
        abandoned_house_path(points)
    else:
        points += 10
        print_slow_and_sleep("your got 10 points")
        print_points(points)
        random_event(points)


# هذه الدالة تستدعي في حالة عودة اللاعب الي نقطة البدايه دون ان بخسر باللعبه
def return_to_start(points):
    print_slow_and_sleep("You returned to the starting point.")
    print_points(points)
    choice = get_choice("You face four paths: forest (enter 1), dark cave "
                        "(enter 2), abandoned house (enter 3), random event"
                        "(enter 4). Choose the path: ", ['1', '2', '3', '4'])

    if choice == '1':
        points += 5
        print_slow_and_sleep("your got 5 points")
        print_points(points)
        forest_path(points)
    elif choice == '2':
        points += 5
        print_slow_and_sleep("your got 5 points")
        print_points(points)
        cave_path(points)
    elif choice == '3':
        points += 5
        print_slow_and_sleep("your got 5 points")
        print_points(points)
        abandoned_house_path(points)
    else:
        points += 10
        print_slow_and_sleep("your got 10 points")
        print_points(points)
        random_event(points)


# هذه الدالة تعبر عن احد مسارات
# اللاعب (الغابه) وتتحدد النفاط علي حسب اختياراته
def forest_path(points):
    choice = get_choice("You face three paths: dark (enter 1), bright "
                        "(enter 2), mysterious gate (enter 3). Choose "
                        "the path: ", ['1', '2', '3'])

    if choice == '1':
        points -= 5
        print_slow_and_sleep("your lost 5 points")
        print_points(points)
        print_slow_and_sleep("You found a ferocious lion that kills you.")
        print_slow_and_sleep("You lost the game!")
        restart_game()
    elif choice == '3':
        mysterious_gate_path(points)
    else:
        points += 10
        print_slow_and_sleep("your got 5 points")
        print_points(points)
        print_slow_and_sleep("You found a map and got an "
                             "additional 15 points!")
        points += 15
        print_points(points)
        if points >= 30:
            print_slow_and_sleep("You won the game and returned home!")
        restart_game()


# هذه الدالة تعبر عن احد مسارات اللاعب (الكهف)
# وتتحدد النفاط علي حسب اختياراته
def cave_path(points):
    choice = get_choice("You face three rooms: dark (enter 1), and slightly "
                        "lit (enter 2), mysterious gate path (enter 3)."
                        " Choose the room: ", ['1', '2', '3'])

    if choice == '1':
        points -= 5
        print_slow_and_sleep("your lost 5 points")
        print_points(points)
        print_slow_and_sleep("You found a big bear that kills you.")
        print_slow_and_sleep("You lost the game!")
        restart_game()
    elif choice == '3':
        mysterious_gate_path(points)
    else:
        points += 10
        print_slow_and_sleep("your got 5 points")
        print_points(points)
        points += 15
        print_slow_and_sleep("You found a map and got"
                             " an additional 15 points!")
        print_points(points)
        if points >= 30:
            print_slow_and_sleep("You won the game and returned home!")
        else:
            print_slow_and_sleep("You didn't get enough points"
                                 " to win the game.")
        restart_game()


# هذه الدالة تعبر عن احد مسارات اللاعب
# (البيت المهجور) وتتحدد النفاط علي حسب اختياراته
def abandoned_house_path(points):
    choice = get_choice("An evil witch appears before you. Do you want to"
                        " enter with her (enter 1) or run "
                        "away (enter 2)? ", ['1', '2'])

    if choice == '1':
        points -= 5
        print_slow_and_sleep("your lost 5 points")
        print_points(points)
        print_slow_and_sleep("The evil witch killed you.")
        print_slow_and_sleep("You lost the game!")
        restart_game()
    else:
        points += 10
        print_slow_and_sleep("your got 10 points")
        print_points(points)
        print_slow_and_sleep("You successfully escaped and "
                             "returned to the starting point.")
        choice = get_choice("You face two paths: forest (enter 1), dark cave"
                            " (enter 2), random event(enter 3). "
                            "Choose the path: ", ['1', '2', '3'])
        if choice == '1':
            points += 5
            print_slow_and_sleep("your got 5 points")
            print_points(points)
            forest_path(points)
        if choice == '2':
            points += 5
            print_slow_and_sleep("your got 5 points")
            print_points(points)
            cave_path(points)
        else:
            points += 5
            print_slow_and_sleep("your got 5 points")
            print_points(points)
            random_event(points)


# هذه الدالة عباره عن احد التحديات
# (البوابه الغامضه) اللتي سيواجهها اللاعب خلال طريقه الي المنزل
def mysterious_gate_path(points):
    print_slow_and_sleep("You found a mysterious gate with a sign "
                         "that reads: 'Test your luck'.")
    print_slow_and_sleep("You can pass through the gate for a chance to"
                         " increase your points or lose them all.")
    choice = get_choice("Do you want to pass through the gate? "
                        "(yes(enter y)/no(enter n)): ", ['y', 'n'])

    if choice == 'y':
        print_slow_and_sleep("You took a risk and passed through the gate...")
        luck = random.choice(["good", "bad"])
        if luck == "good":
            additional_points = random_points()
            points += additional_points
            print_slow_and_sleep(f"Congratulations!You got {additional_points}"
                                 " additional points. You "
                                 "now have {points} points.")
        else:
            print_slow_and_sleep("Unfortunately, you were not lucky. "
                                 "You lost all your points.")
            points = 0
            print_points(points)
    else:
        points -= 5
        print_slow_and_sleep("You decided not to take the"
                             " risk and continue the adventure.")
        print_points(points)

    if points >= 30:
        print_slow_and_sleep("You won the game and returned home!")
        restart_game()
    else:
        return_to_start(points)


# هذه الدالة عباره عن احد التحديات اللتي
# سيواجهها اللاعب خلال طريقه الي المنزل ولكنها تعتمد علي العشوائيه
def random_event(points):
    events = ['mad_killer', 'find_coins', 'meet_wise_man']

    selected_event = random.choice(events)

    if selected_event == 'mad_killer':
        print_slow_and_sleep("You found a mad killer attacking you!")
        print_slow_and_sleep("You lost the game!")
        restart_game()
    elif selected_event == 'find_coins':
        print_slow_and_sleep("You found a bunch of coins!")
        additional_points = random_points()
        points += additional_points
        print_slow_and_sleep(f"You got {additional_points} additional "
                             "points. You now have {points} points.")
        if points >= 30:
            print_slow_and_sleep("You won the game and returned home!")
            restart_game()
        else:
            return_to_start(points)
    else:
        print_slow_and_sleep("You met a wise man who offers "
                             "you valuable advice.")
        additional_points = random_points()
        points += additional_points
        print_slow_and_sleep(f"You got {additional_points} additional points."
                             " You now have {points} points.")
        if points >= 30:
            print_slow_and_sleep("You won the game and returned home!")
            restart_game()
        else:
            print_slow_and_sleep("You didn't get enough "
                                 "points to win the game.")
            return_to_start(points)


# هذه الدالة تطلب من اللاعب اتخاذ قرار بشأن إعادة تشغيل اللعبة أو الخروج منها
def restart_game():
    choice = get_choice("Do you want to restart the"
                        " game (enter y) or exit (enter n)? ", ['y', 'n'])

    if choice == 'y':
        print_slow_and_sleep("Restarting the game...")
        start_game()
    else:
        print_slow_and_sleep("Thanks for playing! Goodbye!")
        sys.exit()


if __name__ == "__main__":
    start_game()
