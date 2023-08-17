from posts_app.models import PostModel
from api.decorators.validate_serializer import validate_serializer
from .create_update_comment_operations import CreateUpdateCommentOperations


class CreateCommentOperation(CreateUpdateCommentOperations):
    def __init__(self, request):
        super().__init__(request=request)
        self._post_instance = self.get_commented_post()

    def create_or_update_process(self):
        self.instance_manager.instance = self.serializer_manager.serializer.create(
            validated_data=self.serializer_manager.serializer.validated_data)

        self.add_created_message_to_post()

    def add_created_message_to_post(self):
        self._post_instance.messages.add(self.instance_manager.instance)

    def get_commented_post(self):
        post_id = self.request_manager.request.data.get('id')
        return PostModel.objects.get(id=post_id)
