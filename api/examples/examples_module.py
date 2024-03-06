from api.examples.examples_service import ExamplesService
from api.examples.examples_controller import ExamplesController


class ExamplesModule:

    def __init__(self):
        self.providers = [ExamplesService]
        self.controllers = [ExamplesController]



