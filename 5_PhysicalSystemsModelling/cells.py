
dt = 0.01


def create_cell(transfer_a = 1, temp = 0, capacity = 1, neighbours = None, mode = None):
    if mode is None:
        self = Cell(transfer_a, temp, capacity, neighbours)
    elif mode.lower() == 'empty':
        self = EmptyCell()
    elif mode.lower() == 'const':
        self = ConstCell(transfer_a, temp, capacity, neighbours)
    else:
        raise ValueError(f'WTF&&!!&& What is {mode} cell?')
    return self


class CellBody:
    def __init__(self, SPACEW, SPACEH, space):
        self.space = space
        self.SPACEW = SPACEW
        self.SPACEH = SPACEH

    def update(self):
        for row in self.space:
            for cell in row:
                cell.compile()
        for row in self.space:
            for cell in row:
                cell.update()


class Cell:
    def __init__(self, transfer_a=1, temp=0, capacity=1, neighbours=None):
        self.temp = temp
        self.transfer_a = transfer_a
        self.capacity = capacity
        if neighbours is None:
            self.neighbours = []
        self.neighbours = neighbours
        self.delta_temp = 0

    def compile(self):
        N = sum([(self.transfer_a + neighbour.transfer_a) * (neighbour.temp - self.temp)
                 for neighbour in self.neighbours])
        self.delta_temp = N * dt / self.capacity

    def update(self):
        self.temp += self.delta_temp


class EmptyCell(Cell):
    def update(self):
        pass


class ConstCell(Cell):
    def __init__(self, transfer_a=1, temp=0, capacity=1, neighbours=None):
        super().__init__(transfer_a, temp, capacity, neighbours)
        self.N_data = []
        # self.Q =

    def update(self):
        self.N_data.append(sum([(self.transfer_a + neighbour.transfer_a) * (neighbour.temp - self.temp)
                                for neighbour in self.neighbours]))
