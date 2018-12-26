import aiml

# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.learn("basic_chat.aiml")
# kernel.respond("load aiml b")

# Press CTRL-C to break this loop
while True:
    print("Enter your message >> ")
    print(kernel.respond(input()))