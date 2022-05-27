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
        linesX = width / 14

        for i in range(3):
            self.create_line(
                linesX * (7 - (i + 1) * 0.5), linesY * (i + 2),
                linesX * (7 + (i + 1) * 0.5), linesY * (i + 2)
            )
            
        for i in range(5):
            self.create_line(
                linesX * (1 + i * 0.5), linesY * (i + 5),
                linesX * (13 - i * 0.5), linesY * (i + 5)
            )
            
        for i in range(4):
            self.create_line(
                linesX * (1 + i * 0.5), linesY * (13 - i),
                linesX * (13 - i * 0.5), linesY * (13 - i)
            )
            
        for i in range(3):
            self.create_line(
                linesX * (7 - (i + 1) * 0.5), linesY * (16 - i),
                linesX * (7 + (i + 1) * 0.5), linesY * (16 - i)
            )
            
        for i in range(3):
            self.create_line(
                linesX * (i + 2), linesY * 5,
                linesX * (2 + (i - 1) * 0.5), linesY * (i + 6)
            )
            
        for i in range(5):
            self.create_line(
                linesX * (i * 0.5 + 7), linesY * (i + 1),
                linesX * (i + 1), linesY * 13
            )
            
        for i in range(4):
            self.create_line(
                linesX * (i + 10), linesY * 5,
                linesX * ((i * 0.5) + 5.5), linesY * (14 + i)
            )
            
        for i in range(3):
            self.create_line(
                linesX * (i + 10), linesY * 13,
                linesX * (12 + (i - 1) * 0.5), linesY * (10 + i)
            )
            
        for i in range(3):
            self.create_line(
                linesX * (12 - i), linesY * 5,
                linesX * (12 - (i - 1) * 0.5), linesY * (i + 6)
            )
            
        for i in range(5):
            self.create_line(
                linesX * (7 - i * 0.5), linesY * (i + 1),
                linesX * (13 - i), linesY * 13
            )
            
        for i in range(4):
            self.create_line(
                linesX * (i + 1), linesY * 5,
                linesX * ((i * 0.5) + 7), linesY * (17 - i)
            )
            
        for i in range(3):
            self.create_line(
                linesX * (i + 2), linesY * 13,
                linesX * (2 + (i - 1) * 0.5), linesY * (12 - i)
            )
            
        for i in range(4):
            for j in range(i + 1):
                self.create_oval(
                    linesX * (7 + j - i * 0.5) - linesX / 4, linesY * (i + 1) - linesX / 4,
                    linesX * (7 + j - i * 0.5) + linesX / 4, linesY * (i + 1) + linesX / 4,
                    fill='white'
                )
                
        for i in range(5):
            for j in range(13 - i):
                self.create_oval(
                    linesX * (1 + j + i * 0.5) - linesX / 4, linesY * (i + 5) - linesX / 4,
                    linesX * (1 + j + i * 0.5) + linesX / 4, linesY * (i + 5) + linesX / 4,
                    fill='white'
                )
                
        for i in range(4):
            for j in range(10 + i):
                self.create_oval(
                    linesX * (2.5 + j - i * 0.5) - linesX / 4, linesY * (i + 10) - linesX / 4,
                    linesX * (2.5 + j - i * 0.5) + linesX / 4, linesY * (i + 10) + linesX / 4,
                    fill='white'
                )
                
        for i in range(4):
            for j in range(i + 1):
                self.create_oval(
                    linesX * (7 + j - i * 0.5) - linesX / 4, linesY * (17 - i) - linesX / 4,
                    linesX * (7 + j - i * 0.5) + linesX / 4, linesY * (17 - i) + linesX / 4,
                    fill='white'
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
