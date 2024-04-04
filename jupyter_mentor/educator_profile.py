# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/04_educator_profile.ipynb.

# %% auto 0
__all__ = ['EducatorProfileView']

# %% ../nbs/04_educator_profile.ipynb 1
from ipywidgets import VBox, HBox, HTML, Text, Button, Label

# %% ../nbs/04_educator_profile.ipynb 2
class EducatorProfileView(VBox):

    def __init__(self):
        super().__init__()

        # Username input
        self.username_label = Label('Name:')
        self.username_input = Text(placeholder='Enter your name')

        # Password input
        self.key_label = Label('Educator:')
        self.key_input = Text(placeholder='Enter Your Level', password=True)

        # Next button
        self.next_button = Button(description='Next')

        # Arrange labels and inputs horizontally
        self.username_box = HBox([self.username_label, self.username_input])
        self.key_box = HBox([self.key_label, self.key_input])

        # Arrange widgets vertically
        self.children = [
            HTML('<h2>User Profile</h2>'),  # Heading
            self.username_box,       # Username label and input box
            self.key_box,       # Password label and input box
            HBox([self.next_button], layout={'justify_content': 'flex-end'}),  # Login button aligned to the right
        ]
