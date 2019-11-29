# # attr = [5,7,1,2,6,4,3,3,9,15,13]
# def maopao(attr):
#     for i in range(len(attr) - 1):
#         for j in range(len(attr) - i - 1):
#             if attr[j] > attr[j + 1]:
#                 attr[j], attr[j + 1] = attr[j + 1], attr[j]
#     return attr
#
#
# def xuanze(attr):
#     for i in range(len(attr)):
#         m = i
#         for j in range(i+1, len(attr)):
#             if attr[j] < attr[m]:
#                 m = j
#
#         attr[m], attr[i] = attr[i], attr[m]
#
#     return attr
#
#
#
# if __name__ == '__main__':
#     attr = [5, 7, 1, 2, 6, 4, 3, 3, 9, 15, 13]
#     print(xuanze(attr))


# class A():
#     _instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if cls._instance:
#             return cls._instance
#         else:
#             cls._instance = super().__new__(cls)
#             return cls._instance
#
#
# a = A()
# b = A()
#
# print(id(a))
# print(id(b))

#
# def sinde(cls):
#     _instance = None
#
#     def get_instance(*args, **kwargs):
#         nonlocal _instance
#         if _instance is None:
#             _instance = cls(*args, **kwargs)
#         return _instance
#     return get_instance
#
# @sinde
# class B:
#     pass
#
# a = B()
# b = B()
#
# print(a)
# print(b)

