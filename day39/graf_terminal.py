import plotext as plt

depth_ores = {
    "cyanite": 1250,
    "crystalline sulfur": 860,
    "quartz": 50
}
Minérios = list(depth_ores.keys())
Profundidade = list(depth_ores.values())

plt.title("Qantos metros de profundidade se encontra esses minérios")

plt.xlabel("Minérios")
plt.ylabel("Profundidade")

plt.bar(Minérios, Profundidade, label="Profundidade")

plt.show()