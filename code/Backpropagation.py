

def output_layer_grads(layer, outputs, targets, prev_layer, rate):
    grads = []
    for (n, o, t) in zip(layer, outputs, targets):
        grad = []
        total_op = layer.loss_d(t, o)
        op_lin = n.activation_d(o)
        for pln in prev_layer.neurons:
            lin_w = pln.last_output
            g = total_op * op_lin * lin_w
            grad.append(g)
        grads.append(grad)
        n.adjust_weights(grad, rate)
    return grads

def single_layer_grads(layer, outputs, targets, inputs, rate):
    grads = []
    for (n, o, t) in zip(layer, outputs, targets):
        grad = []
        total_op = layer.loss_d(t, o)
        op_lin = n.activation_d(o)
        for inp in inputs:
            lin_w = inp
            g = total_op * op_lin * lin_w
            grad.append(g)
        grads.append(grad)
        n.adjust_weights(grad, rate)
    return grads