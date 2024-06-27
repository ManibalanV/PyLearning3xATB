#ENV_API_URLS = tuple("xyz.com/get", "xyz.com/post", "xyz.com/put")
ENV_API_URLS = tuple(["xyz.com/get", "xyz.com/post", "xyz.com/put"])

print(ENV_API_URLS) # TypeError: tuple expected at most 1 argument, got 3