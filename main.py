import gradio


def greet(name):
    return "Hello " + name + "!"


demo = gradio.Interface(fn=greet, inputs="text", title='Hello without clearml Task', outputs="text")
demo.launch()
