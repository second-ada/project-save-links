from typing import Any, List
from flask import abort, request


class Validator:
    messages = {
        'required': "The '{}' field is required.",
        'not_empty': "'{}' field should not be empty.",
    }

    def __init__(self, raw_data: dict) -> None:
        self.data: dict = request.get_json(silent=True)
        if self.data is None:
            self.abort_with_error('No data provided.')

        self.keys = list(raw_data.keys())
        self.errors = []
        self.validations = {
            'required':
            lambda item: item in self.data,
            'not_empty':
            lambda item: self.data[item] is not None and len(self.data[item]) >
            0
        }

        rules = self.extract_rules(raw_data)
        self.apply_rules(rules)

    def abort_with_error(self, message: Any):
        abort(422, message)

    def apply_rules(self, rules: List[tuple]):
        for rule, field in rules:
            if not self.validations[rule](field):
                self.errors.append(self.messages[rule].format(field))

    def extract_rules(self, raw_rules: dict) -> List[tuple]:
        rules = []

        for key, value in raw_rules.items():
            splited = value.split('|')
            for item in splited:
                rules.append((item, key))

        return rules

    def send_errors(self):
        if self.errors:
            self.abort_with_error(self.errors)

    def check_errors(self):
        if self.has_errors:
            self.send_errors()

    @property
    def has_errors(self) -> bool:
        return len(self.errors) > 0
