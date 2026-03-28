def get_learning_path(label):

    if label in ["one", "two", "three", "four", "five"]:
        return ["Learn Numbers Basics", "Practice Counting", "Take Quiz"]

    elif label in ["left", "right", "forward", "backward"]:
        return ["Learn Directions", "Practice Movements", "Real-world Tasks"]

    elif label in ["cat", "dog", "bird"]:
        return ["Learn Animals", "Identify Sounds", "Animal Quiz"]

    else:
        return ["General Learning", "Practice", "Assessment"]