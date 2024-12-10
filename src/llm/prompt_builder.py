from langchain_core.prompts import ChatPromptTemplate


def get_bouquet_prompt():
    """
    Prompt template for a bouquet arrangement suggestions
    :return: Prompt template for a bouquet arrangement suggestions
    """
    return ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are a talented florist and you have been asked to create a bouquet of flowers for a special event. Answer the user's question  using the given image context with direct references to parts of the images provided."
                " Maintain a more conversational tone, don't make too many lists. Use markdown formatting for highlights, emphasis, and structure.",
            ),
            (
                "user",
                [
                    {
                        "type": "text",
                        "text": "what are some good ideas for a bouquet arrangement {user_query}",
                    },
                    {
                        "type": "image_url",
                        "image_url": "data:image/jpeg;base64,{image_data_1}",
                    },
                    {
                        "type": "image_url",
                        "image_url": "data:image/jpeg;base64,{image_data_2}",
                    },
                ],
            ),
        ]
    )


def get_event_theme_promt():
    """
    Promp template for suggestions themes for an event.
    :return: Promt template for suggestions themes for an event.
    """
    return ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are an event planner, and you have been asked to suggest themes for an event. "
                "Consider the user's preferences and the type of event they are organizing."
            ),
            (
                "user",
                {
                    "type": "text",
                    "text": "Suggest some themes for {event_type} with a focus on {preferences}.",
                },
            ),
        ]
    )


def get_flower_description_promt():
    """
    Prompt template for describing flowers in a image
    :return: Promt template for describing flowers in a image
    """

    return ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are a botanist and an expert in flowers. Describe the flowers in the image in detail, "
                "including their colors, patterns, and species if identifiable."
            ),
            (
                "user",
                {
                    "type": "image_url",
                    "image_url": "data:image/jpeg;base64,{image_data}",
                },
            ),
        ]
    )
