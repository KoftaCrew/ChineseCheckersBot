import tkinter as tk

class CheckerCanvas(tk.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.bind("<Configure>", self.redraw)

    def redraw(self, event):
        self.delete("all")

        width = event.width
        height = event.height

        wInterval = width / 3
        hInterval = height / 4

        self.create_polygon(
            width / 2, 0,
            wInterval, hInterval,
            wInterval * 2, hInterval,
            fill="#e2e9af"
        )

        self.create_polygon(
            0, hInterval,
            wInterval, hInterval,
            wInterval / 2, hInterval * 2,
            fill="#b1d6cf"
        )

        self.create_polygon(
            wInterval / 2, hInterval * 2,
            0, hInterval * 3,
            wInterval, hInterval * 3,
            fill="#ba9bc7"
        )

        self.create_polygon(
            wInterval, hInterval * 3,
            wInterval * 2, hInterval * 3,
            width / 2, height,
            fill="#ee7f81"
        )

        self.create_polygon(
            wInterval * 2, hInterval * 3,
            width, hInterval * 3,
            wInterval * 5/2, hInterval * 2,
            fill="#edc473"
        )

        self.create_polygon(
            wInterval * 2, hInterval,
            width, hInterval,
            wInterval * 5/2, hInterval * 2,
            fill="#faf373"
        )


        self.create_line(
            width / 2, 0,
            0, hInterval * 3,
            width, hInterval * 3,
            width / 2, 0,
        )

        self.create_line(
            width / 2, height,
            0, hInterval,
            width, hInterval,
            width / 2, height,
        )

        linesY = height / 18
        linesX = height / 14

        for i in range(2, 17):
            self.create_line(
                0, linesY * i,
                width, linesY * i
            )


class CheckerFrame(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.bind("<Configure>", self.redraw)

        self.canvasPadding = 25
        self.canvas = CheckerCanvas(self, borderwidth=0, highlightthickness=0, **kwargs)

    def redraw(self, event):
        padding = self.canvasPadding
        width = event.width - padding * 2
        height = event.height - padding * 2
        x = 0
        y = 0

        if(width * 4 / 3 < height):
            y = (height - width * 4 / 3) / 2 + padding
            x = padding
            height = width * 4 / 3
        else:
            x = (width - height * 3 / 4) / 2 + padding
            y = padding
            width = height * 3 / 4

        self.canvas.place(x= x, y= y, width= width, height= height)
