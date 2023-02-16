import gradio
from clearml import Task

task = Task.init(project_name="gonzaloproject", task_name="gradiosupertask")


def greet(name):
    return "Hello " + name + "!"


demo = gradio.Interface(
    fn=greet, inputs="text",
    title='Hola from local-network-no-patching',
    outputs="text"
)
demo.launch()
