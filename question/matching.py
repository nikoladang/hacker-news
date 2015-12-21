from django.contrib.auth import get_user_model

from question.models import UserAnswer

User = get_user_model()

users = User.objects.all()
all_user_answers = UserAnswer.objects.all().order_by('user__id')

def get_match(user_a, user_b):
    user_a_answers = UserAnswer.objects.filter(user=user_a)[0]
    print(user_a_answers)
    user_b_answers = UserAnswer.objects.filter(user=user_b)[0]
    print(user_b_answers)

    if user_a_answers.question.id == user_b_answers.question.id:
        user_a_answer = user_a_answers.my_answer
        user_a_pref = user_a_answers.their_answer
        user_b_answer = user_b_answers.my_answer
        user_b_pref = user_b_answers.their_answer
        user_a_total_awarded = 0
        user_b_total_awarded = 0

        if user_a_answer == user_b_pref:
            user_b_total_awarded += user_b_answers.their_points
            print("user {0} fits with user {1}'s preference").format(user_a_answers.user.username, user_b_answers.user.username)
            pass

        if user_b_answer == user_a_pref:
            user_a_total_awarded += user_a_answers.their_points
            print("user b fits with user a's preference").format(user_a_answers.user.username, user_b_answers.user.username)
            pass

        if user_a_answer == user_b_pref and user_a_pref == user_b_answer:
            print("This is an ideal answer for both")

        print(user_a, user_a_total_awarded, user_b)
        print(user_b, user_b_total_awarded, user_b)
        print("zzzzz")

jmitchel3 = users[0]
khaleesi = users[1]

get_match(jmitchel3, khaleesi)


def get_points(user_a, user_b):
    a_answers = UserAnswer.objects.filter(user=user_a)[0]
    b_answers = UserAnswer.objects.filter(user=user_b)[0]
    a_total_awarded = 0
    a_points_possible = 0
    if a_answers.question.id == b_answers.question.id:
        a_pref = a_answers.their_answer
        b_answer = b_answers.my_answer
        if a_pref == b_answer:
            '''
            awards points for correct answer
            '''
            a_total_awarded += a_answers.their_points
        '''
        assigning total points
        '''
        a_points_possible += a_answers.their_points
    print("{0} has awarded {1} points of {2} to {3}").format(user_a, a_total_awarded, a_points_possible, user_b)

# TODO Working on lecture 025