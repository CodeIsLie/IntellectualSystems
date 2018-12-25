import aiml

# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.learn("basic_chat.aiml")
kernel.respond("load aiml b")