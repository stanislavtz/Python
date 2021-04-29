class Neighborhood:
    def __init__(self, name, blocks_list):
        self.__blocks = []
        self.name = name
        self.blocks_list = self.__set_blocks(blocks_list)

    def update_blocks(self, blocks_list):
        self.blocks_list = self.__set_blocks(blocks_list)

    def __set_blocks(self, blocks_list):
        for block in blocks_list:
            if not block.number in list(map(lambda b: b.number, self.__blocks)):
                self.__blocks.append(block)

        return sorted(self.__blocks, key=lambda b: int(b.number))

    def __str__(self):
        result = [f"Neighborhood: {self.name}"]
        [result.append(
            f"* Block number: {bl.number} -> {bl.apartments_count} apartments for sale. Price for one: {bl.price}") for bl in self.blocks_list]
        return '\n'.join(result)


class Block:
    def __init__(self, number, apartments_count=0, price=None):
        self.number = number
        self.apartments_count = apartments_count
        self.price = price


def collect_appartments(data, collection):
    neighborhood_name = data.split(' -> ')[0]
    blocks = list(map(lambda bl: Block(bl), data.split(' -> ')[1].split(',')))

    mapped = list(map(lambda n: n.name, collection))
    if not neighborhood_name in mapped:
        neighborhood = Neighborhood(neighborhood_name, blocks)
        collection.append(neighborhood)
    else:
        neighborhood = list(filter(lambda n: n.name == neighborhood_name, collection))[0]
        neighborhood.update_blocks(blocks)

    return collection


def set_appartments_for_sale(data, collection):
    neighborhood_name, block_number = data.split(' -> ')[0].split('&')
    count_of_available_apartments, price_for_one_apartment = list(map(int, data.split(' -> ')[1].split('|')))

    if not neighborhood_name in list(map(lambda n: n.name, collection)):
        return collection

    neighborhood = list(filter(lambda n: n.name == neighborhood_name, collection))[0]
    if not block_number in list(map(lambda bl: bl.number, neighborhood.blocks_list)):
        return collection

    for block in neighborhood.blocks_list:
        if block.number == block_number:
            block.apartments_count = count_of_available_apartments
            block.price = price_for_one_apartment

    return collection

collection = []
data = input()
while data != 'collectApartments':
    collection = collect_appartments(data, collection)
    data = input()

data = input()
while data != 'report':
    collection = set_appartments_for_sale(data, collection)
    data = input()


sorted_neighborhoods = sorted(collection, key=lambda n: n.name)

for n in sorted_neighborhoods:
    print(n)