def ford_bellman():
    import sys

    # Ввод графа
    print("Введите количество вершин и рёбер (через пробел):")
    n, m = map(int, input().split())  # n — количество вершин, m — количество рёбер

    edges = []
    indexedPeaks = {}
    peaksIndexed = {}

    print("Введите рёбра в формате 'начало конец вес':")
    vertex_count = 0
    for _ in range(m):
        startCoord, endCoord, weight = input().split()
        weight = int(weight)

        # Добавляем вершины в словари, если их ещё нет

        if startCoord not in indexedPeaks:
            indexedPeaks[startCoord] = vertex_count
            peaksIndexed[vertex_count] = startCoord
            vertex_count += 1

        if endCoord not in indexedPeaks:
            indexedPeaks[endCoord] = vertex_count
            peaksIndexed[vertex_count] = endCoord
            vertex_count += 1

        # Добавляем ребро
        edges.append((indexedPeaks[startCoord], indexedPeaks[endCoord], weight))

    print("Введите стартовую вершину:")
    start = input()

    # Проверяем, что стартовая вершина есть в графе
    if start not in indexedPeaks:
        print("Ошибка: указанная стартовая вершина отсутствует в графе.")
        return

    start_index = indexedPeaks[start]

    # Инициализация расстояний
    INFINITY = sys.maxsize
    distances = [INFINITY] * len(indexedPeaks)
    distances[start_index] = 0

    # Основной алгоритм
    for _ in range(len(indexedPeaks) - 1):  # Итерации для релаксации рёбер
        for startCoord, endCoord, weight in edges:
            if distances[startCoord] != INFINITY and distances[startCoord] + weight < distances[endCoord]:
                distances[endCoord] = distances[startCoord] + weight

    # Проверка на наличие отрицательных циклов
    for startCoord, endCoord, weight in edges:
        if distances[startCoord] != INFINITY and distances[startCoord] + weight < distances[endCoord]:
            print("Обнаружен отрицательный цикл.")
            return

    # Вывод результатов
    print("Кратчайшие расстояния от вершины", start, ":")
    # Создаём словарь с названиями вершин и их расстояниями
    result = {peaksIndexed[i]: distances[i] for i in range(len(indexedPeaks))}

    # Проверяем, являются ли вершины числами или строками
    def parse_key(key):
        try:
            return int(key)  # Преобразуем в число, если возможно
        except ValueError:
            return key  # Иначе оставляем строкой

    # Сортируем вершины с учётом числовых значений
    for vertex in sorted(result, key=parse_key):
        distance = result[vertex]
        if distance == INFINITY:
            print(f"Вершина {vertex}: недостижима")
        else:
            print(f"Вершина {vertex}: {distance}")


# Запуск программы
if __name__ == "__main__":
    ford_bellman()
