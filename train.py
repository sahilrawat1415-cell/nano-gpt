import tiktoken

enc = tiktoken.get_encoding("gpt2")
tokens = enc.encode("hii there")

print(tokens)