import tkinter as tk
from analyzer import analyze_verb

def analyze():
    input_text = text_input.get("1.0", "end").strip()
    words = input_text.split()
    results = [analyze_verb(word) for word in words]
    output_text.delete("1.0", "end")
    for res in results:
        output_text.insert("end", f"{res}\n")

root = tk.Tk()
root.title("Text Analyzer")

tk.Label(root, text="Enter your text:").pack()
text_input = tk.Text(root, height=5, width=50)
text_input.pack()

tk.Button(root, text="Analyze", command=analyze).pack()
output_text = tk.Text(root, height=10, width=50)
output_text.pack()

root.mainloop()