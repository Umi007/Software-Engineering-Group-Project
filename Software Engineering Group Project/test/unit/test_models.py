import base64
import unittest
from models import User, SurveyResult, QuizResult, UserFriends, SocialPosts, SocialPostLikes, SocialPostComments, FAQ, \
    UsefulLinks, ReportedUser, ReportedPost


class test_models(unittest.TestCase):

    def test_user(self):
        with open("./img/profile-picture.png", "rb") as img_file:
            profile_img = base64.b64encode(img_file.read())

        user = User("test@email.co.uk",
                    "testFirst",
                    "testSur",
                    "testUsername",
                    "Test1!",
                    "user",
                    profile_img)
        assert user.email == "test@email.co.uk"
        assert user.firstname == "testFirst"
        assert user.surname == "testSur"
        assert user.username == "testUsername"
        assert user.password != "Test1!"
        assert user.role == "user"

    def test_survey_result(self):
        with open("./img/profile-picture.png", "rb") as img_file:
            profile_img = base64.b64encode(img_file.read())
        SurveyResultT = SurveyResult(1,
                                     6,
                                     3,
                                     4,
                                     4,
                                     4,
                                     profile_img,
                                     "2022-01-16 00:00:00.000000")
        assert SurveyResultT.user_id == 1
        assert SurveyResultT.carbon_emissions == 6
        assert SurveyResultT.food == 3
        assert SurveyResultT.transport == 4
        assert SurveyResultT.purchasing == 4
        assert SurveyResultT.energy == 4
        assert SurveyResultT.date == "2022-01-16 00:00:00.000000"

    def test_quiz_result(self):
        QuizResultT = QuizResult(
            1,
            "11111BBADE",
            5,
            "general")

        assert QuizResultT.user_id == 1
        assert QuizResultT.user_answer == "11111BBADE"
        assert QuizResultT.user_mark == 5
        assert QuizResultT.quiz_category == "general"


    def test_user_friend(self):

        UserFriendT = UserFriends(
            1,
            2,
            True)

        assert UserFriendT.user1_id == 1
        assert UserFriendT.user2_id == 2
        assert UserFriendT.starredFriend == True

    def test_social_post(self):
        SocialPostT = SocialPosts(
            1,
            "TestPost",
            None)

        assert SocialPostT.UserId == 1
        assert SocialPostT.PostText == "TestPost"
        assert SocialPostT.PostImg == None

    def test_social_post_likes(self):
        SocialPostsLikesT = SocialPostLikes(
            1,
            2)

        assert SocialPostsLikesT.UserId == 2
        assert SocialPostsLikesT.PostId == 1

    def test_social_post_comments(self):
        SocialPostCommentsT = SocialPostComments(
            2,
            "TestComment",
            2
        )

        assert SocialPostCommentsT.PostId == 2
        assert SocialPostCommentsT.CommentText == "TestComment"
        assert SocialPostCommentsT.UserId == 2

    def test_faq(self):
        FAQT = FAQ(
            "testQuestion",
            "testAnswer",
            True
        )

        assert FAQT.question == "testQuestion"
        assert FAQT.answer == "testAnswer"
        assert FAQT.approved == True

        FAQT.update("updatedQuestion","updatedAnswer",False)

        assert FAQT.question == "updatedQuestion"
        assert FAQT.answer == "updatedAnswer"
        assert FAQT.approved == False

    def test_useful_links(self):
        UsefulLinksT = UsefulLinks("testName",
                                   "testLink",
                                   "testDesc")

        assert UsefulLinksT.name == "testName"
        assert UsefulLinksT.link == "testLink"
        assert UsefulLinksT.description == "testDesc"

        UsefulLinksT.update("updatedName",
                            "updatedLink",
                            "updatedDesc")

        assert UsefulLinksT.name == "updatedName"
        assert UsefulLinksT.link == "updatedLink"
        assert UsefulLinksT.description == "updatedDesc"


    def test_reported_user(self):
        reportedUserT = ReportedUser(1)

        assert reportedUserT.UserId == 1

    def test_reported_post(self):
        reportedPostT = ReportedPost(1)

        assert reportedPostT.PostId == 1

if __name__ == '__main__':
    unittest.main()
