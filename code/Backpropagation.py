

def hidden_layer_backpropagate(layer, prev_outputs, outputs, next_weights_totlin, rate):
    tot_lin = []
    weights = []

    i = 0
    for (n, o) in zip(layer, outputs):
        op_lin = n.activation_d(o)
        
        total_op = 0
        for w, tl in zip(next_weights_totlin["w"], next_weights_totlin["tl"]):
            total_op = total_op +  tl * w[i]
            #print(str(tl) + " " + str(w[i]))
        
        grad = []
        for pl_o in prev_outputs:
            lin_w = pl_o
            g_w = total_op * op_lin * lin_w
            grad.append(g_w)
            #print(str(total_op) + " " + str(op_lin) + " " + str(lin_w))
        g_b = total_op * op_lin
        tot_lin.append(total_op * op_lin)
        weights.append(n.weights)
        n.adjust_weights(grad, rate)
        n.adjust_bias(g_b, rate)
        i = i + 1

    return {'w':weights, 'tl':tot_lin}

def output_layer_backpropagate(layer, outputs, targets, inputs, rate):
    tot_lin = []
    weights = []
    for (n, o, t) in zip(layer, outputs, targets):
        grad = []
        total_op = layer.loss_d(t, o)
        op_lin = n.activation_d(o)
        for inp in inputs:
            lin_w = inp
            g_w = total_op * op_lin * lin_w
            grad.append(g_w)
        g_b = total_op * op_lin
        #print(str(total_op) + " | " + str(op_lin))
        #print(total_op * op_lin)
        tot_lin.append(total_op * op_lin)
        weights.append(n.weights)
        n.adjust_weights(grad, rate)
        #print(grad)
        n.adjust_bias(g_b, rate)
    return {'w':weights, 'tl':tot_lin}