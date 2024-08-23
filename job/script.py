import os

file_names = [
    "linkedin.md",
    "indeed.md",
    "glassdoor.md",
    "monster.md",
    "careerbuilder.md",
    "simplyhired.md",
    "ziprecruiter.md",
    "snagajob.md",
    "jooble.md",
    "flexjobs.md",
    "angellist.md",
    "dice.md",
    "stack_overflow_jobs.md",
    "upwork.md",
    "freelancer.md"
]

for file_name in file_names:
    with open(file_name, 'w') as file:
        # Заменяем пробелы на нижние подчеркивания для корректного отображения в заголовке
        header_name = file_name.replace(".md", "").replace(" ", "_").capitalize()
        file.write("# " + header_name + "\n")

print("Файлы успешно созданы.")