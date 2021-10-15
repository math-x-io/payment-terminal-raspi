from flask import Flask, jsonify
from flask_restx import Resource, Namespace, fields

from .utils import abort_if_doesnt_exist, authentification_required

from database.user import User
from database.database import Database
from datetime import datetime

ns = Namespace('users', description='Users related operations')


@ns.route('/users')
class Users(Resource):
    @authentification_required
    def get(self):
        user_list = []
        with Database(auto_commit=True) as db:
            result = db.query(User).all()
            for user in result:
                user_list.append(user.to_public_dict(
                    User.user_id,
                    User.name,
                    User.first_name,
                    User.email,
                    User.creation_date
                ))
        return jsonify(user_list)


USER_UPDATE_PARAMS = ns.model('Updating user parameter', {
    "name": fields.String(required=True),
    "firstName": fields.String(required=True),
    "email": fields.String(required=True)
})

@ns.route('/user/user_id/<user_id>')
class SingleUser(Resource):
    @authentification_required
    def get(self, user_id):
        user = None

        with Database(auto_commit=True) as db:
            user = db.query(User).filter_by(user_id=user_id).first()
            if user:
                user = user.to_public_dict(
                    User.user_id,
                    User.name,
                    User.first_name,
                    User.email,
                    User.creation_date,
                    User.currency_amount,
                )

        abort_if_doesnt_exist(
            user, 
            code=400, 
            message="No user found with this user id"
        )

        return jsonify(user)

    @ns.expect(USER_UPDATE_PARAMS, validate=True)
    @authentification_required
    def put(self, user_id, **kwargs):
        return update_user(
            card_uid=None,
            user_id=user_id,
            name=str(ns.payload["name"]),
            first_name=str(ns.payload["firstName"]),
            email=str(ns.payload["email"])
        )

@ns.route('/user/card_uid/<card_uid>')
class SingleUserCardUID(Resource):
    @authentification_required
    def get(self, card_uid):
        user = None

        with Database(auto_commit=True) as db:
            user = db.query(User).filter_by(card_uid=card_uid).first()
            if user:
                user = user.user.to_public_dict(
                    User.user_id,
                    User.name,
                    User.first_name,
                    User.email,
                    User.creation_date,
                    User.currency_amount,
                )

        abort_if_doesnt_exist(
            user, 
            code=400, 
            message="No user found with this card id"
        )

        return jsonify(user)

    @ns.expect(USER_UPDATE_PARAMS, validate=True)
    @authentification_required
    def put(self, card_uid, **kwargs):
        return update_user(
            card_uid=card_uid,
            user_id=None,
            name=str(ns.payload["name"]),
            first_name=str(ns.payload["firstName"]),
            email=str(ns.payload["email"])
        )

def update_user(card_uid, user_id, name, first_name, email):

    with Database(auto_commit=True) as db:

        abort_if_doesnt_exist(
            name, 
            first_name,
            email,
            message="Server could not get parameters properly",
            code=500
        )

        user = db.query(User).filter_by(card_uid=card_uid).first() if card_uid \
            else db.query(User).filter_by(user_id=user_id).first()
        abort_if_doesnt_exist(user, code=400, message="No user found with this card id")

        user.update_date = datetime.now()
        user.name = name
        user.first_name = first_name
        user.email = email
        db.commit()

    return True
