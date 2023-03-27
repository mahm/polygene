import ast
import json

from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

import polygene.templates as t


def _extract_json_and_convert_to_dict(input_string):
    stack = []
    start_pos = None

    for pos, char in enumerate(input_string):
        if char == '{':
            if not stack:
                start_pos = pos
            stack.append(char)
        elif char == '}':
            stack.pop()
            if not stack:
                json_string = input_string[start_pos:pos + 1]
                try:
                    json_data = json.loads(json_string)
                    return json_data
                except json.JSONDecodeError:
                    return None

    return None


def _call_llm(prompt):
    llm = ChatOpenAI(temperature=0.5)
    result = llm([HumanMessage(content=prompt)])
    return result.content


def _condition_prompt(condition):
    return t.condition_prompt().format(condition=condition)


def condition_generator(condition):
    condition_str = _call_llm(_condition_prompt(condition))
    conditions = ast.literal_eval(condition_str)
    return conditions


class Generator:
    def __init__(self, target, condition, lang='ja'):
        self.target = target
        self.condition = condition
        self.lang = lang

    async def generate(self):
        persona = _call_llm(self.persona_prompt())
        persona_json = _extract_json_and_convert_to_dict(persona)
        if persona_json is None:
            self.generate()
        else:
            return persona_json

    def persona_prompt(self):
        return t.persona_prompt().format(condition=self.condition, target=self.target, lang=self.lang)
