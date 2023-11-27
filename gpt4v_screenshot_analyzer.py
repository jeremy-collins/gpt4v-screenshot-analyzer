#!/usr/bin/env python3

import subprocess
import base64
import requests
import threading
import keyboard
import time
import tkinter as tk
from PIL import Image, ImageTk

# OpenAI API Key
api_key = "your-api-key-here"

# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Function to send image or follow-up message to GPT-4 Vision API and get the description
def get_image_description(base64_image, followup_message=None):
    print("Sending request to GPT-4 Vision API...")
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    payload = {
        "model": "gpt-4-vision-preview",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "What’s in this image?"
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}",
                            "detail": "high"
                        }
                    }
                ]
            }
        ],
        "max_tokens": 1000
    }

    if followup_message is not None:
        payload["messages"] += followup_message

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    return response.json()

# Global variables for mouse and rectangle
start_x, start_y, end_x, end_y = 0, 0, 0, 0
rect_id = None
selection_window = None

# Update the on_click function to only capture coordinates
def on_click(x, y, button, pressed):
    global start_x, start_y, end_x, end_y
    if pressed:
        start_x, start_y = x, y
    else:
        end_x, end_y = x, y
        return False  # Stop listener

def display_result(image_path, text):
    def run_window():
        root = tk.Tk()
        root.title("GPT-4V Output")

        window_x = start_x
        window_y = start_y

        # Display image
        img = Image.open(image_path)
        imgtk = ImageTk.PhotoImage(image=img)
        img_label = tk.Label(root, image=imgtk)
        img_label.image = imgtk
        img_label.pack()

        # Scrollable Text Widget for displaying text
        text_frame = tk.Frame(root)
        text_widget = tk.Text(text_frame, wrap='word', height=10)
        scrollbar = tk.Scrollbar(text_frame, command=text_widget.yview)
        text_widget.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        text_frame.pack(fill=tk.BOTH, expand=True)

        # Update text widget with API response
        text_widget.insert(tk.END, text)
        text_widget.config(state='disabled')  # Make the text widget read-only

        # Text variable to hold the conversation history for follow-up questions
        conversation_text = text

        # Text Entry for follow-up questions
        entry_frame = tk.Frame(root)
        entry_var = tk.StringVar()
        entry_widget = tk.Entry(entry_frame, textvariable=entry_var, width=50)
        entry_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        entry_frame.pack(fill=tk.BOTH)

        # Button to send follow-up questions
        def send_followup(event=None):
            nonlocal conversation_text
            followup_text = entry_var.get()
            if followup_text.strip() == '':
                return  # Do nothing if text is empty

            followup_message = [
                {
                    "role": "assistant",
                    "content": conversation_text
                },
                {
                    "role": "user",
                    "content": followup_text
                }
            ]

            base64_image = encode_image(image_path)
            response = get_image_description(base64_image, followup_message)
            entry_var.set('')  # Clear the entry widget

            # Append the follow-up response to the text widget
            text_widget.config(state='normal')
            new_response_text = response['choices'][0]['message']['content']  # The received response
            conversation_text += "\n\n" + new_response_text  # Update the conversation history
            text_widget.insert(tk.END, "\n\n" + new_response_text)
            text_widget.config(state='disabled')  # Make the text widget read-only

        entry_widget.bind("<Return>", send_followup)
        send_button = tk.Button(entry_frame, text="Send", command=send_followup)
        send_button.pack(side=tk.RIGHT)

        root.geometry(f'+{window_x}+{window_y}')

        root.mainloop()

    window_thread = threading.Thread(target=run_window)
    window_thread.start()

# Updated function to take a screenshot with coordinates
def take_screenshot():
    global start_x, start_y, end_x, end_y
    screenshot_path = "screenshot.png"

    subprocess.run(["gnome-screenshot", "-f", screenshot_path, "-a", 
                    f"{start_x},{start_y},{end_x - start_x},{end_y - start_y}"])
    print("Screenshot taken!")
    time.sleep(1)
    base64_image = encode_image(screenshot_path)
    description = get_image_description(base64_image)
    display_result(screenshot_path, description['choices'][0]['message']['content'])

# Hotkey function
def hotkey_function():
    print("Hotkey pressed! Drag to select screenshot area...")
    take_screenshot()

# Hotkey listener thread
def hotkey_listener():
    while True:
        keyboard.wait('ctrl+alt+s')
        hotkey_function()

# Main function
if __name__ == "__main__":
    listener_thread = threading.Thread(target=hotkey_listener, daemon=True)
    listener_thread.start()

    # Keep the main thread alive
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Program exiting...")