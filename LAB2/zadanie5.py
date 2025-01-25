import ast

class DynamicCodeGenerator:
    def __init__(self, template):
   
        self.template = template
        self.code = ""

    def fill_template(self, **kwargs):

        self.code = self.template.format(**kwargs)

    def validate_code(self):

        try:
            ast.parse(self.code)
            return True
        except SyntaxError as e:
            print(f"Błąd składni: {e}")
            return False

    def execute_code(self, globals_dict=None, locals_dict=None):

        if self.validate_code():
            try:
                exec(self.code, globals_dict, locals_dict)
            except Exception as e:
                print(f"Błąd wykonania: {e}")
        else:
            print("Kod nie przeszedł walidacji i nie zostanie wykonany.")

# Przykład użycia:
template_code =

generator = DynamicCodeGenerator(template_code)
generator.fill_template(wartosc=2)

print("Wygenerowany kod:")
print(generator.code)

generator.execute_code()

# Sprawdzamy czy funkcja została zdefiniowana i możemy ją wywołać
if "funkcja" in globals():
    print(f"Wywołanie funkcji: {globals()o zwrócić 7
