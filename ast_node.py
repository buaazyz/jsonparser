class AtomNode(object):
    def __init__(self, tok):
        self.tok = tok

        self.pos_begin = self.tok.pos_begin
        self.pos_end = self.tok.pos_end

    def __repr__(self):
        return f'{self.tok}'



class ValNode(object):
    def __init__(self, node, pos_begin, pos_end):
        self.node = node
        self.pos_begin = pos_begin
        self.pos_end = pos_end

    def __repr__(self):
        return f'{self.node}'



class PairNode(object):
    def __init__(self, key, value_node, pos_begin, pos_end):
        self.key = key
        self.value_node = value_node

        self.pos_begin = self.key.pos_begin
        self.pos_end = self.value_node.pos_end

    def __repr__(self):
        return f'(KEY:{self.key} VALUE:{self.value_node})'



class ListNode(object):
    def __init__(self, element_nodes, pos_begin, pos_end):
        self.element_nodes = element_nodes
        self.pos_begin = pos_begin
        self.pos_end = pos_end

    def __repr__(self):
        return f'[ {self.element_nodes} ]'



class KvsNode(object):
    def __init__(self, element_nodes, pos_begin, pos_end):
        self.element_nodes = element_nodes
        self.pos_begin = pos_begin
        self.pos_end = pos_end

    def __repr__(self):
        return f'( {self.element_nodes} )'



