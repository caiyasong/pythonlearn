import zlib


class VirNode:
    def __init__(self):
        self.node = {}

    def crcencode(self, data):
        return zlib.crc32(str(data).encode())

    def add_node(self, server):
        for i in range(20):
            key = self.crcencode(f'{server}+{i}')
            self.node[key] = server

    def crcsort(self):
        return dict(sorted(self.node.items()))


    def printnode(self):
        print('全部节点:%s \n 长度为%d' % (self.crcsort(), len(self.crcsort())))

    def searchnode(self, data):
        data = self.crcencode(str(data).encode())

        sortnode = self.crcsort()

        for k, v in sortnode.items():
            if k > data:
                node = v
                break
        else:
            node = sortnode.get(min(sortnode))
        return data, node

node = VirNode()
node.add_node('a')
node.add_node('b')
node.add_node('c')
node.printnode()
data, node = node.searchnode(10000)
print(data, node)