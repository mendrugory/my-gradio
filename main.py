import gradio
from clearml import Task

task = Task.init()


def greet(name):
    return "Hello " + name + "!"


demo = gradio.Interface(
    fn=greet, inputs="text", title='Hello from main', outputs="text"
)
demo.launch()
