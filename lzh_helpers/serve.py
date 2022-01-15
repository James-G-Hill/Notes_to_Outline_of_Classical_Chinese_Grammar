from deplacy import (
    deplacy,
    to_conllu
)
from IPython.display import display
from IPython.lib.display import IFrame
from urllib.parse import quote

deplacy.EDITOR_URL = deplacy.EDITOR_URL.replace("editor.html", "viewer.svg")

def serve(doc, height=200):
    c = to_conllu(doc, False)
    display(
        IFrame(
            src=deplacy.EDITOR_URL+"#"+quote(c),
            width="100%",
            height=height,
            extras=['style="background-color: white;"']
        )
    )