from datetime import  date


def WriteLogFileForDataBase(error, additional_text: str = ""):
    with open("datafiles/log-file.txt", "a", encoding="utf-8") as file:
        file.write(f"{type(error)}: {error} {date.today()} & {additional_text}\n")

