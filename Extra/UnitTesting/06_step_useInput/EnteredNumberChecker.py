class EnteredNumberChecker:

    def GetNumberFromInput(self) -> int:
        text: str = input("Give me a number: ")
        if text.isnumeric():
            return int(text)
        raise Exception(f"The text you entered '{text}' is not a number")
