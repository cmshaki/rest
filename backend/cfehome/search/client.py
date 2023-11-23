from algoliasearch_django import algolia_engine


def get_client():
    return algolia_engine.client


# def get_index(index_name="cfe_Product"):
#     client = get_client()
#     index = client.init_index(index_name)
#     return index


def perform_search(query, **kwargs):
    client = get_client()
    params = {}
    tags = ""
    if "tags" in kwargs:
        tags = kwargs.pop("tags") or []
        if len(tags) != 0:
            params["tagFilters"] = tags
    index_filters = [f"{k}:{v}" for k, v in kwargs.items() if v]
    if index_filters != 0:
        params["facetFilters"] = index_filters
    queries = [
        {"indexName": "cfe_Product", "query": query, "params": params},
        {"indexName": "cfe_Article", "query": query, "params": params},
    ]
    results = client.multiple_queries(queries)
    return results
