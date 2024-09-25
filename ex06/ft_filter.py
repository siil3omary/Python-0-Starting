# def ft_filter1(function, iter):
#     """
#     ft_filter(function, iter) -> list
#     purpose: filter elements of an iterable
#     function: function to filter the elements
#     iter: iterable to filter
#     return: list of elements that passed the filter
#     """
#     returned_list = []
#     if function is None:
#         for i in iter:
#             if i:
#                 returned_list.append(i)
#     else:
#         for i in iter:
#             if function(i):
#                 returned_list.append(i)
#     return returned_list


def ft_filter(function, iter):
    """
    ft_filter(function, iter) -> list
    purpose: filter elements of an iterable
    function: function to filter the elements
    iter: iterable to filter
    return: list of elements that passed the filter
    """
    return [item for item in iter if (function(item) if function else item)]
