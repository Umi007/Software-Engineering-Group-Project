from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user

from admin.forms import FAQForm, linkForm
from RBAC import require_role
from app import db
from models import FAQ, UsefulLinks, User, ReportedUser, SocialPosts, SocialPostLikes, SocialPostComments, ReportedPost

# Config
admin_blueprint = Blueprint('admin', __name__, template_folder='templates')


@admin_blueprint.route('/admin')
@login_required
@require_role('admin')
def admin():
    """ Render the admin page when the link is pressed. """
    return render_template('admin.html', hasNav=True)


@admin_blueprint.route('/viewFAQ', methods=['GET'])
@login_required
@require_role('admin')
def viewFAQ():
    """ When FAQ button is pressed query the database and re-render admin with records. """
    faqs = FAQ.query.all()

    return render_template('admin.html', faqs=faqs, hasNav=True)


@admin_blueprint.route('/viewLinks', methods=['GET'])
@login_required
@require_role('admin')
def viewLinks():
    """ When useful link button is pressed query the database and re-render admin with records. """
    links = UsefulLinks.query.all()

    return render_template('admin.html', linksC=True,links=links, hasNav=True)


@admin_blueprint.route('/<int:id>/deleteFAQ')
@login_required
@require_role('admin')
def deleteFAQ(id):
    """ Delete FAQ record based on id. """
    FAQ.query.filter_by(FAQID=id).delete()
    db.session.commit()
    faqs = FAQ.query.all()

    return render_template('admin.html', faqs=faqs, hasNav=True)


@admin_blueprint.route('/<int:id>/deleteLink')
@login_required
@require_role('admin')
def deleteLink(id):
    """ Delete useful link record based on id. """
    UsefulLinks.query.filter_by(linkID=id).delete()
    db.session.commit()
    links = UsefulLinks.query.all()

    return render_template('admin.html', links=links, hasNav=True)


@admin_blueprint.route('/<int:id>/updateFAQ', methods=['GET', 'POST'])
@login_required
@require_role('admin')
def updateFAQ(id):
    """ Render the page for updating an FAQ and alter record based on input data."""
    faq = FAQ.query.filter_by(FAQID=id).first()
    form = FAQForm()

    if form.validate_on_submit():
        faq.update(form.question.data, form.answer.data, form.approved.data)

        return admin()

    form.question.data = faq.question
    form.answer.data = faq.answer
    form.approved.data = faq.approved

    return render_template('updateFAQ.html', form=form, hasNav=True)


@admin_blueprint.route('/<int:id>/updateLinks', methods=['GET', 'POST'])
@login_required
@require_role('admin')
def updateLink(id):
    """ Render the page for updating a useful link and alter record based on input data."""
    link = UsefulLinks.query.filter_by(linkID=id).first()
    form = linkForm()

    if form.validate_on_submit():
        link.update(form.name.data, form.link.data, form.description.data)

        return admin()

    form.name.data = link.name
    form.link.data = link.link
    form.description.data = link.description

    return render_template('updateLink.html', form=form, hasNav=True)


@admin_blueprint.route('/logs', methods=['POST'])
@login_required
@require_role('admin')
def logs():
    """ Get the latest 10 records entered in the security log and render them. """
    with open("carbon.log", "r") as f:
        content = f.read().splitlines()[-10:]
        content.reverse()

    return render_template('admin.html', logs=content, name=current_user.firstname, hasNav=True)


@admin_blueprint.route('/addAdmins')
@login_required
@require_role('admin')
def addAdmins():
    """ Render a admin control page with all admin users to manage access levels. """
    admins = User.query.filter_by(role="admin").all()

    return render_template('adminAdminControl.html', admins=admins, hasNav=True)


@login_required
@admin_blueprint.route('/searchUser', methods=['GET', 'POST'])
@require_role('admin')
def searchUser():
    users = User.query.filter_by(role="user").all()
    admins = User.query.filter_by(role="admin").all()

    seachUser = []
    try:

        for user in users:
            print(request.form['searchForFriend'])
            if request.form['searchForFriend'].upper() in user.username.upper():
                seachUser.append(user)

        return render_template('adminAdminControl.html', admins=admins, users=users)
    except():
        if len(seachUser) == 0:
            return render_template('adminAdminControl.html', admins=admins)


@login_required
@admin_blueprint.route('/AddUserAdmin', methods=['GET', 'POST'])
@require_role('admin')
def AddUserAdmin():
    """ Update user role to admin. """
    try:
        user = User.query.filter(User.id == request.form['addAdmin']).first()
        user.role = "admin"
        db.session.commit()
    except():
        pass

    return redirect(url_for('admin.addAdmins'))


@login_required
@admin_blueprint.route('/removeAdmin', methods=['GET', 'POST'])
@require_role('admin')
def removeAdmin():
    """ Update a user role to user. """
    try:
        user = User.query.filter(User.id == request.form['removeAdmin']).first()
        user.role = "user"
        db.session.commit()
    except():
        pass

    return redirect(url_for('admin.addAdmins'))


@login_required
@admin_blueprint.route('/addLink', methods=['POST'])
@require_role('admin')
def addLink():
    """ This method creates a new link and adds it to the database. """
    name = request.form.get("name")
    link = request.form.get("link")
    description = request.form.get("description")

    new_link = UsefulLinks(name=name, link=link, description=description)

    db.session.add(new_link)
    db.session.commit()

    links = UsefulLinks.query.all()

    return render_template('admin.html', links=links, hasNav=True)


@admin_blueprint.route('/viewReportedUsers', methods=['GET', 'POST'])
@login_required
@require_role('admin')
def viewReportedUsers():
    """ Gets all users who have been reported """
    reportedUsersC = ReportedUser.query.all()
    reportedUsers = []
    for rUser in reportedUsersC:
        print(rUser.UserId)
        reportedUsers.append(User.query.filter_by(id=rUser.UserId).first())

    return render_template('admin.html', reportedUsers=reportedUsers, name=current_user.firstname, hasNav=True)


@admin_blueprint.route('/deleteUser', methods=['GET', 'POST'])
@login_required
@require_role('admin')
def deleteUser():
    """ Deletes Users from the database. """
    if request.method == 'POST':
        User.query.filter_by(id=request.form['deleteUser']).delete()

    ReportedUser.query.filter_by(UserId=request.form['deleteUser']).delete()
    SocialPosts.query.filter_by(UserId=request.form['deleteUser']).delete()
    SocialPostLikes.query.filter_by(UserId=request.form['deleteUser']).delete()
    SocialPostComments.query.filter_by(UserId=request.form['deleteUser']).delete()

    db.session.commit()
    return viewReportedUsers()


@admin_blueprint.route('/viewReportedPost', methods=['GET', 'POST'])
@login_required
@require_role('admin')
def viewReportedPost():
    """ Gets all users who have been reported """
    ReportedPostC = ReportedPost.query.all()
    AllPosts = []

    for rPost in ReportedPostC:
        post = SocialPosts.query.filter_by(PostId=rPost.PostId).first()
        print(post)
        user = User.query.filter_by(id=post.UserId).first()
        AllPosts.append([post, user])

    return render_template('admin.html', AllPosts=AllPosts, name=current_user.firstname, hasNav=True)


@admin_blueprint.route('/deletePost', methods=['GET', 'POST'])
@login_required
@require_role('admin')
def deletePost():
    """ Deletes reported Post """

    SocialPosts.query.filter_by(PostId=request.form['deletePost']).delete()
    ReportedPost.query.filter_by(PostId=request.form['deletePost']).delete()
    db.session.commit()

    return viewReportedPost()
