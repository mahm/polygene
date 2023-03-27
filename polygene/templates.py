from langchain.prompts.prompt import PromptTemplate


def persona_prompt():
    return PromptTemplate(
        input_variables=["condition", "target", "lang"],
        template=load_prompt("persona"),
    )


def condition_prompt():
    return PromptTemplate(
        input_variables=["condition"],
        template=load_prompt("condition"),
    )


def load_prompt(prompt_name):
    with open(f"./polygene/prompts/{prompt_name}.prompt", "r") as f:
        return f.read()
