button_frame = tk.Frame(window)
button_frame.pack(pady=10)

record_button = tk.Button(button_frame, text="Record", font=font, fg=color, bg="#EB5E28", width=10, command=convert_audio)
record_button.pack(side=tk.LEFT, padx=5)

upload_button = tk.Button(button_frame, text="Upload", font=font, fg=color, bg="#EB5E28", width=10, command=lambda: os.system("start ."))
upload_button.pack(side=tk.LEFT, padx=5)

convert_button = tk.Button(window, text="Convert to Text", font=font, fg=color, bg="#EB5E28", width=20, command=convert_audio)
convert_button.pack(pady=10)

window.mainloop()