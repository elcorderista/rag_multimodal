import chromadb
from chromadb.utils.embedding_functions import OpenCLIPEmbeddingFunction
from chromadb.utils.data_loaders import ImageLoader
from matplotlib import pyplot as plt
from settings.config import Config


# ==============================================================
# Create the Vector Multimodal Store
# ==============================================================
image_loader = ImageLoader()
chroma_client = chromadb.PersistentClient(Config.CHORMA_DB_PATH)
embedding_function = OpenCLIPEmbeddingFunction()

collection = chroma_client.get_or_create_collection(
    name=Config.CHROMA_COLLECTION_NAME,
    embedding_function=embedding_function,
    data_loader=image_loader
)

# ==============================================================
# Add Image to Database
# add() or update()
# ==============================================================
'''
collection.update(
    ids=['0','1'],
    uris=['./images/lion.jpg', './images/tiger.jpg'],
    metadatas=[{'category': 'animal'}, {'category': 'animal'}]
)
'''
collection.update(
    ids=[
        "E23",
        "E25",
        "E33",
    ],
    uris=[
        "./images/E23-2.jpg",
        './images/E25-2.jpg',
        './images/E33-2.jpg',
    ],
    metadatas=[
        {
            "item_id": "E23",
            "category": "food",
            "item_name": "Braised Fried Tofu with Greens",
        },
        {
            "item_id": "E25",
            "category": "food",
            "item_name": "Sauteed Assorted Vegetables",
        },
        {
            "item_id": "E33",
            "category": "food",
            "item_name": "Kung Pao Tofu",
        }
    ]
)
# ==============================================================
# Ask Database
# ==============================================================
print(collection.count())

# ==============================================================
# Print query results
#Print a dict {ids, disntances, data, ...}
#Each item in the dict is a 2d list.
# ==============================================================
def print_query_results(query_list: list, query_results: dict) -> None:
    result_count = len(query_results["ids"][0])

    #Iterate query list
    for i in range(len(query_list)):
        print(f"Results for query: {query_list[i]}")

        for j in range(result_count):
            id = query_results["ids"][i][j]
            distance = query_results["distances"][i][j]
            data = query_results["data"][i][j]
            document = query_results["documents"][i][j]
            metadata = query_results["metadatas"][i][j]
            uri = query_results["uris"][i][j]

            print(
                f"id: {id}, distance: {distance}, metadata: {metadata}, document: {document}"
            )

            #Display image, the physical file must exist at URI.
            #ImageLoader loads the image from file
            print(f'data: {uri}')
            plt.imshow(data)
            plt.axis('off')
            plt.show()

#Generate the query
query_texts = ['food with carrots and a tiger']

query_results = collection.query(
    query_texts=query_texts,
    n_results=4,
    include=["documents", "distances", "metadatas", "data", "uris"],
)

#Call the output function
print_query_results(query_texts, query_results)


