with open("data.txt", "r") as f:
    data = f.read()

# if ("donkey" in data):
#     with open("data.txt", "w") as f:
#         f.write(data.replace("donkey", "####"))
# else:
#     print("There is no donkey in data.txt")

with open("this.txt", "r") as f:
    this = f.read()

if (data == this):
    print("Both files are same")
else:
    print("Both files are unique")