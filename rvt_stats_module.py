def get_mean(numb):
    return sum(numb) / len(numb)
def get_variance(numb):
    mean = get_mean(numb)
    return sum ([(x - mean) ** 2 for x in numb]) / len(numb)
def get_std_dev(numb):
    return get_variance(numb) ** 0.5
def get_std_error(numb):
    return get_std_dev(numb)/(len(numb)**0.5)
def get_z_score(obs, numb):
    mean = get_mean(numb)
    std_dev = get_std_dev(numb)
    return (obs - mean) / std_dev