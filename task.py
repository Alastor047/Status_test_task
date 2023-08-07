class TreeStore:
    """
    Класс, представляющий структуру дерева, используя массив объектов с полями id и parent.
    Предоставляет методы для эффективного доступа и управления деревом.
    """

    def __init__(self, items):
        """
        Инициализирует TreeStore с массивом элементов.
        Параметры:
        - items (list): Список словарей, представляющих элементы с полями id и parent.
        """
        self.dict_by_id = {}          # Словарь для хранения элементов по их ID (id: item)
        self.child_dict_by_parent = {}  # Словарь для хранения дочерних элементов по родительскому ID (parent_id: [items])

        for item in items:
            item_id = item["id"]
            parent_id = item["parent"]
          
            # Сохраняем элемент в словаре по его ID
            self.dict_by_id[item_id] = item

            # Добавляем элемент в список дочерних элементов его родителя
            self.child_dict_by_parent.setdefault(parent_id, []).append(item)

    def getAll(self):
        """
        Получить все элементы в TreeStore.
        Возвращает:
        - list: Список, содержащий все элементы в TreeStore.
        """
        return list(self.dict_by_id.values())

    def getItem(self, item_id):
        """
        Получить элемент с указанным item_id.
        Параметры:
        - item_id (int): ID элемента для получения.
        Возвращает:
        - dict or None: Элемент, если найден, в противном случае None.
        """
        return self.dict_by_id.get(item_id)

    def getChildren(self, parent_id):
        """
        Получить дочерние элементы элемента с указанным parent_id.
        Параметры:
        - parent_id (int): ID родительского элемента.
        Возвращает:
        - list: Список, содержащий дочерние элементы родительского элемента.

        """
        return self.child_dict_by_parent.get(parent_id, [])

    def getAllParents(self, item_id):
        """
        Получить путь элемента к корню дерева.
        Параметры:
        - item_id (int): ID элемента.
        Возвращает:
        - list: Список, содержащий цепочку родительских элементов от элемента до корня дерева.

        """
        parents = []
        while item_id is not None:
            parent = self.getItem(item_id)
            if not parent:
                break
            parents.append(parent)
            item_id = parent["parent"]
        return parents[::-1]  # Обратный порядок списка для получения пути от элемента к корню
