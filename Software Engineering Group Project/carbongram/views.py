import base64
import copy
import os
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_required
from werkzeug.utils import secure_filename
from carbongram.forms import CreatePost, CreateComment
from models import SocialPosts, User, SocialPostLikes, SocialPostComments, UserFriends, ReportedUser, ReportedPost
from app import db

# Config
carbongram_blueprint = Blueprint('carbongram', __name__, template_folder='templates')


@login_required
@carbongram_blueprint.route('/carbongram')
def carbongram():
    """ Render the carbongram main page. """
    # Get all current posts and users
    Posts = SocialPosts.query.all()
    Users = User.query.all()

    postInfo = []
    print(Posts)
    # Make copies of posts
    if Posts:
        PostsCopies = list(map(lambda x: copy.deepcopy(x), Posts))

        # Find out more data for each post such as likes and comments
        # then add all data to 2D array postInfo
        for post in PostsCopies:
            for user in Users:
                if post.UserId == user.id:
                    postLikes = SocialPostLikes.query.filter_by(PostId=post.PostId).all()
                    postLiked = True if 0 < len(
                        SocialPostLikes.query.filter_by(PostId=post.PostId, UserId=current_user.id).all()) else False
                    CommentTotal = len(SocialPostComments.query.filter_by(PostId=post.PostId).all())
                    userF = UserFriends.query.filter_by(user1_id=current_user.id, user2_id=post.UserId).first()
                    userF1 = UserFriends.query.filter_by(user1_id=post.UserId, user2_id=current_user.id).first()
                    friend = False
                    if userF or userF1:
                        friend = True
                    postInfo.append([post, user, postLikes, postLiked, CommentTotal, friend])

        return render_template('carbongram.html', AllPosts=postInfo[::-1], form=CreatePost(), hasNav=True)

    return render_template('carbongram.html')


@login_required
@carbongram_blueprint.route('/add_post', methods=['GET', 'POST'])
def add_post():
    """ Add a new post to the database. """
    if request.method == 'POST':
        if request.form['submit_button'] == 'Post':
            if request.form["text_area"] == "What's on your mind?" or None:
                return carbongram()

            postImage = None
            if request.files['userpostimage']:
                pic = request.files['userpostimage']
                pic.save(os.path.join('static/images', secure_filename(pic.filename)))
                with open('static/images/' + pic.filename, "rb") as img_file:
                    postPic = base64.b64encode(img_file.read())
                postImage = postPic
                os.remove('static/images/' + pic.filename)


            post = SocialPosts(
                UserId=current_user.id,
                PostText=request.form["text_area"],
                PostImg=postImage
            )
            db.session.add(post)
            db.session.commit()

    return redirect(url_for('carbongram.carbongram', form=CreatePost()))


@login_required
@carbongram_blueprint.route('/delete_post', methods=['GET', 'POST'])
def delete_post():
    """ Delete a post from the database. """
    if request.method == 'POST':
        if request.form['submit_button'] == 'Delete Post':
            postId= int(request.form['carbongramDeletePost'])

            SocialPosts.query.filter(SocialPosts.PostId == postId).delete()
            SocialPostLikes.query.filter_by(PostId=postId).delete()
            SocialPostComments.query.filter_by(PostId=postId).delete()
            db.session.commit()

    return redirect(url_for('carbongram.carbongram'))


@login_required
@carbongram_blueprint.route('/like_post', methods=['GET', 'POST'])
def like_post():
    """ Increase the amount of likes on a post. """
    if request.method == 'POST':
        like = SocialPostLikes(
            PostId=request.form['like'],
            UserId=current_user.id
        )
        db.session.add(like)
        db.session.commit()

    return redirect(url_for('carbongram.carbongram'))


@login_required
@carbongram_blueprint.route('/unlike_post', methods=['GET', 'POST'])
def unlike():
    """ Decrease the amount of like on a post. """
    if request.method == 'POST':
        unlike = SocialPostLikes.query.filter_by(PostId=request.form['unlike'], UserId=current_user.id).first()
        db.session.delete(unlike)
        db.session.commit()

    return redirect(url_for('carbongram.carbongram'))


