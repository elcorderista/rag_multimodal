import base64


def format_prompt_inputs(data, user_query):
    """
    Format the inputs for the promopt template by adding yser query and Base64-encoded data.
    :param data: dict: Dictionary contianing  URIS of images
    :param user_query: User's query text
    :return: dict: Dictionary containing the formatted inputs (user_query, image_data_1, image_data_2)
    """
    print("=== Formatting prompt inputs... ===")
    inputs = {}

    #Add user t o dictionary
    inputs['user_query'] = user_query

    image_path_1 = data["uris"][0][0]
    image_path_2 = data["uris"][0][1]

    with open(image_path_1, "rb") as image_file:
        image_data_1 = image_file.read()
        inputs['image_data_1'] = base64.b64encode(image_data_1).decode("utf-8")

    with open(image_path_2, "rb") as image_file:
        image_data_2 = image_file.read()
        inputs['image_data_2'] = base64.b64encode(image_data_2).decode("utf-8")

    print("==== Prompts inputs formatted ====")
    return inputs
