# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/03_file_viewer.ipynb.

# %% auto 0
__all__ = ['FileViewer']

# %% ../nbs/03_file_viewer.ipynb 1
import ipywidgets as widgets
from ipywidgets import VBox, HBox, HTML, Button, Label, Text, Checkbox, Accordion, FileUpload
from IPython.display import display, clear_output
import ipyvuetify as v
from traitlets import observe

# %% ../nbs/03_file_viewer.ipynb 2
class FileViewer(VBox):
    
    def __init__(self):
        super().__init__()
        
        # File viewer (hidden in accordion)
        self.file_viewer_accordion = Accordion(children=[HTML('File viewer content')])
        self.file_viewer_accordion.selected_index = None  # Hide the accordion content initially

        # Arrange widgets vertically
        self.children = [
            self.file_viewer_accordion,  # File viewer (hidden initially)
        ]
