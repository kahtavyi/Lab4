from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die

# Create two D6 dice.
die_1 = Die()
die_2 = Die(num_sides=22+3)  # Asymmetric die with N = n + 3

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)
    
# Analyze the results.
frequencies = []
max_result = die_1.num_sides * 2  # Максимальний результат кидка для двох симетричних кубиків
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
    
# Visualize the results.
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling two dice with one symmetric and one asymmetric (N=22+3) die 1000 times',
        xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='symmetric_asymmetric_dice.html')
