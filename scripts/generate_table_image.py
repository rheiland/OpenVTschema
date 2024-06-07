import json
import os
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import table

def load_instances(directory):
    instances = []
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r') as file:
                instances.append(json.load(file))
    return instances

def generate_table(instances):
    data = []
    for instance in instances:
        name = instance.get("name", "N/A")
        description = instance.get("description", "N/A")
        website = instance.get("website", "N/A")
        data.append([name, description, website])
    return pd.DataFrame(data, columns=["Name", "Description", "Website"])

def save_table_as_image(df, file_path):
    if df.empty:
        print("No data to display.")
        return

    # Create figure and axis
    fig, ax = plt.subplots(figsize=(12, len(df) * 0.5 + 1))
    ax.axis('off')

    # Create table
    tbl = table(ax, df, loc='center', cellLoc='center', colWidths=[0.2, 0.5, 0.3])
    tbl.auto_set_font_size(False)
    tbl.set_fontsize(12)

    # Style the table
    for key, cell in tbl.get_celld().items():
        cell.set_edgecolor('grey')
        if key[0] == 0:
            cell.set_text_props(weight='bold', color='white')
            cell.set_facecolor('black')

    # Adjust column widths
    for i in range(len(df.columns)):
        tbl.auto_set_column_width(i)

    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    plt.savefig(file_path, bbox_inches='tight', pad_inches=0.1, dpi=300)
    plt.close(fig)

def main():
    instances_directory = "instances"
    output_path = "docs/instances_table.png"

    instances = load_instances(instances_directory)
    df = generate_table(instances)
    save_table_as_image(df, output_path)

if __name__ == "__main__":
    main()
