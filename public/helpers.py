def to_dict(input_array):
    output = []
    for element in input_array:
        dict_element = element.__dict__
        del dict_element["_sa_instance_state"]
        output.append(dict_element)
    return output
