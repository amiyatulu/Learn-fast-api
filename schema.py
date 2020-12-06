import graphene
from database import db
from typing import List

from serializers import (
    UserGrapheneInputModel,
    UserGrapheneModel,
    PostGrapheneInputModel,
    PostGrapheneModel,
    CommentGrapheneInputModel,
    CommentGrapheneModel,
    UserModel,
)



class Query(graphene.ObjectType):
    all_users = graphene.List(UserGrapheneModel)

    @staticmethod
    def resolve_all_users(parent, info):
        # print(info.context['request'])
        cursor = db.aql.execute(
         'FOR s IN user RETURN s'   
        )
        usermodels = [UserModel(**document) for document in cursor]
        return usermodels


class CreateUser(graphene.Mutation):
    class Arguments:
        user_details = UserGrapheneInputModel()

    Output = UserGrapheneModel

    @staticmethod
    def mutate(parent, info, user_details):
        cursor = db.aql.execute(
            'INSERT {name:@name, surname: @surname, alive: @alive, traits: @traits} INTO "user" RETURN NEW',
            bind_vars = user_details)
        user = [document for document in cursor]
        print(user)
        usermodel = UserModel(**user[0])
        return usermodel


# class CreatePost(graphene.Mutation):
#     class Arguments:
#         post_details = PostGrapheneInputModel()

#     Output = PostGrapheneModel

#     @staticmethod
#     def mutate(parent, info, post_details):
#         user = User.find_or_fail(post_details.user_id)
#         post = Post()
#         post.title = post_details.title
#         post.body = post_details.body

#         user.posts().save(post)

#         return post


# class CreateComment(graphene.Mutation):
#     class Arguments:
#         comment_details = CommentGrapheneInputModel()

#     Output = CommentGrapheneModel

#     @staticmethod
#     def mutate(parent, info, comment_details):
#         user = User.find_or_fail(comment_details.user_id)
#         post = Post.find_or_fail(comment_details.post_id)

#         comment = Comments()
#         comment.body = comment_details.body

#         user.comments().save(comment)
#         post.comments().save(comment)

#         return comment


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    # create_post = CreatePost.Field()
    # create_comment = CreateComment.Field()