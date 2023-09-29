def linear_search_product(product_list, target_product):
    indices = []

    for i, product in enumerate(product_list):
        if product == target_product:
            indices.append(i)

    return indices

# Example usage:
products = ["Apple", "Banana", "Orange", "Apple", "Grapes"]
target_product = "Apple"
result = linear_search_product(products, target_product)

if result:
    print(f"The target product '{target_product}' was found at indices: {result}")
else:
    print(f"The target product '{target_product}' was not found in the list.")
