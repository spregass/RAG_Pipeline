import ollama

print("🍝 BellaVista Italian Restaurant Assistant")
print("Type 'exit' to quit.\n")

# Chat history
messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant specialized in providing information about BellaVista Italian Restaurant."
    }
]

while True:
    prompt = input("You: ")

    if prompt.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    # Add user message
    messages.append({"role": "user", "content": prompt})

    print("Assistant: Thinking...\n")

    # Call Ollama
    response = ollama.chat(
        model="llama3.1:latest",
        messages=messages
    )

    reply = response["message"]["content"]

    # Print reply
    print("Assistant:", reply, "\n")

    # Save response
    messages.append({"role": "assistant", "content": reply})