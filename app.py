import requests
import json
import gradio as gr

url = "http://localhost:11434/api/generate"

headers = {
    'Content-Type': 'application/json'
}

history =[]

def generate_response(prompt):
    history.append(prompt)
    final_prompt = "\n".join(history)
    
    data = {
        "model":"CodeWala",
        "prompt":final_prompt,
        "stream":False
    }

    response = requests.post(url,headers = headers, data=json.dumps(data))

    if response.status_code == 200:
        respone = response.text
        data = json.loads(respone)
        actual_respone = data['response']
        return actual_respone
    else:
        print("error:", respone.text)



## Frontend Part
interface = gr.Interface(
    fn = generate_response,
    inputs = gr.Textbox(lines=4,placeholder="Enter your prompt"),
    outputs = "text"
)
interface.launch()


