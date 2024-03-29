from rest_framework.views import APIView
from api.decorators.add_security import access_protected
from api.shortcuts.data_get import process_and_get_response
from newspaper_app.classes.createNewspaperOperation import CreateNewspaperOperation
from newspaper_app.classes.deleteNewspaperOperation import DeleteNewspaperOperation
from newspaper_app.classes.getNewspaperOperation import GetNewspaperOperation
from newspaper_app.classes.updateNewspaperOperation import UpdateNewspaperOperation
from newspaper_app.models import NewspaperModel


@access_protected
class NewspaperView(APIView):
    def get(self, request):
        get_news_instance = GetNewspaperOperation(request=request, news_instance=NewspaperModel.objects.all())
        return process_and_get_response(get_news_instance)

    def post(self, request):
        create_news_instance = CreateNewspaperOperation(request=request)
        return process_and_get_response(create_news_instance)

    def put(self, request):
        update_news_instance = UpdateNewspaperOperation(request=request)
        return process_and_get_response(update_news_instance)

    def delete(self, request, id):
        delete_news_instance = DeleteNewspaperOperation(request=request, news_id=id)
        return process_and_get_response(delete_news_instance)
