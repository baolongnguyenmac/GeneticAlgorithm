import random
from codecs import decode
import struct

# def float_to_bin(num):
#     return format(struct.unpack('!I', struct.pack('!f', num))[0], '032b')

# def bin_to_float(binary):
#     return struct.unpack('!f',struct.pack('!I', int(binary, 2)))[0]

def bin_to_float(b):
    """ Convert binary string to a float. """
    bf = int_to_bytes(int(b, 2), 8)  # 8 bytes needed for IEEE 754 binary64.
    return struct.unpack('>d', bf)[0]


def int_to_bytes(n, length):  # Helper function
    """ Int/long to byte string.

        Python 3.2+ has a built-in int.to_bytes() method that could be used
        instead, but the following works in earlier versions including 2.x.
    """
    return decode('%%0%dx' % (length << 1) % n, 'hex')[-length:]


def float_to_bin(value):  # For testing.
    """ Convert float to 64-bit binary string. """
    [d] = struct.unpack(">Q", struct.pack(">d", value))
    return '{:064b}'.format(d)


class Node:
    """
    Node dùng để lưu trữ giá trị nghiệm vừa random ra được
    fitness là giá trị được tính từ hàm getFitness của class Genetic
    """
    
    def __init__(self, data, fitness = 1000):
        self.data = data
        self.fitness = fitness

class Genetic:
    def __init__(self, a = 0, b = 0, c = 0):
        self.array = []
        # self.length = random.randint(0, 10)
        # self.length = random.randint(200, 300)
        
        # số lượng quần để mặc định là 200
        self.length = 200
        
        # khoảng nghiệm được random trong khoảng [0, 10]
        self.boundary = random.uniform(0, 10)
        # self.boundary = 10000
        self.a = a
        self.b = b
        self.c = c
        
        # tính đỉnh của parabol 
        self.x0 = 0 # x0 = -b/2a

    def push(self, item):
        """
        đẩy node (chứa giá trị nghiệm và fitness) vào quần thể trước đó 
        sắp xếp quần thể theo thứ tự giảm dần fitness 
        """
        for i in range(len(self.array)):
            if self.array[i].fitness > item.fitness:
                self.array.insert(i, item)
                return
        self.array.append(item)

    def run(self, a, b, c):
        """
        chạy thuật toán tìm nghiệm 
        """
        print(self.boundary)
        self.a = a
        self.b = b
        self.c = c

        self.x0 = -b / (2 * a)
        for i in range(self.length):
            x = random.uniform(self.x0 - self.boundary, self.x0 + self.boundary)
            self.push(Node(x, self.getFitness(x)))

        # count dùng để đếm số vòng while. không có gì đáng quan tâm lắm :> 
        count = 0
        while not self.array[0].fitness < 0.0001:
            count += 1
            
            # loại 1/2 số lượng cá thể trong quần thể. giữ lại 1/2 những cá thể tốt nhất  
            self.pop()
            
            self.mate()
            print(self.array[0].data)

        print(self.array[0].data)
        print(count)

    def mate(self):
        """
        tiến hành lai ghép ngẫu nhiên giữa các cá thể của 1 quần thể sau chọn lọc 
        """
        while len(self.array) < self.length:
            index1 = random.randint(0, len(self.array) - 1)
            index2 = random.randint(0, len(self.array) - 1)
            while index1 == index2 or self.array[index1].data == self.array[index2].data:
                index2 = random.randint(0, len(self.array) - 1)

            bin1 = float_to_bin(self.array[index1].data)
            bin2 = float_to_bin(self.array[index2].data)

            x1, x2 = self.getCrossover(bin1, bin2)
            if not (self.x0 - self.boundary <= x1 <= self.x0 + self.boundary) or not (self.x0 - self.boundary <= x2 <= self.x0 + self.boundary):
                continue
            f1 = self.getFitness(x1)
            f2 = self.getFitness(x2)
            if f1 < self.array[len(self.array) - 1].fitness or f2 < self.array[len(self.array) - 1].fitness:
                # self.array.pop()
                if f1 < f2:
                    self.push(Node(x1, f1))
                elif f1 > f2:
                    self.push(Node(x2, f2))
                else:
                    self.push(Node(x1, f1))
                    self.push(Node(x2, f2))

    def getCrossover(self, bin1, bin2):
        """
        ramdom ngẫu nhiên 1 vị trí trong dãy bit rồi trao đổi chéo nội dung 2 dãy bit tại vị trí đó 
        trả về 2 số thực sau khi đã trao đổi chéo 
        """
        crossover = random.randint(0, len(bin1))
        while (crossover) == 0:
            crossover = random.randint(0, len(bin1))
        bin11 = bin1[0:crossover] + bin2[crossover:]
        bin21 = bin2[0:crossover] + bin1[crossover:]
        return bin_to_float(bin11), bin_to_float(bin21)

    # không dùng 
    def addMaxFitnessItem(self, item):
        for i in range((self.length - 4) // 3):
            self.array.insert(0, item)

    # không dùng 
    def getMaxFitnessItem(self):
        return self.array[0]

    def pop(self):
        """
        loại bỏ 1 nửa số cá thể trong quần thể
        những cá thể bị loại bỏ là những cá thể có giá trị fitness cao (lower = better)
        """
        while len(self.array) > self.length // 2:
            self.array.pop()

    def getFitness(self, x):
        return abs(self.a * x**2 + self.b * x + self.c)

def main():
    g = Genetic()
    # g.run(1,-7,12)

    a = random.uniform(-10, 10)
    b = random.uniform(-10, 10)
    c = random.uniform(-10, 10)
    print(a, ' ', b, ' ', c)
    g.run(a,b,c)

if __name__ == '__main__':
    main()
