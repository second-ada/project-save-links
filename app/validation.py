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
    keys: list[str]
    data: Union[Any, None]
    rules = ['required']
    errors = []

    def __init__(self, raw_data: dict) -> None:
        self.data = request.get_json(silent=True)
        if self.data is None:
            abort(422, 'No data provided.')

        self.keys = list(raw_data.keys())

        rules = self.extract_rules(raw_data)
        for rule, field in rules:
            self.apply_rule(rule, field)

    def apply_rule(self, rule: str, field: str):
        if rule == 'required':
            self.errors.append(f'Field "{field}" is required')

    def extract_rules(self, rules: dict) -> list[str]:
        _rules = []

        for value in list(rules.values()):
            _rules.extend(value.split('|'))

        return _rules

    @property
    def has_errors(self):
        return len(self.errors) > 0
