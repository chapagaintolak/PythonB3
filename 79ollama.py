import ollama

deepseek = "deepseek-r1:1.5b"
llama = "llama3.2:1b"
# Load the Llama 3.2 model (replace "llama3.2" with the correct model name)
response = ollama.chat(model="deepseek-r1:1.5b", messages=[{"role": "user", "content": "Write essay on Computer."}])

# Print the response from the model
print(response['message']['content'])

