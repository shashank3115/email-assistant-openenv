def grade(pred, actual):
    if pred == actual:
        return 1.0
    elif pred in actual:
        return 0.5
    else:
        return 0.0