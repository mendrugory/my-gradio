import gradio


def greet(name):
    return "Hello " + name + "!"


demo = gradio.Interface(
    fn=greet, inputs="text", title='Hello from main', outputs="text"
)
demo.launch()
