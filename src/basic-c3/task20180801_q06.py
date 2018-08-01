arasi = {
    "Aiba": 175,
    "Matsumoto": 172,
    "Ninomiya": 168,
    "Oono": 166,
    "Sakurai": 171
}

li = sorted(
    arasi.items(),
    key=lambda x: x[1],
)

for name, height in li:
    print(name, height)
