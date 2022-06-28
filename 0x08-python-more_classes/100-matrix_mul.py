"""
Moule 100-matrix_mul
Contain method that does matrix multiplication
Requires the same size lits/rows of matrix
"""

def matrix_mul(m_a, m_b):
    """Returns multiplication of matrix"""
    message1 = "m_a should contain only integers or floats"
    message2 = "m_b should contain only integers or floats"
    list1 = []
    result = []
    calculation = 0
    if type(m_a) != list:
        raise TypeError("m_a must be a list")
    elif type(m_b) != list:
        raise TypeError("m_b must be a list")
    elif len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    elif len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    else:
        for i in range(len(m_a)):
            if type(m_a[i])!= list:
                raise TypeError("m_a must be a list of lists")
            if len(m_a[i]) == 0:
                raise ValueError("m_a can't be empty")
            elif len(m_a[i]) != len(m_a[0]):
                raise ValueError("each row of m_a must be of the same size")
            elif len(m_b[i]) == 0:
                raise ValueError("m_b can't be empty")
            for j in range(len(m_b[0])):
                for k in range(len(m_b)):
                    if type(m_b[k])!= list:
                        raise TypeError("m_b must be a list of lists")
                    elif len(m_b[k]) != len(m_b[0]):
                        raise ValueError("each row of m_b must be of the same size")
                    elif type(m_a[i][k]) != (int or float):
                        raise TypeError("m_a should contain only integers or floats")
                    elif type(m_b[k][j]) != (int or float):
                        aise TypeError("m_b should contain only integers or floats")
                    else:
                        try:
                            calculation += m_a[i][k] * m_b[k][j]
                            except:
                                raise ValueError ("m_a and m_b can't be multiplied")
                result.append(calculation)
                calculation = 0

            list1.append(result.copy())
            result.clear()
    return list1
