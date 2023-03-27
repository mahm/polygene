# Polygene - Persona Generator

The Polygene Python library is designed to create fictional personas based on user-defined criteria. It allows users to generate a specific number of personas, which are then saved in a JSON file for easy access and storage. Furthermore, the library also supports displaying personas in a clear and organized tabular format, extracted from an existing JSON file containing the persona list.

## Usage

TODO: pip install support

### Generate Personas

To generate personas, use the following command:

```
poetry run polygene generate [num] --target [target] --condition [condition] --lang [lang] --output [output]
```

- `[num]`: (Required) The number of personas to generate.
- `[target]`: (Required) The target for generating personas.
- `[condition]`: (Required) The condition for generating personas.
- `[lang]`: (Optional) The language for generating personas (default: 'ja').
- `[output]`: (Optional) The name of the output JSON file (default: 'output.json').

Example:

```
poetry run polygene generate 3 --target 仮説検証のため --condition 日本人の男 性・女性を両方含む10代〜60代
```

### List Personas

To list personas from a JSON file, use the following command:

```
poetry run polygene list [filename]
```

- `[filename]`: (Required) The path to the JSON file containing the personas.

Example:

```
poetry run polygene list output.json
```

This command will display the personas in a tabular format, showing their Name, Age, Gender, Residence, and Occupation.

## License

This project is licensed under the MIT License.