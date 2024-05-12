def wspolczynniki(nodes_amount, node_nr):
    data = (
            ((1.5707963267948966192, -0.7071067811865475244), (1.5707963267948966192, 0.7071067811865475244)),
            ((1.0471975511965977462, -0.8660254037844386468), (1.0471975511965977462, 0.0000000000000000000), (1.0471975511965977462, 0.8660254037844386468)),
            ((0.7853981633974483096, -0.9238795325112867561), (0.7853981633974483096, -0.3826834323650897717), (0.7853981633974483096, 0.3826834323650897717), (0.7853981633974483096, 0.9238795325112867561)),
            ((0.6283185307179586477, -0.9510565162951535721), (0.6283185307179586477, -0.5877852522924731292), (0.6283185307179586477, 0.0000000000000000000), (0.6283185307179586477, 0.5877852522924731292), (0.6283185307179586477, 0.9510565162951535721))
            )
    return data[nodes_amount - 2][node_nr]