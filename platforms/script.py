import os

file_names = [
    "netflix.md",
    "hulu.md",
    "amazon_prime.md",
    "disney.md",
    "hbomax.md",
    "apple_tv.md",
    "youtube.md",
    "peacock.md",
    "paramount.md",
    "espn.md",
    "crunchyroll.md",
    "twitch.md",
    "vudu.md",
    "tubi.md",
    "plutotv.md"
]

for file_name in file_names:
    with open(file_name, 'w') as file:
        # Удаляем плюсы и пробелы из названий файлов
        header_name = file_name.replace(".md", "").replace("+", "").replace(" ", "").capitalize()
        file.write("# " + header_name + "\n")

print("Файлы успешно созданы.")