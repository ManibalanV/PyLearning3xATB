# List files
import os
print(os.getcwd())
all_dir = os.listdir("C:/Users/manib/PycharmProjects/PyLearning3xATB/Ex02_July/Ex_05072024")
print(all_dir)


# Set an environment variable
os.environ["MY_VAR"] = "manibalan"
print(os.getenv("MY_VAR"))