def PrintText(text,start_x,start_y,font_size=80):
    x_off = 0
    y_off = 0
    for c in range(len(text)):
        if x_off + (TextPositions.text_positions[text[c]]['Size'][0]*font_size) > 800:
            x_off = 0
            y_off += (1*font_size)
        for elm in TextPositions.text_positions[text[c]]["Vectors"]:
            for i in range(len(elm)):
                x1 = start_x + (elm[i-1][0]*font_size) + x_off
                y1 = start_y - (elm[i-1][1]*font_size) + y_off
                x2 = start_x + (elm[i  ][0]*font_size) + x_off
                y2 = start_y - (elm[i  ][1]*font_size) + y_off
                dist = numpy.linalg.norm(np.array([x1,y1]) - np.array([x2,y2]))
                device.shell(f"input touchscreen swipe {x1} {y1} {x2} {y2} {max(150,int(dist*8))}")
        x_off += (TextPositions.text_positions[text[c]]['Size'][0]*font_size) + 10
