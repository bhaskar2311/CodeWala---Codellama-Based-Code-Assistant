# 👨‍🏫 CodeWala: CodeLlama-Based Code Teaching Assistant
CodeWala is a simple and effective code assistant that helps users generate code snippets in natural language — powered by CodeLlama via Ollama and wrapped in an interactive Gradio interface. Whether you're learning to code or just need quick syntax help, CodeWala responds intelligently with working code examples and contextual explanations.

## 📌 Features
* 💡 Accepts natural language prompts like “give me a Java code to perform binary search”
* 🤖 Powered by CodeLlama, running locally via the Ollama engine
* 💬 Maintains conversation context using basic prompt history
* ⚙️ API-based backend integrated with a Gradio front-end
* 🖥️ Lightweight, browser-based UI — no cloud calls or third-party LLMs

## 🧠 Technologies Used
* CodeLlama (via Ollama)
* Ollama – Local LLM runner and API server
* Gradio – UI framework for building ML/LLM interfaces
* Python (requests, json) – API integration and prompt handling

## 🗂 Project Structure
```
├── app.py           # Main application logic and Gradio UI
├── modelfile        # Model registration/config for Ollama
├── requirements.txt # List of Python dependencies
└── Output.png       # UI screenshot
```

⚙️ Setup Instructions
1. Install Ollama
You need to install Ollama first:
* For Windows just download OllamaSetup.exe from the Ollama Website (https://ollama.com/download/windows) and then follow step two.
```
# On macOS (via Homebrew)
brew install ollama

# On Ubuntu
curl -fsSL https://ollama.com/install.sh | sh
```
🔁 Restart terminal after installation if needed.


2. Pull the CodeLlama Model
```
ollama pull codellama
```
You can customize or rename the model as CodeWala using a modelfile.

3. Clone the Repository
```
git clone https://github.com/bhaskar2311/CodeWala---Codellama-Based-Code-Assistant
cd CodeWala---Codellama-Based-Code-Assistant
```
4. Install Python Dependencies
```
pip install -r requirements.txt
```
5. Run the App
Make sure Ollama is running in the background:
```
ollama run CodeWala
```
Then in a separate terminal, run:
```
python app.py
```
The app will launch in your browser at http://127.0.0.1:7860

## 💡 Example Prompt
Prompt: give me a java code to perform binary search
Response:
```Java
public static int binarySearch(int[] arr, int target) {
    int low = 0, high = arr.length - 1;
    while (low <= high) {
        int mid = (low + high) / 2;
        if (arr[mid] == target) return mid;
        else if (target < arr[mid]) high = mid - 1;
        else low = mid + 1;
    }
    return -1;
}
```
## 📸 Screenshot
![Output](https://github.com/user-attachments/assets/aa932579-1e2a-4d46-891f-ff6b1c39fbe4)

## 📝 Notes
This project was fully developed by me. The README was written based on my knowledge and experience, with support from generative AI tools to refine its structure and presentation.

## 📄 License
This project is open source and available under the MIT License.

## 🙋‍♂️ Author
Made with ❤️ by Bhaskar Shivaji Kumbhar

