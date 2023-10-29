from tkinter import *
import openai

root = Tk()
root.geometry('500x500')
root.title('OpenAI-Python-Chatbot')

def search():
    openai.api_key='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'
    prompt = question.get()
    if prompt.lower()=='exit' or prompt.lower()=='quit':
        exit()
    else:
        response = openai.completions.create(
        model='gpt-3.5-turbo-instruct',
        prompt=prompt,
        max_tokens = 2000
        )
        myText.insert(END, response.choices[0].text)

Label(root, text='OpenAI-Python-Chatbot', font=('Helvetica', 13)).pack(padx=10, pady=20)

myText = Text(root, bg='#fff', fg='#000', insertbackground ='#fff', height=20)
myText.pack(padx=10, pady=20)

frameInput = Frame(root, borderwidth=6)
frameInput.pack(padx=10, pady=20, side=BOTTOM)

question = StringVar()
Entry(frameInput, textvariable = question, font=('Helvetica', 10)).grid(row=0, column=0, padx=(0, 10))

Button(frameInput, text='Submit', bg='#000', fg='#fff', command=search).grid(row=0, column=1, padx=(10, 0))

root.mainloop()