



# class Context(object):
#     def __init__(self, display_name, parent=None, parent_entry_pos=None):
#         self.display_name = display_name
#         self.parent = parent
#         self.parent_entry_pos = parent_entry_pos
#         self.key_table = None




class Interpreter(object):
    def visit(self, node):
        """
        递归下降法： 遍历ast node
        :param node: 起始节点
        :param context: 上下文定位错误
        :return:
        """

        method_name = f"visit_{type(node).__name__}"
        method = getattr(self, method_name, self.no_visit_method)
        return method(node)

    def no_visit_method(self, node):
        raise Exception(f"No visit_{type(node).__name__}")

    def visit_KvsNode(self, node):

        res = dict()

        elements = node.element_nodes

        for ele in elements:
            key, val = self.visit_PairNode(ele)
            res[key.value[1:-1]] = val

        return res


    def visit_PairNode(self, node):
        key = node.key
        value_node = node.value_node
        # print(type(value_node))
        value = self.visit_ValNode(value_node)

        return key, value

    def visit_ValNode(self, node):
        node = node.node
        method_name = f"visit_{type(node).__name__}"
        # print(method_name)
        method = getattr(self, method_name, self.no_visit_method)
        return method(node)

    def visit_AtomNode(self, node):
        value = node.tok.value
        if type(value)==str:
            value = value[1:-1]
        return value


    def visit_ListNode(self, node):

        res = list()

        elements = node.element_nodes

        for ele in elements:
            val = self.visit_ValNode(ele)
            res.append(val)

        return res

