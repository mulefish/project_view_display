# Repulsion force
for i in range(len(self.nodes) - 1):
    for j in range(i+1, len(self.nodes)):
        delta = self.nodes[j].position - self.nodes[i].position
        if np.any(delta):
            distance_squared = np.sum(delta**2)
            distance = np.sqrt(distance_squared)
            force = self.repulsive_force_constant / distance_squared
            f = force * delta / distance
        else:
            f = np.random.rand(2)
        self.nodes[i].force -= f
        self.nodes[j].force += f

# Attraction force
for i in range(len(self.nodes)):
    for j in self.nodes[i].neighbors:
        if i < j:
            delta = self.nodes[j].position - self.nodes[i].position
            if np.any(delta):
                distance = np.sqrt(np.sum(delta**2))
                force = self.attraction_constant * distance
                f = force * delta / distance
                self.nodes[i].force += f
                self.nodes[j].force -= f


# Spring force
for i in range(len(self.nodes)):
    for j in self.nodes[i].neighbors:
        if i < j:
            delta = self.nodes[j].position - self.nodes[i].position
            if np.any(delta):
                distance = np.sqrt(np.sum(delta**2))
                force = self.spring_constant * \
                    (distance - self.spring_rest_length)
                f = force * delta / distance
                self.nodes[i].force += f
                self.nodes[j].force -= f


# Center force
for node in self.nodes:
    delta = self.center - node.position
    if np.any(delta):
        distance = np.sqrt(np.sum(delta**2))
        force = distance * self.center_constant
        f = force * delta / distance
        node.force += f

# Update positions
for node in self.nodes:
    delta = self.delta_t * node.force
    displacement_squared = np.sum(delta**2)
    if displacement_squared > self.max_displacement_squared:
        s = np.sqrt(self.max_displacement_squared / displacement_squared)
        delta *= s
    node.position += delta


class ForceNode:
    def __init__(self, position, obj, neighbors):
        self.position = position
        self.obj = obj
        self.neighbors = neighbors
        self.force = None


class ForceLayout:
    def __init__(self, nodes,
                 position_getter=itemgetter('position'),
                 position_setter=itemsetter('position'),
                 neighbor_getter=itemgetter('neighbors'),
                 center=(0, 0), spring_rest_length=40, repulsive_force_constant=6666,
                 spring_constant=2, delta_t=0.003, max_displacement_squared=20,
                 center_constant=0.6):
        self.spring_rest_length = spring_rest_length
        self.repulsive_force_constant = repulsive_force_constant
        self.spring_constant = spring_constant
        self.delta_t = delta_t
        self.max_displacement_squared = max_displacement_squared
        self.center_constant = center_constant

        self.position_getter = position_getter
        self.position_setter = position_setter
        self.center = np.array(center, dtype=float)

        self.nodes = [ForceNode(np.array(position_getter(x), dtype=float),
                                obj=x,
                                neighbors=neighbor_getter(x))
                      for x in nodes]

    def apply_forces(self):
        # Init forces
        for node in self.nodes:
            node.force = np.array([0.0, 0.0], dtype=float)
        ...

    def update(self):
        self.apply_forces()
        for node in self.nodes:
            self.position_setter(node.obj, node.position)