@login_required
@carbongram_blueprint.route('/update/<int:id>', methods=('GET', 'POST'))
def updatePost(id):
    """ Update a post with changes. """
    post = SocialPosts.query.filter_by(PostId=id,UserId=current_user.id).first()
    if not post:
        return redirect(url_for('carbongram.carbongram'))

    form = CreatePost()

    if request.method == 'POST':
        if form.validate_on_submit():
            postImage = None
            if request.files['userpostimage']:
                pic = request.files['userpostimage']
                pic.save(os.path.join('static/images', secure_filename(pic.filename)))
                with open('static/images/' + pic.filename, "rb") as img_file:
                    postPic = base64.b64encode(img_file.read())
                postImage = postPic
                os.remove('static/images/' + pic.filename)


            SocialPosts.query.filter_by(PostId=id).update({"PostText": request.form["updatedPost"],"PostImg":postImage})
            db.session.commit()
            return redirect(url_for('carbongram.carbongram'))

    return render_template('carbongramUpdatePost.html', form=form, post=post, hasNav=True)


@login_required
@carbongram_blueprint.route('/comment/<int:id>', methods=('GET', 'POST'))
def commentPost(id):
    """ Add a comment to SocialPostComments and a post. """
    posts = SocialPosts.query.filter_by(PostId=id).first()
    user = User.query.filter_by(id=posts.UserId).first()
    postComments = []
    post = [posts, user]

    form = CreateComment()

    if not posts:
        return redirect(url_for('carbongram.carbongram'))

    comments = SocialPostComments.query.all()
    try:
        for i in comments:
            if i.PostId == id:
                userComment = User.query.filter_by(id=i.UserId).first()
                postComments.append([i, userComment])
    except():
        pass

    post.append(postComments)
    if request.method == 'POST':
        if form.validate_on_submit():
            if not form.comment.data == "":
                postComment = SocialPostComments(
                    PostId=id,
                    CommentText=form.comment.data,
                    UserId=current_user.id
                )
                db.session.add(postComment)
                db.session.commit()
        return redirect(url_for('carbongram.commentPost', id=id))

    return render_template('carbongramAddComment.html', form=form, post=post, hasNav=True)


@login_required
@carbongram_blueprint.route('/search_for_friend', methods=('GET', 'POST'))
def search_for_friend():
    if request.method == 'POST':
        if len(request.form['searchForFriend']) > 0:
            return search_friend(username=request.form['searchForFriend'])
        else:
            return redirect(url_for('carbongram.carbongram'))


@login_required
@carbongram_blueprint.route('/search/<string:username>', methods=('GET', 'POST'))
def search_friend(username):
    users = User.query.filter(User.id != current_user.id).all()
    userF = UserFriends.query.filter_by(user1_id=current_user.id).all()
    userF1 = UserFriends.query.filter_by(user2_id=current_user.id).all()

    friends = userF + userF1

    searchUser = []
    try:
        for user in users:
            if username.upper() in user.username.upper():

                if UserFriends.query.filter_by(user1_id=current_user.id, user2_id=user.id).first():
                    searchUser.append([user, True])

                elif UserFriends.query.filter_by(user2_id=current_user.id, user1_id=user.id).first():
                    searchUser.append([user, True])

                else:
                    searchUser.append([user, False])

        return render_template('carbongramSearchFreinds.html', users=searchUser, form=CreatePost(), hasNav=True)
    except():
        if len(searchUser) == 0:
            return render_template('carbongramSearchFreinds.html', notFound=True, form=CreatePost(), hasNav=True)


