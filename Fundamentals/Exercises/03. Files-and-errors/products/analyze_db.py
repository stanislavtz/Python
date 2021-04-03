def do_analyze(p_list):
    if len(p_list) == 0:
        return ['No products stocked']
    result = []
    for pr in list(sorted(p_list, key=lambda x: x['type'])):
        result.append(
            f"{pr['type']}, Product: {pr['name']}\nPrice: ${pr['price']:.2f}, Amount Left: {pr['quantity']}")
    return result