def traffic_light(color):
    if color.lower() == 'red':
        return "Stop"
    elif color.lower() == 'yellow':
        return "Caution"
    elif color.lower() == 'green':
        return "Go"
    else:
        return "Invalid color"

# Example usage
color = input("Enter the traffic light color (red, yellow, green): ")
action = traffic_light(color)
print(f"The action for {color} light is: {action}")