@carbongram_blueprint.route('/profile/<string:username>/<int:id>', methods=('GET', 'POST'))
def userProfile(username, id):
    user = User.query.filter_by(id=id).first()
    Posts = SocialPosts.query.filter_by(UserId=id).all()
    postInfo = []

    if Posts:
        PostsCopies = list(map(lambda x: copy.deepcopy(x), Posts))

        for post in PostsCopies:
            if post.UserId == user.id:
                postLikes = SocialPostLikes.query.filter_by(PostId=post.PostId).all()
                postLiked = True if 0 < len(
                    SocialPostLikes.query.filter_by(PostId=post.PostId, UserId=id).all()) else False
                CommentTotal = len(SocialPostComments.query.filter_by(PostId=post.PostId).all())
                userF = UserFriends.query.filter_by(user1_id=id, user2_id=post.UserId).first()
                userF1 = UserFriends.query.filter_by(user1_id=post.UserId, user2_id=id).first()
                friend = False
                if userF or userF1:
                    friend = True
                postInfo.append([post, user, postLikes, postLiked, CommentTotal, friend])

    accFriend = []

    userF = UserFriends.query.filter(UserFriends.user1_id == id).limit(6).all()
    userF1 = UserFriends.query.filter(UserFriends.user2_id == id).limit(6).all()
    friend = False
    friends = userF + userF1
    if friends:
        for friend in friends:
            if UserFriends.query.filter_by(user1_id=current_user.id, user2_id=friend.id).first():
                friend = True
            elif UserFriends.query.filter_by(user2_id=current_user.id, user1_id=friend.id).first():
                friend = True
            if friend.user1_id == id:
                accFriend.append(User.query.filter_by(id=friend.user2_id).first())
            else:
                accFriend.append(User.query.filter_by(id=friend.user1_id).first())

    return render_template('carbongramProfiles.html', user=user, Posts=postInfo
                           , friends=accFriend, form=CreatePost(), friend=friend, hasNav=True)


@login_required
@carbongram_blueprint.route('/addFriend', methods=('GET', 'POST'))
def addFriend():
    id2 = User.query.filter_by(id=request.form['addFriend']).first()
    friend = UserFriends(
        user1_id=current_user.id,
        user2_id=id2.id,
        starredFriend=False
    )
    db.session.add(friend)
    db.session.commit()

    return redirect(url_for('carbongram.carbongram'))


@login_required
@carbongram_blueprint.route('/change_cover', methods=['GET', 'POST'])
def change_cover():
    if request.method == 'POST':
        user = User.query.filter_by(id=current_user.id).first()

        pic = request.files['userCoverPic']
        pic.save(os.path.join('static/images', secure_filename(pic.filename)))
        with open('static/images/' + pic.filename, "rb") as img_file:
            accountCover = base64.b64encode(img_file.read())
        user.accountCover = accountCover
        os.remove('static/images/' + pic.filename)

        db.session.commit()

    return redirect(url_for('carbongram.userProfile', username=current_user.username, id=current_user.id))


@login_required
@carbongram_blueprint.route('/reportAccount', methods=('GET', 'POST'))
def reportAccount():
    rAccount = ReportedUser(
        UserId=request.form['reportedAccount']
    )
    db.session.add(rAccount)
    db.session.commit()

    return redirect(url_for('carbongram.carbongram'))


@login_required
@carbongram_blueprint.route('/reportPost', methods=('GET', 'POST'))
def reportPost():
    reportPost = ReportedPost(
        PostId=request.form['reportPost']
    )
    db.session.add(reportPost)
    db.session.commit()

    return redirect(url_for('carbongram.carbongram'))

@login_required
@carbongram_blueprint.route('/removeFriend', methods=('GET', 'POST'))
def removeFriend():
    f2 = UserFriends.query.filter_by(user1_id=request.form['removeFriend'], user2_id=current_user.id).first()
    f1 = UserFriends.query.filter_by(user2_id=request.form['removeFriend'], user1_id=current_user.id).first()

    if f1:
        UserFriends.query.filter_by(id=f1.id).delete()
    if f2:
        UserFriends.query.filter_by(id=f2.id).delete()
    db.session.commit()

    return redirect(url_for('carbongram.carbongram'))
