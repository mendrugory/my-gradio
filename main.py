import gradio


def greet(name):
    return "Hello " + name + "!"

demo = gradio.Interface(fn=greet, inputs="text", title=f'Hello', outputs="text")
demo.launch()
