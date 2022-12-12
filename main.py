from clearml import Task
import gradio


task = Task.init(project_name='test', task_name='gradio')


def patching(path):
    import gradio.networking
    import requests
    original_networking_start_server = gradio.networking.start_server
    
    response = requests.get("https://ipinfo.io")
    if response.status_code != 200:
        raise Exception("error retrieving ip")
    ip = response.json()["ip"]
    task._set_runtime_properties({"_SERVICE": "EXTERNAL", "_ADDRESS": ip, "_PORT": 7860})
    task.set_system_tags(["external_service"])
    print(f"path: {path}")

    def patched_networking_start_server(
        self=None,
        server_name=None,
        server_port=None,
        ssl_keyfile=None,
        ssl_certfile=None,
        ssl_keyfile_password=None,
        *args, **kwargs
    ):
        server_name = "0.0.0.0"
        server_port = 7860
        return original_networking_start_server(
            self, server_name, server_port, ssl_keyfile, ssl_certfile, ssl_keyfile_password, *args, **kwargs)

    gradio.networking.start_server = patched_networking_start_server

    import gradio.routes
    original = gradio.routes.App.__init__
    def patched_init(*args, **kwargs):
        kwargs["root_path"] = path
        kwargs["root_path_in_servers"] = False
        kwargs["server_name"] = "0.0.0.0"
        kwargs["server_port"] = 7860
        return original(*args, **kwargs)

    gradio.routes.App.__init__ = patched_init

patching(f"/service/{task.id}")

def greet(name):
    return "Hello " + name + "!"

demo = gradio.Interface(fn=greet, inputs="text", title=f'Hello from Task {task.id}', outputs="text")
demo.launch()


