"""Pynecone card: custom card selection."""

# modules
import asyncio
import pynecone as pc


class State(pc.State):
    """The app state."""

    uid: list = [0, 1, 2]
    labels: list = ["Personal", "Streaming", "Shopping"]

    # main list
    items_list: list[list] = []
    for i in range(len(uid)):
        items_list.append([
            uid[i], labels[i],
        ])


def click_button(scale: str, bg: str):
    return pc.button(
        transform=scale,
        transition="all 0.35s ease transform 0.35s",
        border_radius="150px",
        background=bg,
        color_scheme="None",
        border="2px solid #45485f",
    )


def card_container(values: list):
    return pc.container(
        pc.hstack(
            pc.hstack(
                pc.text(
                    values,
                    font_weight="bold",
                )
            ),
            # mini credit card ui here
            spacing="20px",
        ),
        min_width="320px",
        height="62px",
        bg="lightblue",
        position="relative",
        cursor="pointer",
        #
        _hover={
            "border_color": "#4062F6",
            "background_color": "#313a51",
        },
    )


def index() -> pc.Component:
    return pc.center(
        # main ui here
        pc.vstack(
            # main ui here
            pc.foreach(State.items_list, card_container),
            # stack settings
            transform="scale(1.45)",
            box_shadow="0 30px 60px 0 rgba(90, 116, 148, 0.4)",
            padding="20px",
            border_radius="8px",
        ),
        # body settings
        bg="#313b44",
        width="100%",
        height="100vh",
        desiply="flex",
        dlex_direction="column",
        align_items="center",
        justify_content="center",
    )


# Add state and page to the app.
app = pc.App(state=State)
app.add_page(index)
app.compile()
