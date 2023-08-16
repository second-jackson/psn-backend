from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from message_app.classes.create_comment import CreateCommentOperation
from message_app.classes.update_comment import UpdateCommentOperation
from message_app.classes.get_comment import GetCommentOperation
from api.shortcuts.data_get import process_and_get_response


class MessageView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        create_comment_instance = CreateCommentOperation(request=request)
        return process_and_get_response(create_comment_instance)

    def put(self, request):
        update_comment_instance = UpdateCommentOperation(request=request)
        return process_and_get_response(update_comment_instance)

    def get(self, request, id):
        get_comment_instance = GetCommentOperation(request=request, post_id=id)
        return process_and_get_response(get_comment_instance)
