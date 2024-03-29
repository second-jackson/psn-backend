from abc import ABC
from auth_app.models import User
from api.classes.model_operations import ModelOperations, SearchModel
from api.classes.type_alias.operations import Operations
from api.classes.controller_logic_excecutor import ControllerLogicExecutor


class UserOperations(Operations, ABC):
    def __init__(self, request, model_id=None, model_instance=None):
        ControllerLogicExecutor.__init__(self, request=request)
        ModelOperations.__init__(self, search_model=SearchModel(model_id=model_id, model_class=User),
                                 model_instance=model_instance)

    def only(self) -> str:
        return self.request_manager.request.query_params.get('only', '')
