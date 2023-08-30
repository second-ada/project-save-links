from typing import Any, Optional, Union
from flask import abort, request

# data = request.get_json(silent=True)
# if data is None:
#     abort(422, 'No data provided.')
# if 'category' not in data:
#     abort(422, 'Missing category.')
# if 'link' not in data:
#     abort(422, 'Missing link.')


class Validator:
    KEYS: list[str]
    RULES = ['required']
    DATA: Union[Any, None]

    def __init__(self, data: dict) -> None:
        self.DATA = request.get_json(silent=True)
        if self.DATA is None:
            abort(422, 'No data provided.')

        self.KEYS = list(data.keys())

        rules = self.extract_rules(data)
        for rule in rules:
            self.apply_rule(rule)

    def apply_rule(self, rule: str):
        if rule not in self.RULES:
            return False

    def extract_rules(self, rules: dict) -> list[str]:
        _rules = []

        for value in list(rules.values()):
            _rules.extend(value.split('|'))

        return _rules

    @property
    def data(self):
        print(self.KEYS)
        return {}
